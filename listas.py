#encoding: utf-8
#La linea 1 es importante para trabja con la codificación
import os, sys
print('Las representa un conjunto de  objetos, en python pueen cambiar de tamaño y guardar cualquier tipo de dato')
lista=[1,2,3,4,'5']
print(lista)
#aqui agregamos un elemento mas lista
print('aqui agregamos elementos un string')
lista += [6,7,8,9,'10']
print(lista)
#aqui agregamos un elemento mas lista
print('aqui agregamos una lista ')
lista.append([11,12])
print (lista)
#aqui agregamos un elemento mas lista
print('aqui agregamos un string')
lista.append('bronca')
print(lista)
print('aqui agregamos varios elementos con metodo extend')
lista.extend([13,14,15])
print(lista)
print('aqui removemos un string')
lista.remove('bronca')
print(lista)
print('aqui removemos una lista')
lista.remove([11,12])
print(lista)
lista=list([1,2,2,"ñiño","ñiño"])
print("se repite la palabra niño en la lista ",lista.count("ñiño"),"veces")
print(lista[3])
for x in lista:
	print x

