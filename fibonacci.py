
print("Hola este programa sirve para sacar numeros de la secuencia de Fibonacci")
print("¿cuantos numeros de la secuencia de Fibonacci quieres generar? ")

terminos = int(input())

resultado_anterior = 0
resultado = 1

for i in range(terminos):
    termino_fibonacci = resultado_anterior + resultado

    print(termino_fibonacci)

    resultado_anterior = resultado
    resultado = termino_fibonacci
