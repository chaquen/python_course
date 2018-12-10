#encoding:utf-8
try:
	verso=str(input("Ingresa una palabra para agregar a tu lista, recuerda solo dar enter cuando lo acabes, y de este modo registrarlo ;) \n"))
	print("Comenzando proceso de registro\n")	
	file=open('/home/chaquen/prestame_tus_versos_py','a')
	file.write(verso+'\n')
	file=open('/home/chaquen/prestame_tus_versos_py','r')
	print("Finalizando proceso de registro\n")	
except SyntaxError as err:
	print("Se ha registrado un error debe ingresar el texto una vez te aparezca el mensaje, vuelve a ejecutarme, mensaje de error \n  err => {0}".format(err))
except NameError as err:
	print("Se ha registrado un error debes ingresar el texto entre comillas simples o dobles, recuerda que es una prueba :P ,mensaje de error \n  err => {0}".format(err))
except IOError as err:	
	print('Ha ocurrido un error, mensaje de error \n  err => {0}'.format(err))
except TypeError as err: 	
	print('Ha ocurrido un error, mensaje de error \n  err => {0}'.format(err))
else :
	for verso in file.readlines():
		print(verso)
	file.close()			