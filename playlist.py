cars=['mercedes','audi','ferrari']
print(type(cars))	#list class	first index position is zero

cars[0]='Mercedes'
print(len(cars))

print(cars[len(cars)-1])	#always access last element of list

cars.append("Lamborghini")		#gives same index to bunch of newly added
print(cars)

cars.extend(['i20','i10'])		#gives different index to each new added
print(cars)

cars.insert(1,'Porsche')
print(cars)

print(cars.pop())
print(cars)
 
print(cars.pop(2))
print(cars)

for car in cars:
	print(car)

cars.sort()			#capital letters comes before small letters in ascending order,numbers come before capital letters
print(cars)			

'''cars.reverse()			#descending
print(cars)'''
#or
cars.sort(reverse=True)
print(cars)

nos=[1,2,3,4,5,6,7,8,9]
'''sqnos=[]
for n in nos:
	sqnos.extend([n**2])'''
sqnos=[n**2 for n in nos]
print(sqnos)

evensq=[n**2 for n in nos if n%2==0]
print(evensq)

evencube=[n**3 for n in nos if n>4 and n%2==0]
print(evencube)


