from collegeuser import CollegeUser

class Student(CollegeUser):
	def __init__(self,name,gender,rollno,marks):	#address of obj for which __init__ was called
		super().__init__(name,gender)
		self.rollno=rollno
		self.marks=marks

	def get_name_roll(self):
		t=(self.name,self.rollno)	#'t' is tuple containing name and rollno
		return t			#tuple is used when heterogenous list has to be passed

	def displayDetails(self):
		'''print("Name is ",self.name)
		print("Gender is ",self.gender)
		print("Rollno is ",self.rollno)'''
		#print("Name is : {0}\nGender : {1}\nRoll No : {2}".format(self.name,self.gender,self.rollno))
		#print("{name}\n{gender}\n{rollno}".format_map({'name':self.name,'rollno':self.rollno,'gender':self.gender}))
		super().displayDetails()
		print("Roll No : {0}".format(self.rollno))
	def studentGrade(self):
		if self.marks>=70 and self.marks<=100:
			print('A grade')
		elif self.marks>=60 and self.marks<70:
			print('B grade')
		elif self.marks>=40 and self.marks<60:
			print('C grade')
		elif self.marks>=0 and self.marks<40:
			print("Fail")
		else:
			print('Invalid Marks')

		
		

