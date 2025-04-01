while True:

    value = int(input("Ingresa un valor entero positivo: "))
    print("Valor: ", value)
    a = isinstance(value, int)
    if a == True and value > 0:
        fact = 1
        for i in range(1, value + 1):
            fact = fact * i
        print(f'El factorial de {value} es: ', fact)
    else:
        print("Por favor, ingresa un número entero positivo")