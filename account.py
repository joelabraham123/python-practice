class InsufficientBalError(Exception):	#user defined exception
	
	def __init__(self.msg):
		super().__init__(msg)
class Account:
	def __init__(self,acc_no,bal,min_bal):
		self.acc_no=acc_no
		self.bal=bal
		self.min_bal=min_bal

	def withdraw(self,amt):
		if self.bal-amt<self.min_bal:
			#print("Insufficient balance")
			raise InsufficientBalError("Current balance is : {0}".format(self.bal))
		
		self.bal=self.bal-amt
		return self.bal
