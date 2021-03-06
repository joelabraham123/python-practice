from sys import intern		#sys is module intern is function

n1='joel'		#calculation of n2 is done at runtime
n2='j'+' oel'		#cache only stores if there is no space in between
print(n1 is n2)	#False	#a-z,A-Z,0-9 are accepted

n1='joel'		
n2='j'+'oel'		
print(n1 is n2)	#True	#no space     #calculation of n2 is done at runtime

n1='joel abraham'	#since no calculation has to be done at the runtime so output is true
n2='joel abraham'
print(n1 is n2)	#True

a=4+5
b=8+1
print(a is b)	#True

c=255+2
d=254+3
print(c is d)	#False	#cache range is -5 to 256
print(c==d)	#True

e=258
d=258
print(e is d)	#True

n1=intern('joel abraham')
n2=intern('joel'+' abraham')
print(n1 is n2)  #True
