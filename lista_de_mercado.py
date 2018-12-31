#encoding:utf-8

lista_mercado=list()

def main():
	while True:
		print "Selecciona una opción"
		print "1 - Agregar producto"
		print "2 - Eliminar producto"
		print "3 - Ver productos"
		print "4 - Salir"
		print ""
		opcion=int(input("Ingresa la opción: "))

		if opcion == 1:
			agregar_producto()
		elif  opcion == 2:
			eliminar_producto()	
		elif opcion == 3:
			ver_productos()
		elif opcion == 4:
			exit()
		else:
			print ""
			print "Debes ingresr una opción valida"			

def agregar_producto():
	print ""
	art=input("Ingresa el nombre del producto ")
	print " => "
	lista_mercado.append(art.capitalize())
	print "Producto agregado"

def eliminar_producto():
	print ""
	ver_productos()
	#eliminar por posicion
	art=input("Ingresa la posicion del producto que quieres eliminar ")
	print ""
	print "el producto a eliminar es :"
	print lista_mercado[art-1]
	del lista_mercado[art-1]
	
	#eliminar por elemento 
	#art=input("Ingresa el nombre del producto que quieres eliminar ")
	#lista_mercado.remove($art)
	#print "el producto a eliminar es :"
	#print lista_mercado[art]
	
	print "Producto eliminado"

def ver_productos():
	print ""
	print "-------------------lista de mercado-------------------------"
	i=0
	for articulo in lista_mercado:
		i+=1
		print str(i) + ":"+str(articulo)
	print "------------------------------------------------------------"
try:
	main()
except Exception as e:
	print e
	print ""
	main()
except ValueError as ve:
	print ve
	print ""
	main()
else:
	main()
finally:
	print "Gracias por usar mercapp"


	