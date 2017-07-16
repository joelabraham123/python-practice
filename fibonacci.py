num=int(input("Enter number of terms : "))
i,fib,num1,num2=0,0,0,1
print("0\n1")
for i in range(0,num-2):
	fib=num1+num2
	print(fib)
	num1,num2=num2,fib
	
	
