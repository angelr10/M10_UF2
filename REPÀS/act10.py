import random

numero = 0
random = random.randrange(1,100)
print(random)
salimos = False
while salimos != True:
	numero = input("Intenta adivinar el numero: ")
	if int(numero) == int(random):
		print("Lo has adivinado!")
		break
	else:
		print("Nice try")
		if int(numero) > int(random):
			print("el numero es menor")
		else:
			print("el numero es mayor")

