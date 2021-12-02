
          # TASK 

data = '''101 ravi hp hyderabad 40000
102 linga hp banglore 45000
103 eswar infosys chennai 35000'''

    # OUTPUT = 40000+45000+35000 = (120000)

            # METHOD 1(FOR LOOP (APPEND))

l = []
for i in data.splitlines():
	salary = data.split()[4]
	l.append(int(salary))
print(sum(l))

            # METHOD 2 (USING COUNT)

count = 0
for i in data.splitlines():
	salary = i.split()[4]
	count = count+int(salary)
print(count)

            # METHOD 3 (USING DEF FUNCTIONS)

def total(data):
	count = 0
	for i in data.splitlines():
		salary = int(i.split()[4])
		count += salary
	return count
print(total(data))

            # METHOD 4 (USING LIST COMPREHENSION) MOST IMPORTANT

print(sum([int(data.split()[4]) for i in data.splitlines()]))

            # METHOD 5
def total(data):
	return(sum([int(i.split()[4]) for i in data.splitlines()]))
print(total(data))


