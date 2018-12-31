tuplas=(1,2,dict( [ ["a", [0,1,2] ] , ["b", ["abc","def","hij"] ]  ]),4,["prueba","de","tuplas"])
print tuplas
print tuplas[2]
print "las tuplas son inmutables por ende no se puede agregar o eliminar errores"
try:
	del tuplas[2] 
except Exception as e:
	print e

try:
	tuplas[2]="ab"
except Exception as e:
	print e

print "Pero se puede elementos mutables como listas o diccionarios"
tuplas[2].update({"abcdefghij":"abecedario","a":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]})
print tuplas
print "==========="
for tupla in tuplas:
	print tupla