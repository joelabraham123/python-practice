from professor import Professor
name=input("\nEnter the name of professor : ")
gender=input("Gender : ")
subject=input("Subject : ")
print("---------Details---------")
p=Professor(name,gender,subject)	#p is object
p.displayDetails()

