a = input("Inserta el primer caracter: ")
b = input("Inserta el segon caracter: ")
obtenA = a[0]
obtenB = b[0]
punto = 0
nuevoA = ""
nuevoB = ""
while punto < len(a):
	if punto == 0:
		nuevoA = nuevoA+obtenB
	else:
		nuevoA = nuevoA+a[punto]
	punto = punto + 1

punto = 0
while punto < len(b):
	if punto == 0:
		nuevoB = nuevoB+obtenA
	else:
		nuevoB = nuevoB+b[punto]
	punto = punto + 1
print(nuevoA)
print(nuevoB)
