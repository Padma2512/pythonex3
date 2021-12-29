class student():
	def getdata():
		a=input("enter the name:")
 		print(a)
 		a1=int(input("enter the subjects:"))
 		print(a1)
 		b=list(map(int,input("enter the marks:").split(" ")))
 		print(b)
		c=b[0]+b[1]+b[2]
 		print(c) 
 	def average():
 		d=c/a1
 		print(d)
print(student.getdata())
print(student.average())
 	
