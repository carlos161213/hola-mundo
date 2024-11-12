import random

print("hola")
print("¿como te llamas?")

su_nombre = input()

numero_que_tienes_que_adivinar = random.randint(1, 20)
print(f"hola {su_nombre} intenta adivinar un numero del 1 al 20")
oportunidades = 5

for i in range(oportunidades):
    numero_elegido = int(input())

    print(f" {numero_elegido}")
    if numero_elegido > 20:
        print("Debes introducir un numero entre 1 y 20")
    else:
        if numero_que_tienes_que_adivinar == numero_elegido:
            print("¡HAS GANADO!")
            exit(0)
        else:
            if numero_elegido > numero_que_tienes_que_adivinar:
                print("el numero es menor")
            else:
                print("el numero es mayor")

            print(f"vuelvelo a intentar no es correcto:numero de intento {i + 1} de {oportunidades}")

print("HAS PERDIDO")
print(f"el numero era:{numero_que_tienes_que_adivinar}")
