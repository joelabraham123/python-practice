#this is a function definition for various methods for a reactangle

def area(l,b):
	a=l*b
	return a
def peri(l,b):
	p=2*(l+b)
	return p
'''what follows is the variable creation and calling 
the function for a rectangle'''
l=int(input("Length : "))
b=int(input("Breadth : "))
area=area(b,l)
perimeter=peri(b,l)
print('Area is ',area)
print('Perimeter is ',perimeter)
print('Area is '+str(area))
print('Perimeter is '+str(perimeter))

