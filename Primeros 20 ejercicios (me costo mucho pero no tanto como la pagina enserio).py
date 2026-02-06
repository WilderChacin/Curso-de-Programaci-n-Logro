
# def verificar_aprobacion(notas):
#     suma_total = 0
#     cantidad_notas = 0
    
    
#     for nota in notas:
#         suma_total += nota
#         cantidad_notas += 1
        
#     promedio = suma_total / cantidad_notas
    
    
#     if promedio > 60:
#         return f"Promedio {promedio:.2f}: Aprobado"
#     else:
#         return f"Promedio {promedio:.2f}: Reprobado"


# mis_notas = [20, 20, 10, 10,10]
# resultado = verificar_aprobacion(mis_notas)
# print("Ejercicio 1:", resultado)



####################################


# def filtrar_numeros_especiales():
#     numeros_encontrados = []
    
    
#     for numero in range(1, 101):
        
#         if numero % 2 == 0 and numero % 3 == 0:
#             numeros_encontrados.append(numero)
            
#     return numeros_encontrados


# lista_final = filtrar_numeros_especiales()
# print("Ejercicio 2:", lista_final)


######################################

# def iniciar_sesion():
#     contrasena_secreta = "192837465"
#     intentos = 0
#     max_intentos = 3
#     print("\n--- Ejercicio 3: Login ---")

    
#     while intentos < max_intentos:
        
#         entrada = input(f"Intento {intentos + 1}/{max_intentos}. Ingrese clave (es 192837465): ")
        
    
#         if entrada == contrasena_secreta:
#             print("¡Acceso Concedido!")
#             break 
#         else:
#             print("Clave incorrecta.")
#             intentos += 1
    
#     if intentos == max_intentos:
#         print("¡Usuario Bloqueado!")

# iniciar_sesion()
 

################################


# def convertir_km_a_millas(lista_distancias):
#     resultados = []
    
    
#     for km in lista_distancias:
        
#         if km > 0:
#             millas = km * 0.621371
#             resultados.append(f"{km}km = {millas:.2f}mi")
#         else:
#             resultados.append(f"{km}km = Error (No válido)")
            
#     return resultados

# viajes = [100, -5, 50, 0]
# print("Ejercicio 4:", convertir_km_a_millas(viajes))



###################################





# def contar_caracter(texto, letra_objetivo):
#     contador = 0
    
    
#     for letra in texto:
#         if letra == letra_objetivo:
#             contador += 1
            
    
#     if contador > 0:
#         return f"La letra '{letra_objetivo}' aparece {contador} veces."
#     else:
#         return f"Error: La letra '{letra_objetivo}' no existe en el texto."


# mensaje = "programacion en python"
# print("Ejercicio 5:", contar_caracter(mensaje, "o"))




######################################



# def imprimir_sin_multiplos_cuatro():
#     numeros_procesados = []
    
    
#     for i in range(1, 21):
        
#         if i % 4 == 0:
#             continue 
#         numeros_procesados.append(i)
        
#     return numeros_procesados


# print("Ejercicio 6:", imprimir_sin_multiplos_cuatro())





###############################################



# def procesar_compra(orden, inventario):
#     reporte = []
    
    
#     for item, cantidad_pedida in orden:
        
#         if item in inventario and inventario[item] >= cantidad_pedida:
#             inventario[item] -= cantidad_pedida
#             reporte.append(f"{item}: Enviado (Quedan {inventario[item]})")
#         else:
#             reporte.append(f"{item}: Stock Insuficiente o No Existe")
            
#     return reporte


# stock_almacen = {"Laptop": 10, "Mouse": 5, "Teclado": 0}
# mi_pedido = [("Laptop", 2), ("Mouse", 10), ("Monitor", 1)] 
# print("Ejercicio 7:", procesar_compra(mi_pedido, stock_almacen))


#########################################



# def buscar_primos(limite):
#     primos = []
    
    
#     for num in range(2, limite + 1):
#         es_primo = True
        
        
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 es_primo = False
#                 break 
        
        
#         if es_primo:
#             primos.append(num)
            
#     return primos


# print("Ejercicio 8:", buscar_primos(30))



##########################################


# def aplicar_impuestos(lista_precios):
#     precios_finales = []
    
    
#     for precio in lista_precios:
        
#         if precio > 100:
            
#             nuevo_precio = precio * 1.16
#         else:
            
#             nuevo_precio = precio * 1.08
#         precios_finales.append(round(nuevo_precio, 2))
        
#     return precios_finales

# carrito = [50, 200, 100, 10]
# print("Ejercicio 9:", aplicar_impuestos(carrito))




#######################################################





# def simular_cajero():
#     saldo = 500
#     print("\n-- Ejercicio 10: Cajero ----------")
    
    
#     while True:
#         opcion = input("1. Ver | 2. Retirar ($100) | 3. Salir: ")
        
        
#         if opcion == '1':
#             print(f"Saldo actual: ${saldo}")
#         elif opcion == '2':
#             if saldo >= 100:
#                 saldo -= 100
#                 print("Retiraste $100.")
#             else:
#                 print("Saldo insuficiente.")
#         elif opcion == '3':
#             print("Sesión cerrada.")
#             break 
#         else:
#             print("Opción no válida.")


# simular_cajero() 


######################################################



# def limpiar_base_datos(lista_nombres):
#     nombres_validos = []
    
    
#     for nombre in lista_nombres:
#         nombre_limpio = nombre.strip() 
        
        
#         if nombre_limpio.isalpha(): 
#             nombres_validos.append(nombre_limpio.capitalize())
            
#     return nombres_validos

# usuarios_raw = ["  ana ", "pedro123", "LUIS", "mari@"]
# print("Ejercicio 11:", limpiar_base_datos(usuarios_raw))



