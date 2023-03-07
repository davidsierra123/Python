'''
x = 4
x = "Wendy"
print (x)
'''
#Castear
'''
x = float(4)
print (x)
'''

#Type
'''
x = 4
y = "Wendy"
print(type(x))
print(type(y))
'''
#Mostrar
'''
print ("Por favor escribe tu nombre")
nombre = input ()
print("Su nombre es: " + nombre)
'''

#Suma
'''
print ("Por favor digite el primer numero")
n1 = int (input())
print ("Por favor digite el segundo numero")
n2 =  int(input())
ñe = n1 % n2 
print ("El porcentaje es" , ñe)
'''

#Identacion
'''
numero = int(input("Favor digitae un numero "))
if numero > 0:
    print(f"el valor del numero es {numero} positivo")
elif numero < 0:
    print(f"el valor del numero es {numero} negativo")
else:
    print(f"el valor del numero es {numero} cero")
'''



'''
a = """Un texto es una composición de signos codificados
en un sistema de escritura que forma una unidad de sentido.
También es una composición de caracteres imprimibles generados por
un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona,
sí puede ser descifrado por su destinatario original"""
print(a)
'''


"""
b = '''Un texto es una composición de signos codificados
en un sistema de escritura que forma una unidad de sentido.
También es una composición de caracteres imprimibles generados por
un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona,
sí puede ser descifrado por su destinatario original '''
print (b)
    """


'''
for x in range (6):
    print (x)
'''


'''
for x in "banana":
    print(x)
'''


'''
for x in range (2,6):
    print(x)
'''

    

'''for x in range (2,30,3):
    print(x)
    print("si")
    '''
    


'''
for x in range (6):
    if x == 3:
        print(x)
        break
    else:
        print("Termine")
'''

'''
i = 1
while i<6:
    print(i)
    if i == 3:
        break
    i += 1
'''

'''
i = 1
while i < 6:
    i += 1
    if i == 3:
        continue
    print (i)
'''


'''
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i no es menor a 6")
'''

#recorrer breve 
'''
txt = "si sabemos mas"
print ("mañana" in txt)
'''

#recorrer breve con condiciones
'''
txt = "si sabemos mas"
if "mñn" in txt:
    print("Si esta")
else:
    print("No existe")
'''

#Te muestra la posicion 2 y 5
'''
b = "Hello, World"
print(b[2:5])
'''

#Te muestra la posicion desde el 2 hasta el final
'''
b = "Hello, World"
print(b[2:])
'''

#Te muestra la posicion antes del 2
'''
b = "Hello, World"
print(b[:2])
'''

#Muestra valor a en Mayuscula
'''
a = "Hello, World"
print(a.upper())
'''
#Muestra Hello World
'''
a = "Hello, World"
print (a.strip())
'''

#Retorna esto ['Hello', ' World']
'''
a = "Hello, World"
print (a.split(","))
'''
#Muestra valor a en Minuscula
'''
a = "Hello World"
print(a.lower())
'''

#Cambia o reemplazar en este caso cambias H por J
'''
a = "Hello World"
print(a.replace("H", "J"))
'''

# Te mostrara el txt y ademas debes castear para que te muestre tu edad osea: str(age-edad)
'''
age = 18
txt = "My nombre es David " + str (age)
print (txt)
'''
