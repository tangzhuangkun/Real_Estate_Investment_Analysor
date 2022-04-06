import GetProxyIP
import urllib
import random
import fake_useragent


#封装所有的伪装方法

'''
功能表：
2019.01.27： --done
2019.01.27：
''' 

class Disguise:
	
	def __init__(self):
		pass
	
	#得到一批未知活性的代理IP
	def getRawIPList(self):
		rawIPList = GetProxyIP.GetProxyIP().getRawProxyIPList()
		return rawIPList
	
	#通过代理IP发送请求,获得页面的详细信息
	def requestByProxyIP(self,url,header,rawIPList):
		exist = False
		randomIP = ''
		#只要代理IP无活性，就重新选取一个
		while (exist==False):
			# 随机选择一个代理
			randomIP = random.choice(rawIPList)
			exist = GetProxyIP.GetProxyIP().checkSingleProxyAvailability(randomIP)
		proxy_ip = {'http' : randomIP}
		# 使用选择的代理构建代理处理器对象
		#print("using Proxy IP: ",proxy_ip)
		#print()
		httpproxy_handler = urllib.request.ProxyHandler(proxy_ip)
		opener = urllib.request.build_opener(httpproxy_handler)
		page = urllib.request.Request(url,headers=header)
		page_info = opener.open(page).read().decode('utf-8')
		return page_info
		
	
	#方法1：产生一个随机的假的头文件	
	def getAFakeHeader(self):
		#ua = fake_useragent.UserAgent(use_cache_server=False)
		#print("hello kun kun kun ")
		ua = fake_useragent.UserAgent(verify_ssl=False).random
		fakeUA = {'User-Agent' : ua}
		return fakeUA
		
		
	'''
	#方法2.1：随机产生n个假的头文件集合
	def generateFakeHeadersList(self,n):
		fakeHeadersList = list()
		for i in range(n):
			ua = fake_useragent.UserAgent(verify_ssl=False).random
			fakeUA = {'User-Agent' : ua}
			fakeHeadersList.append(fakeUA)
		return fakeHeadersList
	#方法2.2:选择一个随机的假的头文件	
	def chooseAFakeHeader(self,fakeHeadersList):
		fakeUA= random.choice(fakeHeadersList)
		return fakeUA
	
	'''
	
	
	

'''
test = Disguise()
rawIPList = ['119.101.114.172:9999', '115.239.24.253:9999', '1.192.240.45:9999', '125.123.143.38:9999', '111.181.53.112:9999', '220.176.36.15:8118', '119.101.117.157:9999', '121.61.2.3:9999', '110.83.40.83:9999', '119.101.116.64:48303',]
test.requestByProxyIP(rawIPList)
'''

'''
test= Disguise()
fakeHeadersList = test.generateFakeHeadersList()
UA=test.chooseAFakeHeader(fakeHeadersList)
print(UA)
'''