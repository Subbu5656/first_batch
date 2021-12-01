
    # FUNCTIONS PROGRAMMING

def add(a,b): #called function 
	return a+b
#print(add(10,20)) #calling function

def mult(a,b):
	return a*b
#print(mult(10,20))

#method 2

l = [1,2,3,4,5,6]
l1 = list() #or []
def even(l):
	for i in l:
		if i%2 == 0:
			l1.append(i)
#print(even(l))
#print(even([1,2,3,4,5,6]))
#print(l1)

def add (a,b,c=0,d=0):
	return a+b+c+d
#print(add(10,20))
#print(add(10,20,30))
#print(add(10,20,40,40))

def mult(a,b):
	return a*b,a%b
#print(mult(20,30))

def add(*a):
 	return sum(a)
#print(add(10,40,30))
#print(add())
#print(add(10))
#print(add(1,2,3,4,5,6,7,8,9))

def add(a,b=0,*c):
	return a+b+sum(c)
print(add(10))
print(add(10,20))
print(add(10,20,1,2,3,4,5))

def kw(**d):
	print(d)
	print(type(d))
kw(a=10,b=20,c=30)
kw(a=10,b=20,c=30,e=40)

	