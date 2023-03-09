print("¡Valor del estacionamiento dependiendo el dia, minutos y horas estacionado!")

dia = input("\nIngrese el dia de la semana en el que adquirio el servicio de estacionamiento (Lunes, Martes, Miercoles, Jueves, Viernes, Sabado O Domingo): ")
tiempo = input("Ingresa la cantidad de horas y minutos de estacionamiento (HH:MM): ")

horas, minutos = tiempo.split(":")
tiempo_minutos = int(horas) * 60 + int(minutos)

if dia in ["lunes", "martes", "miercoles"]:
    precio_por_hora = 2.00
elif dia in ["jueves", "viernes"]:
    precio_por_hora = 2.50
elif dia in ["sabado", "domingo"]:
    precio_por_hora = 3.00
else:
    print("¡ERROR! El dia la semana es incorrecto o esta mal escrito")
    exit()
    
precio_total = precio_por_hora * (tiempo_minutos // 60 + (1 if tiempo_minutos % 60 > 5 else 0))

print("El precio total del estacionamiento es: $" + str(precio_total))