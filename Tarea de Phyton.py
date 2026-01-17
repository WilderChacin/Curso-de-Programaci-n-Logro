###base= int(input("cual es la base del rectangulo?:"))

#altura= int(input("cual es la altura del rectangulo"))

#area= base * altura

#print(f"El area del rectangulo es: {area}")###

##############

#c= int(input ("Cuantos grados celcius son?:"))

#Fahrenheit= f = (c* 9/5) + 32

#print(f"El total en grados Fahrenheit son {Fahrenheit}")

##############

#nombre= input("ingresa tu nombre:")

#apellido= input("ingresa tu apellido:")

#Nombre_completo = nombre + "" + apellido
#print("Hola " + Nombre_completo)

##############

#numero= int(input("Ingrese un numero entero: "))

#if numero % 2 == 0:
    #print("El numero es PAR ")
#else:
    #print("El numero es IMPAR ")

###############

#Edad= int(input("Cuantos años tienes?: "))

#if Edad >= 18:
    #print("Excelente puedes votar")
#else:
    #print("Aun eres menor de edad no puedes votar")

###############

#numero1= float(input("Ingrese el primer numero: "))

#numero2= float(input("Ingrese el segundo numero: "))

#if numero1 > numero2:
    #print(f"{numero1} Es mayor que {numero2} ")

#elif numero1 < numero2:
    #print(f"{numero1} Es menor que {numero2} ")
#else:
    #print("Ambos numeros son iguales")

################

#numero= int(input("Ingrese un numero: "))

#if numero >= 10 and numero <= 20:
    #print("El numero se encuentra entre 10 y 20")
#else:
    #print("El numero no se encuentra entre 10 y 20 ESTA FUERA DE RANGO XD ")

################

#Super_Contraseña= "Logro1928"

#intento= input("Ingrese su contraseña")

#if intento== Super_Contraseña:
    #print("Acceso Permitido")

#else:
    #print("Acceso Denegado")

##############

#precio= float(input("Ingresa el precio del producto: "))

#if precio > 100:
    #descuento= precio * 0.15

    #precio_final = precio - descuento
    #print(f"Descuento aplicado al cliente, nuevo precio: ${precio_final}")
#else:
    #print(f"No aplica el descuento. Precio final: ${precio}")

###############

#n = float(input("Ingresa un numero: "))

#if n > 0:
    #print("Es positivo (+)")

#elif n < 0:
    #print("Es negativo (-)")

#else:
    #print("El numero es igual a cero (0)")

###############

#No se logro hacer
##ano= int(input("Ingrese el año: "))

#if ( ano % 4 == 0 and ano % 100 = 0 )
    #or ( ano % 400 == 0 ):
#print("Es un año biciesto ")

#else:
#print("No es biciesto")

#################################


#nota= int(input("Ingresa tu nota (0-100): "))

#if nota >= 90:
   # print("Tu calificacion es: A ")

#elif nota >= 80:
    #print("Tu calificacion es: B ")

#elif nota >= 70:
    #print("Tu calificacion es: C ")

#elif nota >= 60:
    #print("Tu calificacion es: D ")

#else:
    #print("Tu calificacion es: F ")

#################


#letra= input("ingresa una letra: "). lower()

#if len (letra) == 1 and letra.isalpha():
    #if letra in "aeiou":
        #print("Es una vocal")
    #else:
        #print("Es una consonante")
#else:
    #print("Por favor, ingresa solo una letra valida.")


###################


#print("1. Saludar")
#print("2. Despedir")
#print("3. Salir")

#opcion = int(input("Elige una opcion (1-3): "))

#if opcion == 1: 
    #print("Hola bro")

#elif opcion == 2:
    #print("Nos vemos amigo")

#elif opcion == 3:
    #print("Saliendo de la Matrix")

#else:
    #print("Opcion no valida.")


#######################


#n1 = int(input('Numero 1:'))
#n2 = int(input('Numero 2:'))
#n3 = int(input('Numero 3:'))

#if n1 >= n2 and n1 >= n3:
   # mayor= n1

#elif n2 >= n1 and n2 >= n3:
    #mayor= n2

#else:
    #mayor = n3

#print(f" El mayor numero es: {mayor}")


#############



peso= float(input("Peso (Kg): "))
altura= float(input ("Altura (m): "))

imc = peso / (altura **2)

print(f" Tu imc es: {imc:.2f}")

if imc < 18.5:
    print("Clasificacion: Bajo peso")

elif 18.5 <= imc < 25:
    print("Clasificacion: Peso normal")

elif 25 <= imc < 30:
    print("Clasificacion: Sobrepeso")

else:
    print("Clasificacion: Obesidad")













