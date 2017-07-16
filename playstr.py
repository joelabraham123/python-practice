msg='good afternoon. Have a nice afternoon ahead.'
print(msg.capitalize())

name='joel abraham'
print(name.title())
print(msg.upper())	#and lower
print(msg.find('afternoon'))	#returns 5
print(msg.find('evening'))	#-1 since it is not found

msg1='		hello world      '
print(msg1.lstrip())	#rstrip()

print(len(msg))		

#substring
print(name[5:12])	#give index of last alphabet +1 
print(msg[16:37])

#replace
print(msg.replace('afternoon','evening'))

print(name.split(" "))

