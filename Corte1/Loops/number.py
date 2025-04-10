import random
#librería para graficar
from matplotlib import pyplot as plt

#Estos son los números que se graficarán en el eje x
numbers_a = range(1, 10)

#Estos son los números que se graficarán en el eje y
#Se generan 9 números aleatorios entre 1 y 1000
numbers_b = [random.randint(1, 1000) for i in range (9)]

#Se grafican los números
plt.plot(numbers_a, numbers_b)

#Se añaden etiquetas a los ejes
plt.xlabel('Número')
plt.ylabel('Número aleatorio')
plt.show()