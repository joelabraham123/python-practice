from collegeuser import CollegeUser

class Professor(CollegeUser):
	def __init__(self,name,gender,subject):	#address of obj for which __init__ was called
		super().__init__(name,gender)
		self.subject=subject

	def displayDetails(self):
		#print("{name}\n{gender}".format_map({'name':self.name,'gender':self.gender}))
		super().displayDetails()
		if len(self.subject) is 0:
			print('No subjects')
		else:
			print(self.subject)
				
		


		

