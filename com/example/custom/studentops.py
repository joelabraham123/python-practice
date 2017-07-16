def disp(name,gender,rollno):
	print("Name : ",name)
	print("Gender : ",gender)
	print("Roll no. : ",rollno)
def cal(marks):
	if marks>=70 and marks<=100:
		print('A grade')
	elif marks>=60 and marks<70:
		print('B grade')
	elif marks>=40 and marks<60:
		print('C grade')
	elif marks>=0 and marks<40:
		print("Fail")
	else:
		print('Invalid Marks')