###################################################



# def detector_palindromos(lista_palabras):
#     resultado = []
    
    
#     for palabra in lista_palabras:
#         p_min = palabra.lower()
        
        
#         if p_min == p_min[::-1] and len(p_min) > 5:
#             resultado.append(palabra)
            
#     return resultado

# textos = ["reconocer", "radar", "oso", "sometemos", "casa"]
# print("Ejercicio 12:", detector_palindromos(textos))


##################################################



# def calcular_factorial(numero):
    
#     while numero < 0:
#         print("Error: El número debe ser positivo.")
#         return None 

#     resultado = 1
    
#     for i in range(1, numero + 1):
#         resultado *= i
        
    
#     if numero == 0:
#         return 1
        
#     return resultado

# print("Ejercicio 13:", calcular_factorial(5))



##########################################################



# def calcular_pagos(empleados):
#     nomina = {}
#     tarifa = 20 
    
    
#     for emp in empleados:
#         nombre = emp["nombre"]
#         horas = emp["horas"]
        
        
#         if horas > 40:
#             horas_normales = 40
#             horas_extra = horas - 40
#             pago = (horas_normales * tarifa) + (horas_extra * tarifa * 2)
#         else:
#             pago = horas * tarifa
            
#         nomina[nombre] = pago
        
#     return nomina

# staff = [{"nombre": "Juan", "horas": 35}, {"nombre": "Maria", "horas": 45}]
# print("Ejercicio 14:", calcular_pagos(staff))



####################################################



# def filtrar_emails(lista_correos):
#     correos_validos = []
    
    
#     for correo in lista_correos:
        
#         if "@" in correo and correo.endswith(".com") and " " not in correo:
#             correos_validos.append(correo)
            
#     return correos_validos

# db_emails = ["juan@gmail.com", "pedro gmail.com", "ana@yahoo.es", "luis@site.com"]
# print("Ejercicio 15:", filtrar_emails(db_emails))



##########################################################



# import random

# def jugar_adivinanza():
#     secreto = random.randint(1, 20)
#     vidas = 5
#     print("\n--- Ejercicio 16: Adivina el número (1-20) ---")
    
    
#     while vidas > 0:
#         try:
#             intento = int(input(f"Tienes {vidas} vidas. Tu número: "))
#         except ValueError:
#             print("¡Ingresa un número válido!")
#             continue

        
#         if intento == secreto:
#             print(f"¡Ganaste! Era el {secreto}")
#             break
#         elif intento < secreto:
#             print("El secreto es MÁS ALTO.")
#         else:
#             print("El secreto es MÁS BAJO.")
            
#         vidas -= 1
        
#     if vidas == 0:
#         print(f"Game Over. El número era {secreto}")


#  jugar_adivinanza() 


###############################################################


# def facturar_productos(lista_productos):
    
#     total_factura = 0
    
    
#     for nombre, categoria, precio in lista_productos:
#         descuento = 0
        
        
#         if categoria == "A":
#             descuento = 0.30
#         elif categoria == "B":
#             descuento = 0.20
#         elif categoria == "C":
#             descuento = 0.10
        
#         precio_final = precio * (1 - descuento)
#         total_factura += precio_final
#         print(f"Producto: {nombre} | Final: ${precio_final:.2f}")
        
#     return total_factura

# carrito_pro = [("Tv", "A", 1000), ("Radio", "B", 100), ("Cable", "D", 20)]
# print("Ejercicio 17 Total:", facturar_productos(carrito_pro))


###################################################################



# def extraer_palabras_largas(parrafo):
    
#     lista_palabras = parrafo.split()
#     seleccionadas = []
    
    
#     for palabra in lista_palabras:
        
#         limpia = palabra.strip(".,;")
        
        
#         if len(limpia) > 7:
#             seleccionadas.append(limpia)
            
#     return seleccionadas

# texto_lorem = "La programación es increiblemente divertida y fascinante."
# print("Ejercicio 18:", extraer_palabras_largas(texto_lorem))



##################################################################



# def convertir_binario(cadena_binaria):
#     decimal = 0
#     exponente = 0
    
    
#     cadena_invertida = cadena_binaria[::-1]
    
    
#     for digito in cadena_invertida:
        
#         if digito == '1':
#             decimal += 2 ** exponente
#         elif digito == '0':
#             pass 
#         else:
#             return "Error: No es un número binario"
            
#         exponente += 1
        
#     return decimal


# print("Ejercicio 19 (101):", convertir_binario("101")) 
# print("Ejercicio 19 (1111):", convertir_binario("1111")) 


#################################################################



# def validar_permiso(solicitudes, base_datos_roles):
#     log_acceso = []
    
    
#     for usuario, accion in solicitudes:
        
        
#         if usuario in base_datos_roles:
#             rol = base_datos_roles[usuario]
            
#             if rol == "Admin":
#                 log_acceso.append(f"{usuario}: Acceso concedido a {accion}")
#             elif rol == "Editor":
#                 if accion == "borrar":
#                     log_acceso.append(f"{usuario}: DENEGADO (Editor no puede borrar)")
#                 else:
#                     log_acceso.append(f"{usuario}: Acceso concedido a {accion}")
#             else:
#                 log_acceso.append(f"{usuario}: DENEGADO (Rol bajo)")
#         else:
#             log_acceso.append(f"{usuario}: Usuario desconocido")
            
#     return log_acceso

# usuarios_db = {"Neo": "Admin", "Trinity": "Editor"}
# intentos = [("Neo", "borrar"), ("Trinity", "borrar"), ("Trinity", "editar")]
# print("Ejercicio 20 Por fin:", validar_permiso(intentos, usuarios_db))






















































    
