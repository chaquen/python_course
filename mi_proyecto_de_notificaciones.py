#encoding:utf:8
import json
import time
import os
file=json.loads(open('horarios.json').read())
#print(file)
#print(time.strftime("%H:%M")) #Formato de 24 horas
for h in file:
	if time.strftime("%H:%M") == h['hora']:
		os.system(h['comando']+' '+h['url_alerta'])
		print(h['mensaje'])