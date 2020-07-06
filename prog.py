import math


def binary(n):
	s = ''
	while n > 0:
		s = str(n%2) + '  ' + s
		n //= 2
	while len(s) < len(leng):
		s = str('0') + '  ' + s
	return s




def addition(mass):
	mass_1 = []
	for i in range(0, len(mass)):
		if i + 1  < len(mass):
			mass_1.append(mass[i] + mass[i+1])
			if mass_1[i] == 2:
				mass_1[i] = 0
	return mass_1
file = open("dict.txt", 'r')
def tab(val):
	str = ''
	str = '  '*(2*val)
	return str
print("Input func values")
k = 0
while k != 1:
	leng = input()
	leng_mass = []
	try:
		for i in range(0, len(leng)):
			leng_mass.append(int(leng[i]))
		base = int(math.log(len(leng), 2))
	except BaseException:
		k = 0
	else:
		k = 1
strok = ''
for i in range(base):
	strok += 'x' + str(i+1) + ' '
print(strok)
stro = tab(base)
print(binary(0) + '  ' + leng)
j = 0
mass_1 = addition(leng_mass)
while j < len(leng_mass):
	s =''
	for i in range(len(mass_1)):
		s = s + str(mass_1[i])
	if j + 1 < len(leng_mass):
		data = binary(j+1)
		mass_1 = addition(mass_1)
		print(data + '  ' + s)
	j = j + 1
