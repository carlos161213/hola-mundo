import random

print("hola")
print("¿como te llamas?")

su_nombre = input()
print(f"hola {su_nombre} intenta adivinar un numero del 1 al 20")

numero_que_tienes_que_adivinar = random.randint(1,20)
numero_elegido = int(input())

print(f" {numero_elegido}")

if numero_elegido > 20:
    print("Debes introducir un numero entre 1 y 20")
else:
    if numero_que_tienes_que_adivinar == numero_elegido:
        print("¡HAS GANADO!")
    else:
        print("HAS PERDIDO")
        print(f"el numero era:{numero_que_tienes_que_adivinar}")
