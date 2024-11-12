import random

def comprobar_cueva():
    print("¿Que cueva quieres elegir?(1 o 2)")
    cueva_elegida = input()

    if int(cueva_elegida) > 2:
        print("No hay tantas cuevas")

    cueva_buena = random.randint(1, 2)

    if int(cueva_elegida) == cueva_buena:
        print("te ha dado su tesoro")
    else:
        print("te ha comido de un bocado")

def imprimir_introduccion():
    print("""
Te encuentras en un país lleno de dragones. Delante de ti,
puedes ver dos cuevas. En una de las cuevas, el dragon es amistoso
y compartira su tesoro contigo. El otro dragon es avaro y hanbriento,
y te comera en cuanto te vea. º
""")

def reino_del_dragon():
    imprimir_introduccion()

    jugar_otra_vez = ("si")

    while jugar_otra_vez == "si":
        comprobar_cueva()
        print(" Quieres segir jugando (si o no)")
        jugar_otra_vez = input()

reino_del_dragon()