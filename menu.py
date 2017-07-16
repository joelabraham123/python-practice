'''import patterns
import math'''
from com.example.custom.patterns import fib
from com.example.custom.math import evenodd as eo	#alias to avoid function name conflict

while True:
	print("\n1.Fibonacci")
	print("2.Even Odd")
	print("3.Exit")
	choice=int(input("Enter choice : "))
	if choice is 1:
		num=int(input("\nEnter number of terms : "))
		fib(num)
	elif choice is 2 :
		num =int(input("\nEnter the number : "))
		eo(num)
	elif choice is 3:
		break
	else:
		print("\nInvalid input")
