
vocales="a e i o u"
lista= vocales.split()
print(lista) 
print("eliminar elemento de lista")
del lista[3]
print(lista) 
print("eliminar variable, ver error, indica que variable ya no esta definida")
del vocales
print(vocales) 