import time

def juego_aventura():
    print(" BIENVENIDO A LA JUNGLA DE CÓDIGO ")
    print("Tu misión es encontrar el Templo del Python Perdido.")
    time.sleep(1)

    
    print("\nEstás frente a una bifurcación en la jungla.")
    print("¿Quieres ir por el sendero de la IZQUIERDA o la DERECHA?")
    
    eleccion_1 = input("> ").upper() 

    if eleccion_1 == "IZQUIERDA":
        
        print("\nCaminas hacia la izquierda y te topas con un río turbulento. ")
        print("Ves algo brillante en el fondo, pero hay pirañas.")
        
        print("Opciones: NADAR, CONSTRUIR una balsa o BORDEAR el río.")
        
        eleccion_2 = input("> ").upper()

        if eleccion_2 == "NADAR":
            print("\nMala idea Las pirañas tenían hambre BROO. ")
            print("GAME OVER.")
        
        elif eleccion_2 == "CONSTRUIR":
            
            print("\nConstruyes una balsa precaria. A mitad del río, empieza a desarmarse.")
            print("¿Intentas REPARAR la balsa o SALTAR a una roca cercana?")
            
            eleccion_3 = input("> ").upper()

            if eleccion_3 == "REPARAR":
                print("\nNo eres ingeniero... la balsa se hunde XDDDD. ")
                print("GAME OVER.")
            elif eleccion_3 == "SALTAR":
                
                print("\nSalto exitoso Llegas a la otra orilla y ves la entrada al templo.")
                print("La puerta tiene un acertijo: '¿Qué corre pero no tiene piernas?'")
                print("Opciones: TIEMPO, RIO o VIENTO") 

                eleccion_4 = input("> ").upper()
                
                if eleccion_4 == "RIO":
                    
                    print("\n¡Correcto! La puerta se abre. Entras a una sala oscura.")
                    print("¿Enciendes una ANTORCHA o usas tu VISION nocturna?")
                    
                    eleccion_5 = input("> ").upper()
                    
                    if eleccion_5 == "ANTORCHA":
                        
                        print("\nEl fuego ilumina la sala. Ves el Ídolo de Oro")
                        print("Pero está sobre un pedestal con trampa.")
                        print("¿Cambias el ídolo por una BOLSA de arena o lo AGARRAS rápido?")
                        
                        eleccion_6 = input("> ").upper()
                        
                        if eleccion_6 == "BOLSA":
                            print("\n¡Funciona! El mecanismo no se activa.")
                            print("¡HAS GANADO EL JUEGO! ")
                        elif eleccion_6 == "AGARRAS":
                            print("\n¡Trampa activada! Una roca gigante te aplasta. 🪨")
                            print("GAME OVER.")
                        else:
                            print("\nTe quedaste pensando y el templo colapsó. Fin.")
                    
                    elif eleccion_5 == "VISION":
                         print("\nNo tienes superpoderes. Tropiezas y caes en un pozo. ")
                         print("GAME OVER.")
                    else:
                        print("\nOpción no válida. Los murciélagos te atacan.")

                else:
                    print("\nRespuesta incorrecta. El suelo se abre bajo tus pies.")
                    print("GAME OVER.")
            else:
                print("\nResbalaste al intentar saltar.")
        
        elif eleccion_2 == "BORDEAR":
            print("\nCaminas por horas y te pierdes en la densidad de la selva.")
            print("Se hace de noche... GAME OVER.")
        
        else:
            print("\nNo hiciste nada y te picó un mosquito radioactivo. Fin.")

    elif eleccion_1 == "DERECHA":
        
        print("\nVas por la derecha y encuentras una cabaña abandonada. ")
        print("¿Quieres ENTRAR, RODEAR la casa o GRITAR 'Hola'?") 
        
        eleccion_2b = input("> ").upper()

        if eleccion_2b == "ENTRAR":
            print("\nEl piso está podrido y caes al sótano. Estás atrapado.")
            print("GAME OVER.")
        elif eleccion_2b == "RODEAR":
            print("\nDetrás de la casa encuentras un mapa, pero el viento se lo lleva.")
            print("Sin mapa, decides volver a casa.")
            print("Fin de la aventura.")
        elif eleccion_2b == "GRITAR":
            print("\nDespiertas a un oso que dormía dentro. Mala suerte.")
            print("GAME OVER.")
        else:
            print(f"\nNo entiendo qué es '{eleccion_2b}'. Un rayo cae sobre ti.")

    else:
        
        print("\nEsa no es una dirección válida. Te quedaste quieto y te aburriste.")
        print("Fin del juego.")


juego_aventura()