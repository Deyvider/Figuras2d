import math
def menu():
	
	print ("Selecciona una opción")
	print ("\t1 - Crear figura")
	print ("\t2 - Listar una clasificación de figuras")
	print ("\t3 - Listar todas las figuras")
	print ("\t4 - Mostrar suma de todas las áreas")
	print ("\t5 - Mostrar la suma de todos los perímetros")
	print ("\t6 - Limpiar listas")
	print ("\t0 - salir")

def crear_cuadrado (lado):
	
	Cuadrado = {"FIGURA":"Cuadrado", "AREA":area_cudrado(lado), "PERIMETRO":perimetro_cuadrado(lado)}
	#print(Cuadrado)
	

def area_cudrado(lado):
	a = lado * lado
	return a

def perimetro_cuadrado(lado):
	p = lado*lado*lado*lado
	return p
#######################################################################
def crear_trianguloEQUI (lado_c):
	
	TrianguloEQuilatero = {"FIGURA":"Triangulo Equilatero", "AREA":area_trianguloEQUI(lado_c), "PERIMETRO":perimetro_trianguloEQUI(lado_c)}
	#print(TrianguloEQuilatero)

def area_trianguloEQUI(lado_c):
	altura = (math.sqrt(3)*lado_c)/2
	a = (lado_c*altura)/2
	return a

def perimetro_trianguloEQUI( lado_c):
	p = lado_c*lado_c*lado_c
	return p
#######################################################################
def crear_trianguloISO (lado_a, lado_b, lado_c):
	
	TrianguloISOSELES = {"FIGURA":"Triangulo isoseles", "AREA":area_trianguloISO(lado_a, lado_b, lado_c), "PERIMETRO":perimetro_trianguloISO(lado_a, lado_b, lado_c)}
	#print(TrianguloEQuilatero)

def area_trianguloISO(lado_a, lado_b, lado_c):
	altura = math.sqrt(((lado_a*lado_a)-(lado_b*lado_b))/4)
	a = (lado_b*altura)/2
	return a

def perimetro_trianguloISO( lado_a, lado_b, lado_c):
	p = lado_a+lado_b+lado_c
	return p
#######################################################################
def crear_trianguloESCA (lado_a, lado_b, lado_c):
	
	TrianguloEscaleno = {"FIGURA":"Triangulo Escaleno", "AREA":area_trianguloESCA(lado_a, lado_b, lado_c), "PERIMETRO":perimetro_trianguloESCA(lado_a, lado_b, lado_c)}
	#print(TrianguloEQuilatero)

def area_trianguloESCA(lado_a, lado_b, lado_c):
	sp= lado_a+lado_b+lado_c
	a = math.sqrt(sp*(sp-lado_a)*(sp-lado_b)*(sp-lado_c))
	return a

def perimetro_trianguloESCA( lado_a, lado_b, lado_c):
	p = lado_a+lado_b+lado_c
	return p
#######################################################################
def crear_circulo(radio):
	Circulo = {"FIGURA":"Circulo", "AREA":area_circulo(radio), "PERIMETRO":perimetro_circulo(radio)}
	#print(Circulo)

def area_circulo(radio):
	a = math.pi * (radio * radio)
	return a

def perimetro_circulo(radio):
	p = 2*math.pi*radio

def menu_figuras():
	print ("Selecciona una opción")
	print ("\t1 - Cuadrado")
	print ("\t2 - Triangulo")
	print ("\t3 - Circulo")
	print ("\t0 - SALIR")
	while True:
		opcion = int(input("---> "))
		if opcion == 1:
			lado = int(input("\tIngrese el lado del cuadrado----> "))
			crear_cuadrado(lado)	
		if opcion == 2:
			print ("Tipos de triangulos")
			print ("\t1 - Equilatero")
			print ("\t2 - Isoseles")
			print ("\t3 - Escaleno")
			Tipo = int(input("Ingrese el tipo de triangulo----> "))
			if Tipo == 1:
				print("TRIANGULOS EQUILATEROS")
				lado_c = int(input("\tIngrese el lado del triangulo----> "))
				crear_trianguloEQUI(lado_c)
			if Tipo == 2:
				print("TRIANGULOS 	ISOSELES")
				lado_a = int(input("\tIngrese el lado A (Lado igual a C)del triangulo----> "))
				lado_b = int(input("\tIngrese el lado B del triangulo----> "))
				lado_c = int(input("\tIngrese el lado C (Lado igual a A)del triangulo----> "))
				crear_trianguloISO(lado_a, lado_b, lado_c)
			if Tipo == 3:
				print("TRIANGULOS ESCALENOS")
				lado_a = int(input("\tIngrese el lado A del triangulo----> "))
				lado_b = int(input("\tIngrese el lado B del triangulo----> "))
				lado_c = int(input("\tIngrese el lado C del triangulo----> "))
				crear_trianguloESCA(lado_a, lado_b, lado_c)
		if opcion == 3:
			radio = int(input("\tIngrese el radio del radio----> "))
			crear_circulo(radio)
		if opcion == 0:
			print("Saliste")	
			break
def listar_clasificacion(clasificacion):
	if clasificacion == Cuadrado:
		print(Cuadrado)
	if clasificacion == Circulo:
		print(Circulo)
	if clasificacion == Triangulos:
		print("SELECIONE UN TRIANGULO")
		print("\n 1. Equilatero")
		print("\n 2. Isoseles")
		print("\n 3. Escaleno ")
		t = int(input("----> "))
		if t == 1:
			print(TrianguloEQuilatero)
		if t == 2:
			print(TrianguloISOSELES)
		if t == 3:
			print(TrianguloEscaleno)
		if t== 0:
			print("SALISTE")
			break
	else:
		print ()
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
			
		

def imprimir():
	print(Cuadrado)
	print(Circulo)
	print(TrianguloEQuilatero)
	print(TrianguloISOSELES)
	print(TrianguloEscaleno)


while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = int(input("Selecciona una opcion >> "))
 
	if opcionMenu==1:
		menu_figuras()
		input("\npulsa una tecla para continuar")
	if opcionMenu==2:
		print("\nCLASIFICACION ")
		print ("\n Cuadrado")
		print ("\n Triangulos")
		print ("\nCirculo")
		clasificacion = input("Ingrese la clasificacion de las figuras ")
		listar_clasificacion(clasificacion)
		input("pulsa una tecla para continuar")
	if opcionMenu==3:
		imprimir()
		input("\npulsa una tecla para continuar")
	if opcionMenu == 4:
		sumador_areas()
		input("\npulsa una tecla para continuar")
	if opcionMenu == 5:
		sumador_perimetros()
		input("\npulsa una tecla para continuar")
	if opcionMenu == 6:
		Cuadrado.clear()
		print ("Eliminaste todo Limpiaste la lista")
		input("\npulsa una tecla para continuar")	

	if opcionMenu == 0:
		print("Saliste")
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
		