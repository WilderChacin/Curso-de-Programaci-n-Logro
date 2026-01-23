
Lista_Principal= [["Cianuro",2],["Iman",5],["Saco de boxeo",34],["Helicoptero Apache",1000]]

Cesta_de_compra= []



def agregar(articulo):
    Cesta_de_compra.append(articulo)
    print(" \n[Articulo agregado exitosamente]\n")
    return


# def eliminar(articulo):
#     for x in enumerate(Cesta_de_compra):
#     Cesta_de_compra.pop

def calcular():
   resultado=0
   for articulo in Cesta_de_compra:
       resultado=resultado+articulo[1]
   return resultado

def renunciar():
    pass


print("CARRITO DE AMAZON")

while True: 
    Opcion1= int(input("1. MOSTRAR \n 2. CALCULAR \n 3. ELIMINAR \n 4. MOSTRAR CESTA \n 5. RENUNCIAR \n Selecciona una de las opciones numericas presentadas: "))

    if Opcion1 == 1:
        while True:
            opcion2= int(input(f""" 
                               Lista de articulos en venta: \n 
                               1. {Lista_Principal[0][0]} Precio: {Lista_Principal[0][1]}$ \n
                               2. {Lista_Principal[1][0]} Precio: {Lista_Principal[1][1]}$ \n
                               3. {Lista_Principal[2][0]} Precio: {Lista_Principal[2][1]}$ \n
                               4. {Lista_Principal[3][0]} Precio: {Lista_Principal[3][1]}$ \n
                               5. Regresar \n
                               Selecione el articulo a agregar a su Cesta de compra :) :"""))

            
            
            

            if opcion2 == 1:
                agregar(Lista_Principal[0])

            elif opcion2 == 2:
                agregar(Lista_Principal[1])

            elif opcion2 == 3:
                agregar(Lista_Principal[2])

            elif opcion2 == 4:
                agregar(Lista_Principal[3])

            elif opcion2 == 5:
                break
    # elif Opcion1 == 3:
    #     posicion=[]
    #     print(" Articulos en la cesta: \n")
    #     for x in enumerate(Cesta_de_compra):
    #         print(x)
    #         posicion.append(x[0])
        
    #     opcion3=input("Que articulo desea eliminar brother?: ")
    #     if opcion3==
    
    elif Opcion1 == 4:
        print(Cesta_de_compra)

    elif Opcion1 == 5:
        break

    elif Opcion1 == 2:
        precio_toal=calcular()
        print(f"El precio total de los articulos es:  {precio_toal}")





    
