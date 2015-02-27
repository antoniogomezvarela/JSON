# -*- coding: utf-8 -*-
import json

f = open("nba.json")
documento =json.load(f)


print "1- Listar todos los equipos."
print "2- Pedir por teclado un equipo y que te muestre las estadisticas de ese equipo"
print "3- Listar los 10 equipos que más victorias tiene."
print "4- Listar los 10 equipos que mas derrotas tiene."
print "5- Listar los equipos segun su división."
opcion = raw_input("Opción: ")

if opcion == "1":
	for i in documento["standing"]:
		print i["first_name"],i["last_name"],", ID:",i["team_id"]

elif opcion == "2":
	equipo=raw_input("ID equipo: ")
	for i in documento["standing"]:
		if i["team_id"] == equipo:
			print "Nombre completo: ",i["first_name"],i["last_name"]
			print "Ganados: ",i["won"]
			print "Perdidos: ",i["lost"]
			print "Puntos a favor: ",i["points_for"]
			print "Puntos en contra: ",i["points_against"]
			print "Diferencia: ",i["point_differential"]
elif opcion == "3":
	equipos = []
	ganados = []
	
	for x in documento["standing"]:
		equipos.append(x["first_name"])
		ganados.append(x["won"])
	
	for i in range(10):
		victorias = max(ganados)
		contador = 0
		for x in ganados:
			if x == victorias:
				print equipos[contador],"",
				print ganados[contador]
				ganados[contador] = 0
				equipos[contador] = ""
				break
			else:
				contador += 1
	

elif opcion == "4":
	equipos = []
	ganados = []
	
	for x in documento["standing"]:
		equipos.append(x["first_name"])
		ganados.append(x["won"])
	
	for i in range(10):
		victorias = min(ganados)
		contador = 0
		for x in ganados:
			if x == victorias:
				print equipos[contador],"",
				print ganados[contador]
				ganados[contador] = 1000
				equipos[contador] = ""
				break
			else:
				contador += 1
elif opcion == "5":
	c = []
	e = []
	w = []
	for i in documento["standing"]:
		if i["division"] == "C":
			c.append(i["first_name"])
		elif i["division"] == "E":
			e.append(i["first_name"])
		elif i["division"] == "W":
			w.append(i["first_name"])
	print "División C"
	for i in c:
		print i
	print "División E"
	for i in e:
		print i
	print "División W"
	for i in w:
		print i
else:
	print "El número que has elegido no es una opción correcta"