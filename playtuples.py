student1=('joel',31,'M')
print(type(student1))

print(student1)

for s in student1:
	print(s)
#student1[0]='skdjh'	#tuple is immutable, so it works faster than a list so it gives error here,pop is not a function of tuple
s=('joel')
print(type(s))

nos=[3,4,5]
t=tuple(nos)	#converting nos list into tuple
print(t)
r=list(student1)	#converting tuple student1 into list
print(r)

ages=[20,21,22,20,20,23,24,20,23,24]
unique_ages=set(ages)	#set is unordered collection of elements but there will be unique elements,duplicates will be discarded
print(unique_ages)	#set is declared in '{}',list in '[]' and tuple in '()'

alphabets={'a','b','a','c','d','s','a','e','d','f','d'}
numbers={1,2,3,4,3,2,1,5,6,7,87}
print(numbers)
print(alphabets)
#print(alphabets[0])		#set does not support indexing so you cannot access single element

for a in alphabets:
	print(a)

a={1,3,5,7}
b={3,5,8}

print(a-b)	#in a but not in b
print(a&b)	#elements present in both a and b
print(a|b)	#in a or b
print(a^b)	#complement of a&b	(a or b)-(a and b)

#empty set
e={}
print(type(e))	#e is dict

e=set()
print(type(e))

e.add(4)
e.add(5)
e.add(4)
e.add(3)
e.add(3)

print(e)

