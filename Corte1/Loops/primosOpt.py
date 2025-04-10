# 1) Imprimir los números primos existentes entre 0 y 30
tope_rango=30
n = 0
primo = True


while (n < tope_rango):
    
    # Se evalua si el número es primo o no
    for div in range(2, n):
        
        # Se evalua si el número es divisible por otro número
        # Si es divisible, no es primo
        if (n % div == 0):
            primo = False
    
    # Si no es divisible por ningún número, es primo
    # Se imprime el número primo
    if (primo):
        print(n)
    else:
        primo = True
    n += 1


# 2) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
n = 0
primo = True
ciclos_sin_break = 0

# Se evalua si el número es primo o no
while (n < tope_rango):
    # Se evalua si el número es divisible por otro número
    # Si es divisible, no es primo
    for div in range(2, n):
        ciclos_sin_break += 1
        # Si el número es divisible por otro número, no es primo
        if (n % div == 0):
            primo = False
    #Si es primo se imprime el número
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break)) #378


# 3) ¿Cuántos ciclos se ejecutan para determinar si un número es primo?
ciclos_con_break = 0
n = 0

# Se evalua si el número es primo o no
primo = True
while (n < tope_rango):
    # Se evalua si el número es divisible por otro número
    for div in range(2, n):
        ciclos_con_break += 1
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_con_break)) #134
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')


# 4) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
tope_rango=100
ciclos_sin_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_sin_break += 1
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break)) #4753


#5) ¿Cuántos ciclos se ejecutan para determinar si un número es primo?
ciclos_con_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_con_break += 1
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_con_break)) # 1132
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')
