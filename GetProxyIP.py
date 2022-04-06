
# !/usr/bin/env python
# -*- coding: utf-8 -*-
 
import requests
from lxml import etree

#获取西刺代理网站上的有用代理IP


'''
功能表：
2019.01.26：抓取西刺上的高匿IP --done
2019.01.26：输出可用的高匿IP集合 --done
2019.01.26：输入高匿IP集合，判断单个IP的活性 --done
2019.01.27：抓取西刺代理后，保存IP
''' 


class GetProxyIP:
	
	
	def __init__(self):
		pass
		

	
	#输入开始页，终止页，得到一批未知活性的代理IP
	def getRawProxyIPList(self,startPage=1,endPage=6):
		rawIPList = []
		for i in range(startPage,endPage):
			#请求路径，西刺代理网站
			url = 'https://www.xicidaili.com/nn/'+str(i)
			print(url)
			#url = 'https://www.xicidaili.com/nn'
			#请求响应头
			headers =  {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
			#通过requests的get方法访问目标网站，获得响应对象
			response = requests.get(url=url,headers=headers)
			#创建一个etree对象，response.text为访问后的到的整个西刺代理页面
			etree_obj = etree.HTML(response.text)
			#通过筛选response.text，得到包含ip信息的列表
			ip_list = etree_obj.xpath("//tr[@class='odd']")
			#遍历得到的集合，将ip，和端口信息进行拼接，添加到IPList列表
			for ip in ip_list:
				ip_num = ip.xpath('./td[2]/text()')[0]
				port_num = ip.xpath('./td[3]/text()')[0]
				http = ip_num + ':' +port_num
				rawIPList.append(http)
		#print(rawIPList)
		return rawIPList
			
			
		#输入IPList列表，检测IP活性,输出所有可用IP集
	def checkALLProxyAvailability(self,IPList):	
			#请求响应头
			headers =  {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}		
			proxyList = []
			#遍历访问,检测列表中IP活性
			for it in IPList:
				#因为并不是每个IP都是能用，所以要进行异常处理
				try:
					proxy = {
						'http':it
					}
					url1 = 'https://www.baidu.com/'
					#遍历时，利用访问百度，设定timeout=1,即在1秒内，未送到响应就断开连接
					res = requests.get(url=url1,proxies=proxy,headers=headers,timeout=1)
					#打印检测信息，elapsed.total_seconds()获取响应的时间
					#print(it +'--',res.elapsed.total_seconds())
					proxyList.append(it)
					#print(proxyList)
				except BaseException as e:
					#print(e)
					pass
					
			return proxyList
			
		#输入单个IP，检测IP活性,输出 是否	
	def checkSingleProxyAvailability(self,it):	
		
			#请求响应头
			headers =  {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}		
			#检测列表中IP活性
			try:
				proxy = {
					'http':it
				}
				url1 = 'https://www.baidu.com/'
				#url1 = 'https://www.anjuke.com/'
				#遍历时，利用访问百度，设定timeout=1,即在1秒内，未收到响应就断开连接
				res = requests.get(url=url1,proxies=proxy,headers=headers,timeout=1)
				#打印检测信息，elapsed.total_seconds()获取响应的时间
				#print(it +'--',res.elapsed.total_seconds())
				return True
			except BaseException as e:
				#print(e)
				return False
				

'''
test = GetProxyIP()
test.getRawProxyIPList(10,11)
'''

					
'''
test = GetProxyIP()
print("collecting ALL available proxys......")
item = test.getRawProxyIPList(10,11)
result = test.checkALLProxyAvailability(item)
print (result)
'''


'''
test = GetProxyIP()
print("checking single proxy ......")
IPList = test.getRawProxyIPList(10,11)
for it in IPList:
	result = test.checkSingleProxyAvailability(it)
	print (result)
'''