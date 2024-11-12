print("Hola este programa sir ve para sabre como multiplican los rusos")
print("Que quieres multiplicar")
print("Pon primero un multiplicador y luego el otro multiplicador")
primer_multiplicador = int (input())
print("Ahora el divisor")
segundo_multiplicador = int (input())
doble = segundo_multiplicador

mitades = [primer_multiplicador]
dobles = [segundo_multiplicador]
mitad, resto = divmod(primer_multiplicador, 2)

while mitad > 0:
    mitades.append(mitad)
    mitad, resto = divmod(mitad, 2)

    doble = doble * 2
    dobles.append(doble)

total = 0
for i, mitad in enumerate(mitades) :
    if mitad % 2 > 0:
       total = dobles[i] + total

print(total)