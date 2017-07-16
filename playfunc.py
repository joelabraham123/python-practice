def add(*nos):		#positional argument packing
	#print(type(nos)) #is a tuple
	sum=0
	for n in nos:
		sum+=n
	return sum

print(add())
print(add(3,4))
print(add(5,6,7,8,9))

#positional argument unpacking
def two_adder(a,b):
	return a+b

l=[5,4]
print(two_adder(*l))	#you can take as many arguments 

#keyword argument packing
def perimeter(**stats):
	#print(type(stats))  #dict
	return 2*(stats['l']+stats['b'])

print(perimeter(l=6,b=3))	
#print(perimeter(6,3))	#wont work

#keyword argument unpacking
def area(length,breadth):
	return length*breadth

s={'length':6,'breadth':3}
print(area(s['length'],s['breadth']))
print(area(**s))
