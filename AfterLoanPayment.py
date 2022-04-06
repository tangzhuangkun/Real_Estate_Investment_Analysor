import LoanPayMethod


'''
本方法用于计算每月付完房租之后的资金情况

功能表：
1.调用本地LoanPayMethod文件下的方法，等额本金，等额本息
2.

'''



class LoanPayment:
	def __init__(self,monthly_rent,rent_increase_ratio,base_rate,ratio):
		#每月房租，每年上涨幅度,基准利率和上浮比例
		self.monthly_rent = monthly_rent
		self.rent_increase_ratio = rent_increase_ratio
		self.base_rate = base_rate
		self.ratio = ratio
		
		
	#以等额本息方式还贷款	
	def payByAverageCapitalInterest(self,total, months=120):
		this_month_rent = self.monthly_rent
		method = LoanPayMethod.PayMethods(self.base_rate,self.ratio)
		monthly_payment = round(method.monthlyPaymentAverageCapitalInterest(total),2)
		#print("贷款"+str(monthly_payment))
		#print()
		for i in range(months):
			'''
			print("第"+str(i+1)+"月",end='  ')
			print("本月房租"+str(this_month_rent),end='  ')
			print("贷款"+str(monthly_payment),end='  ')
			print("剩余"+str(round((this_month_rent-monthly_payment),2)))
			'''
			
			if i%12==11:
				this_month_rent =round(this_month_rent * (1+ self.rent_increase_ratio),2)
				#print("-------------------")


#以等额本金方式还贷款	
	def payByAverageCapital(self,total, months=120):
		this_month_rent = self.monthly_rent
		method = LoanPayMethod.PayMethods(self.base_rate,self.ratio)
		monthly_payment_list = [round (method.monthlyPaymentAverageCapital(total, n),2) for n in range(1,121)]
		for i in range(months):
			monthly_payment = monthly_payment_list[i]
			
			
			print("第"+str(i+1)+"月",end='  ')
			print("本月贷款"+str(monthly_payment_list[i]),end='  ')
			print("本月房租"+str(this_month_rent),end='  ')
			print("剩余"+str(round((this_month_rent-monthly_payment),2)))
			
			if i%12==11:
				this_month_rent =round(this_month_rent * (1+ self.rent_increase_ratio),2)
				print("-------------------")



test = LoanPayment(8753, 0.05, 0.049, 1.3)
#test.payByAverageCapitalInterest(500000)
print()
print()
print()
print()
print()
print()
test.payByAverageCapital(480000)
