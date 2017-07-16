print("program starts")		#error is passed to you by bif 'int' and you sent it to python intrepreter and it displays 'valueError' called as exception
for i in range(0,3):
	n1=input('enter n : ')

	try:
		n2=int(n1)
		#print('value taken is {0}'.format(n2))	#only a func can create a scope for variable,whereas in Java variable scope is always inside the block in which it is defined(no block scoping in python)
		break
	except ValueError:
		print("Please enter a proper value")
	else:
		print('value taken is {0}'.format(n2))
		break
print("program ends")
#else block will execute when no exception occurs in the corresponding try block

print(1)