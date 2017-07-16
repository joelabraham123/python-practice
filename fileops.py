'''file=open("/home/dbit/Desktop/python_31/playlist.py","r")
for l in file:
	print(l)
file.close()
'''
file=open("/home/dbit/Desktop/python_31/tmp.txt","wt")
name=input("Enter")
file.write(name+'|'+name)
file.close()
