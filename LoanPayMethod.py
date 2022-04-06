class PayMethods:

	def __init__(self,base_rate,ratio):
		#基准利率和上浮比例
		self.base_rate = base_rate
		self.ratio = ratio
	
	#等额本金
	def monthlyPaymentAverageCapital(self,total, n, months=120):
		yearly_interest = self.base_rate * self.ratio
		monthly_interest = yearly_interest / 12
		payment_per_month = total / months
		interest = (total - (n - 1) * payment_per_month) * monthly_interest 
		return payment_per_month + interest

		#print out a list
		#print([round (test.monthlyPaymentAverageCapital(450000, n),2) for n in range(1,121)])
		
		
	#等额本金总利息
	def averageCapitalTotalInterest(self,total,months=120):
		yearly_interest = self.base_rate * self.ratio
		return (months+1)*total*(yearly_interest/12)/2
		#print(test.averageCapitalTotalInterest(450000))
		
		

	#等额本息
	def monthlyPaymentAverageCapitalInterest(self,total, months=120):
		yearly_interest = self.base_rate * self.ratio
		monthly_interest = yearly_interest / 12
		compound = (1+monthly_interest) ** months
		return total * compound * monthly_interest / (compound - 1)
		#print(round (test.monthlyPaymentAverageCapitalInterest(450000.00), 2))
	
	#等额本息总利息
	def averageCapitalInterestTotalInterest(self,total, months=120):
		yearly_interest = self.base_rate * self.ratio
		return self.monthlyPaymentAverageCapitalInterest(total)*months - total
		#print(test.averageCapitalInterestTotalInterest(450000))
		

#test = PayMethods(0.049,1.3)
#print([round (test.monthlyPaymentAverageCapital(450000, n),2) for n in range(1,121)])
#print(round(test.averageCapitalTotalInterest(450000),2))
#print()
#print()
#print(round (test.monthlyPaymentAverageCapitalInterest(450000), 2))
#print(round (test.averageCapitalInterestTotalInterest(450000),2))



test = PayMethods(0.049,1.3)
print([round (test.monthlyPaymentAverageCapital(450000, n),2) for n in range(1,121)])
print(round(test.averageCapitalTotalInterest(450000),2))
print()
print()
#print(round (test.monthlyPaymentAverageCapitalInterest(450000), 2))
#print(round (test.averageCapitalInterestTotalInterest(450000),2))