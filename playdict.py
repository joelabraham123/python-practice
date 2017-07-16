student_details={}
student_details[96]=('joel',96,'M')	#add item to dict,key-value
student_details[17]=('steve',17,'M')
student_details[25]=('katrina',25,'F')

#access element from dict
#print(student_details[17])
#print(student_details)

#check presence of key
if 65 in student_details:
	print(student_details[65])
else:
	print("Not found")

for s in student_details:	#print keys
	print(s)

for s in student_details.items():
	print(s[0],'-'+s[1][0])
'''for s in student_details.values():	#print values
	print(s)'''
print(len(student_details))
