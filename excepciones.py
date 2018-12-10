#encoding:utf-8
try:
	numero_uno=int(input("ingresa el primer numero "))
	numero_dos=int(input("ingresa el segundo numero "))
except NameError:
	print("Debes ingresa un valor numerico")
except ValueError:
	print("Debes ingresa un valor numerico")	
else:
	total=numero_uno + numero_dos
	print("el total de la suma de  : "+str(numero_uno)+" + "+str(numero_dos)+" es = a "+str(total))