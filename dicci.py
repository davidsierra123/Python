diccionario={
    "horario":"mañana",
    "Jornada laboral":"07:00 A.M" "06:00 P.M" 
}

#Te regresa las claves del diccionario seleccionado
'''
x = diccionario.keys()
print(x)
'''

#Ingresar un nuevo dato al diccionario
'''
diccionario["Horas extras"] = "6:30 P.M " "10:30 P.M"
print (diccinario)
'''

#Te retorna la longitud osea cuantas claves hay en numeros
'''
print (len(diccionario))
'''
#Te retorna que tipo de vaina estas utilizando (variable, constante, cadena, listas, tuplas o diccionario)
'''
print(type(diccionario))
'''

#Te retorna el contenido de la clave
'''
print(diccionario["horario"])
'''


# Es como un for pero solo recorre las claves
if "Jornada laboral" in diccionario:
    print("Si existe")
else:
    print("No existe")
    