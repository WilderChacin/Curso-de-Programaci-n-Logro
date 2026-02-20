import random 
import sys

def mostar_estado(jugador):
    print("\n" + "="*40)
    print(F"jugador: {jugador['nombre']} |  vida: {jugador['vida']}  |  energia: {jugador['energia']}")
    print(f"posicion: {jugador['posicion']}   |  Inventario: {len(jugador['Inventario'])} objetos ")
    print("="*40)
    
def mover_jugador(jugador,direccion):
    
    x,y = jugador['posicion']
    
    if direccion == 'N':
        y+=1
    elif direccion == 's':
        y-=1
    elif direccion == 'E':
        x+=1
    elif direccion == 'O':
        x-=1
    else:
        print("Direccion no valida")
        return False
    
    if -5 <= x <=5 and -5 <= y <=5:
        jugador['posicion'] = (x,y)
        return False 
    else: 
        print("\n Un muro invisible bloque ")
        return False 





def batalla(jugador):
    vida_enemigo = random.randint(30,50)

    while vida_enemigo > 0 and jugador['vida'] > 0:
        print(f"\Tu vida:{jugador['vida']} | Vida Enemigo:{vida_enemigo}")
        opcion = input("Que haras? (Atacar / Objeto / Huir):").strip().capitalize()

        if opcion == "Atacar":daño_jugador = random.randint(10, 25)
                              da







def usar_objeto(jugador):
    if not jugador['inventario']:
       print("No teneis un coño")
       return 
    print (f" Inventario actual: {','. join(jugador['inventario'])}")
    objeto_deseado = input("Escribe el nombre exacto del objeto a usar(o 'cancelar)")

    if objeto.lower() == 'cancelar':
        return

    objeto_encontrado = none

    for item in jugador ['inventario']:
        if item.lower() == objeto_deseado.lower():
            objeto_encontrado = item
            break
    if objeto_encontrado:
        if objeto_encontrado == "Pocion de vida":
            jugador ['vida']  += 40
            print("Bebes la pocion y recuperas 40 puntos de vida .")
            jugador['inventario'].remove(objeto_encontrado)
        elif objeto_encontrado == "comida enegetica":
            jugador['energia'] += 25
            print("Comes la harina blanca y recuperas 25 puntos de energia , pero ahora hueles el sonido")
            jugador['inventario'].remove(objeto_encontrado)
        elif objeto_encontrado == "Llave Maestra":
            print("La llave no se puede 'usar" . haz la opcion 'salir' cuando la tengas)

    else:
        print("No tienes ese objeto en tu inventario")
            




def encontar(jugador,llave_generada):
       probabilidad= random.random()

       if probabilidad < 0.30:
           print("\nLa sala esta vacia y en silencio")
           
        elif probabilidad < 0.60:
           
           opciones= ["Pocion de vida", "comida energetica"]  
           
        if not llave_generada:
           opciones.append("Llave maestra")
           hallazgo = random.choice(opciones)
       print(f"\n Encontraste algo en el suelo!!!: {hallazgo}")
       jugador['inventario'].append(hallazgo)

       if hallazgo == "Llave Maestra":
            print("ES LA LLAVE MAESTRA!!!! ahora debes intentar 'salir'")
            llave_generada = True
    else:
        
        batalla(jugador)

     return llave_generado


    

def main():
    print("="* 50)
    print("Bienvenido a Latinoamerica")
    print("="*50)

    try:
        nombre = input("ingresa tu nombre , valiente explorador;")
        if not nombre.strip():
               nombre="Explorar Anonimo"
    except (KeyboardInterrupt, EOFError):
        print("\n Saliendo  del juego......")
        sys.exit()






El 






































