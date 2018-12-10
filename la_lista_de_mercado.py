#encoding: utf-8
#Este programa tiene como fin registrar los productos comprados
print('Ingresa la lista de tus productos y luego la cantidad, al final se te indicara el resultado total\n para salir simplemente escribe "SALIR" \n')
file=open('/home/chaquen/lista.txt','w')
texto_producto="ENTRAR"
total=0
while(texto_producto.upper()!="SALIR"):
	texto_producto=str(input('ingresa productos '))
	if texto_producto.upper() == 'SALIR':
		break;
	texto_precio=str(input('ingresa precios '))
	file.write(texto_producto+" = "+texto_precio+'\n')
	total+=int(texto_precio)
file.write('El total es :'+str(total))
file.close()

file=open('/home/chaquen/lista.txt','r')	

for linea in file.readlines():
	l=linea
	print(l)

	


