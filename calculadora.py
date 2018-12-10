#encoding: utf:8
def operacion(operacion,primer_numero,segundo_numero):
		if operacion == 1:
			total=primer_numero + segundo_numero
		elif operacion == 2:
			total=primer_numero - segundo_numero		
		elif operacion == 3:
			total=primer_numero * segundo_numero		
		elif operacion == 4:
			total=float(primer_numero) / float(segundo_numero)			
		elif operacion == 5:
			exit()
		else :
			total=0			
		return total		

def calculadora():
	tipo_operacion=0
	total=0
	while True:
		tipo_operacion = int(input("1-SUMA\n2-RESTA\n3-MULTIPLICACIÓN\n4-DIVISIÓN\n5-SALIR\nIngresa el # de la operación que quieres realizar\n"))	
		if tipo_operacion >= 1 and tipo_operacion <= 4 :
			primer_numero=int(input("Ingresa el primer número:\n "))
			segundo_numero=int(input("Ingresa el segundo número:\n "))
			total = operacion(tipo_operacion,primer_numero,segundo_numero)
		elif tipo_operacion == 5:
			exit()
		else:
			print("Debes ingresar un número entre 1 y 5\n ")
		if tipo_operacion >= 1 and tipo_operacion <= 4 :
			print("EL TOTAL ES: {0}".format(total))
			


try:
	calculadora()
except SyntaxError as s:	
	print("Exception: {0} ".format(s)+"\nPor favor ingresa números las letras, variables o caracteres especiales como / * # $, NO estan permitidas :(\n ")
	calculadora()
except Exception as e:
	print("Exception: {0} ".format(e)+"\nPor favor ingresa números las letras y variables NO estan permitidas :(\n ")
	calculadora()
else:
	calculadora()
finally:
	print("Gracias por usar python calc version 0.1\n ")
	
		




