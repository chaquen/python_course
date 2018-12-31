extenciones_lenguajes={".PHP":"Hypertext Preprocessor",".js":"Javascript",".py":"python",'.css':'Css','html':'HTML :)'}
print("Mi primer diccionario, recuerda el orden no es obligatorio")
print(extenciones_lenguajes)
print(extenciones_lenguajes[".PHP"])
for l in extenciones_lenguajes:
	print(l+" : "+extenciones_lenguajes[l])
dicci = dict( [ [".mp3","musica juepuerca"] , [".vida","lo que somos ;P "], [".chimba","Que lenguaje tan chimba  "] ] )
print dicci
print "Ahora voy a actualizarlo"
dicci["lunes"]=dict([["a","el valor de  el valor de a"],["c","el valor de c"]])
print dicci
print dicci["lunes"]["c"]
dicci.update({"martes":2,".mp3":"es un formato"})
print dicci
print "recorriendolos==="
dicci.update(extenciones_lenguajes)
for item in dicci:
	print item
for item in dicci.values():
	print item	
for item in dicci.items():
	print item
for item in dicci:
	print item 
	print dicci[item] 	