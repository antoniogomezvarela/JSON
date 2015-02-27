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
	print ""
elif opcion == "4":
	print ""
elif opcion == "5":
	print ""
else:
	print "El número que has elegido no es una opción correcta"