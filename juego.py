import time

from personajes import Personaje

print("¡Bienvenido a Gran Fantasía!")

#personaje_jugador = Personaje(input("Por favor indique nombre de su personaje:\n"))

personaje_jugador = Personaje("max") #
personaje_orco = Personaje("Orco")

print(personaje_jugador.estado)

while True:
    print("")
    print("¡Oh no!, ¡Ha aparecido un Orco!")
    print("")

    print(personaje_jugador.comparar_niveles(personaje_orco))

    print("")
    print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
    print("Si pierdes, perdedrás 30 puntos de experiencia y el orco ganará 50.")

    print("")
    print("¿Qué deseas hacer?")
    print("1. Atacar")
    print("2. Huir")
    
    opcion = input("")
    print("")
    if opcion == "1":
        print(personaje_jugador.Atacar(personaje_orco))

    elif opcion == "2":
        print(personaje_jugador.Huir(personaje_orco))
        break
    
    print(personaje_jugador.estado)
    print(personaje_orco.estado)
    time.sleep(5)