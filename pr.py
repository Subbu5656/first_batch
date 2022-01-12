# l=[1,2,3,4,5,6,4,9,2,8,6]
# '''
# for i in range(0,len(l)):
#     for j in range(i+1,len(l)):
#         if(l[i]==l[j]):
#             print(l[j])
# '''
# d = {i:l.count(i) for i in l}
# for i in d:
# #print(d)
#     if d[i] > 1:
#         print(i)

# def add(num,num1):
#     product=num*num1
#     if product >= 1000:
#         return(product)
#     else:
#         return num+num1import os

# print(add(100,40))
# # result=add(20,30)
# # print(result)
# # result=add(30,44)
# # print(result)
# import os
# print(os.listdir('./radheshyam'))
# Program to find the ASCII value of the given character

sd="pyton is a very simple language"

     # METHOID ONE
l=sd.split()
d = {}
for i in l:
    d[i] = len(i)
print(d)

    # METHOD TWO USING DICTIONARY COMPREHENSION

print({i:len(i) for i in sd.split()})

    # METHOD THREE
d = {}
for i in sd.split():
    d[i]=len(i)
print(d)

