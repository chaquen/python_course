#encoding: utf-8
#ciclos while
frutas=9
lista_frutas=['pera','manzana','mango','banano','lulo','freijoa','naranja','pera','breva','uva']
print("while")
while frutas >= 0:
	print('Me estoy comiento una '+lista_frutas[frutas]+" que esta en la posicion "+str(frutas)+" en un while")
	#se hace la resta de 1 en 1
	frutas -= 1
print('me quede sin frutas :(')
print("while ||")
indice = 0
if indice <= len(lista_frutas):
	print("el tamaño de la canasta es  "+str(len(lista_frutas))+" unidades") 
while indice < len(lista_frutas):
	print('Me estoy comiento una '+lista_frutas[indice]+" que esta en la posicion "+str(indice)+"  en un while")
	indice += 1
print('me quede sin frutas ;(')
print("for")
for fruta in lista_frutas:
	print("Me estoy comiendo la fruta "+fruta+" en un for")
print("Ya me quede sin frutas :(")
verdura="Zanahoria"
print("se le agrega una zanahoria, una papaya y una guanabana ")

lista_frutas.append("papaya")
lista_frutas.append(verdura)
lista_frutas.append("guanabana")
print("BREAK")
for fruta in lista_frutas:
	if verdura == fruta:
		print("esto es una "+fruta+" me largo de aqui, con un break")
		break
	print("Me estoy comiendo la fruta "+fruta)
print("Ya me quede sin frutas :(")
for fruta in lista_frutas:
	if verdura == fruta:
		print("esto es una "+fruta+" y no me la comeré, pero seguire disfutando con un continue :P")
		continue
	print("Me estoy comiendo la fruta "+fruta)
print("Ya me quede sin frutas :(")
lista_verduras=["arbega",'habichuela','ahuyama']
lista_frutas.extend(lista_verduras)
lista_frutas.append("mandarina")
lista_frutas.append("melón")
for fruta in lista_frutas:
	if fruta in lista_verduras:
		print("esto es una "+fruta+" y no me la comeré, pero seguire disfutando con un continue :P")
		continue
	print("Me estoy comiendo la fruta "+fruta)
print("quede satisfecho! :)")
