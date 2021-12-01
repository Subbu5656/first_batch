data=''' 101 siva hcl hydrabad 14000
102 sreenu hcl chennai 25000
103 suri hcl banglore 30000
104 subbu ibm kerala 35000
105 kari ibm hydrabad 40000'''
d={}
for i in data.splitlines():
	d[i.split()[0]]={'name':i.split()[1],'company':i.split()[2],'location':i.split()[3],'salary':int(i.split()[4])}
	print(d)



# class D:
# 	def __init__(self,id):
# 		self.id = id
# 		details = d.get(self.id)
# 		print(details)
# 		self.balance = details.get('salary')
	
# 	def deposit(self,amount):
# 		print(self.balance)
# 		self.balance = self.balance + amount
# 		return('{} add to ur account current ur total balance is:{}'.format(amount,self.balance))
	
# 	def withdraw(self,amount1):
# 		print(self.balance)
# 		self.balance = self.balance - amount1
# 		return('{} less to ur account current ur total balance is:{}'.format(amount1,self.balance))

# obj=D('105')
# print(obj.deposit(10000))
# print(obj.withdraw(20000 ))
# # class S:
# # 	__x=10
# # 	__y=30
# # 	def __ss(self):
# # 		return self.__x / self.__y
	
# # 	def __add(self,a,b):
# # 		return self.__x + b
	
# # 	def __even(self,a,b):
# # 		a=self.__x
# # 		b=self.__y
# # 		return a*b
# # obj=S()
# # print(obj._S__ss())
# # # print(obj._S__add(100,33))
# # # print(obj._S__x)
# # # print(obj._S__y)
# # # print(obj._S__even(20,33))

# # # def add(a,b,c):
# # # 	return a+b+c

# # # def add(a,b,c=0):
# # # 	return a+b+c
# # # print(add(4,5,6))
# # # print(add(10,20))
 
# # class D:
# # 	def add(self,a,b):
# # 		return a+b
# # class C:
# # 	def add(self,a,b):
# # 		return a*b
# # obj=D()
# # print(obj.add(10,20))
# # obj=C()
# # print(obj.add(33,33)) 





