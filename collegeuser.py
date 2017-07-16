class CollegeUser:
	def __init__(self,name,gender):
		self.name=name
		self.gender=gender

	def displayDetails(self):
		print("Name : {0}\nGender : {1}".format(self.name,self.gender))
		
