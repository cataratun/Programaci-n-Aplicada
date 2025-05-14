def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

def potencia(a, b):
    return a ** b

def calculadora():
    print("Operaciones disponibles en CalcuPython:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Potencia (^)")

    opcion = input("Elige una operación: ")

    try:
        a = float(input("Ingresa 'a': "))
        b = float(input("Ingresa 'b': "))
    except ValueError:
        print("Error: entrada inválida.")
    else:
        match opcion:
            case "1":
                print(f"Resultado: {sumar(a, b)}")
            case "2":
                print(f"Resultado: {restar(a, b)}")
            case "3":
                print(f"Resultado: {multiplicar(a, b)}")
            case "4":
                print(f"Resultado: {dividir(a, b)}")
            case "5":
                print(f"Resultado: {potencia(a, b)}")
            case _:
                print("Opción inválida.")

while True:
    calculadora()
    continuar = input("¿Quieres realizar otra operación? (s/n): ").lower()
    if continuar != 's':
        print("Gracias por usar CalcuPython")
        break