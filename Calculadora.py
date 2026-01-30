import math

def mostrar_menu(): 

    print("===== Calculadora Cientifica =====")
    print(" 1. Suma(+)       2. Resta(-)        3. Multiplicacion(*) ")
    print(" 4. Division()    5. Potencia ()     6. Raiz() ")
    print(" 7. Seno          8. Coseno          9. Logaritmo ")
    print("10. Salir")

def Calculadora():
    while True:
        mostrar_menu()
        opcion = input("Elige una Opcion entre (1-10):")


        if opcion == 10:
            print("Nos vemos")
            break




        elif opcion == 1:
          Primer_numero = print(input("Inserta el primer numero:"))
          Segundo_numero = print(input("Inserte el Segundo numero:"))

        



