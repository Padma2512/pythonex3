a=list(map(int,input("enter the marks:").split(" ")))
print(a)
total=a[0]+a[1]+a[2]
print("total:",total)
b=total/3
print("average:",b)
if b>=90 and b<=99:
	print("a grade")
elif b>=80 and b<=89:
	print("b grade")
elif b>=70 and b<=79:		
	print("c grade")
elif b<=69:
	print("fail")
