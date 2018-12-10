
import random
abc="abcdefghijklmoprstuvwyz"+"abcdefghijklmoprstuvwyz".upper()+"abcdefghijklmoprstuvwyz".lower()
num="12345678"
lista_abc=list(abc)
lista_num=list(num)
print("tengo una lista")
print(lista_num)
print(lista_abc)
print("deseo  saber que es ")

algo = "8"
if algo in lista_num:
	print(algo+" es un numero")
else:
	print(algo+" es una letra")



algo = "G"
linea="*"
if algo not in lista_num:
	print(algo+" es una letra")
else:
	print(algo+" es un numero")


if algo in lista_abc:
	print(algo+" => esta en la lista de letras")
elif algo in lista_num:
	print(algo+" => esta en la lista de numeros")
else:
	print(algo+" => no existe")



for elemento in lista_abc:
	linea+="*"
	print(linea+elemento)


#print("Linea")	
#print(linea)
#lista = list(linea)
#print("Tengo una lista de las lineas")
#print(lista)
#print("Tamanio")
#tam=len(lista)
#print(tam)
tam_linea=len(linea)
pos=1
l=tam_linea
#recorrer un array al reves
for elemento in lista_abc:
	print(linea[:l]+elemento)
	l=(pos)*(-1)	
	pos+=1
potencia=random.randint(0,random.randint(0,15211))	
for x in lista_num:
	print(x+" elevado a "+str(potencia)+" es = "+str(int(x)**potencia))


