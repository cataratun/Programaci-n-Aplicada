import time

# Este programa calcula los números primos entre 0 y 30
# y mide el tiempo que tarda en ejecutarse.
inicio = time.time()

# Se inicializa la variable que cuenta los números primos
for i in range(0,31):
    contador = 0
    for n in range(1, i+1):
        residuo = i%n
        if residuo == 0:
            contador = contador + 1

    if contador == 2:
        print(f'{i} es un primo')

# Se calcula el tiempo de ejecución
# y se imprime en milisegundos.
fin = time.time()
print("t = ", (fin - inicio)*1000)