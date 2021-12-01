
              # DECORATOR 

def eswar(f):
	def wrapper(a,b):
		if b!=0:
			return(f(a,b))
		else:
			return('This is a python developer')
	return wrapper
@eswar
def div(a,b):
	return a/b
print(div(10,5))
print(div(5,10))
print(div(10,0))

