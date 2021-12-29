class student:
d=0
    def__init__(self,d):
       self.d=d
       
    def add(self):
    	c=self.d[0]+self.d[1]
    	print(c)
    	
d=list(map(int,input("enter the values:").split(" ")))
s=student(d)	
s.add()        
