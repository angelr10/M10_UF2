while True:
	numero = input("Introduce un numero correspondiente a los meses del año: ")
	if int(numero) < 0 or int(numero) > 12:
		numero = input("Introduce un numero valido correspondiente a los meses del año: ")
	tuplaB = ()
	tuplaB = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","AbrilSeptiembre","Octubre","Noviembre","Diciembre")
	if int(numero) == 0:
		print("Goodbye!!!")
		break
	elif int(numero) == 1:
		print(tuplaB[0])
	elif int(numero) == 2:
		print(tuplaB[1])
	elif int(numero) == 3:
		print(tuplaB[2])
	elif int(numero) == 4:
		print(tuplaB[3])
	elif int(numero) == 5:
		print(tuplaB[4])
	elif int(numero) == 6:
		print(tuplaB[5])
	elif int(numero) == 7:
		print(tuplaB[6])
	elif int(numero) == 8:
		print(tuplaB[7])
	elif int(numero) == 9:
		print(tuplaB[8])
	elif int(numero) == 10:
		print(tuplaB[9])
	elif int(numero) == 11:
		print(tuplaB[10])
	elif int(numero) == 12:
		print(tuplaB[11])
	elif int(numero) == 13:
		print(tuplaB[12])
