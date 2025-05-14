saldo = 0

def insertar():
    global saldo
    try:
        cantidad = int(input("Ingrese la cantidad a insertar en COP: "))
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        saldo += cantidad
        print(f"Se han insertado {cantidad} pesos. Saldo actual: {saldo} pesos.")
    except ValueError as e:
        print(f"Error: {e}")

def retirar():
    global saldo
    try:
        cantidad = int(input("Ingrese la cantidad a insertar en COP: "))
        if cantidad > saldo:
            raise ValueError("Excedes el saldo disponible")
        saldo -= cantidad
        print(f"Se han retirado {cantidad} pesos. Saldo actual: {saldo} pesos.")
    except ValueError as e:
        print(f"Error: {e}")

def consultar():
    global saldo
    print(f"Su saldo actual es: {saldo} pesos.")

def correr():
    print("Bienvenido a CataCajero","\n", "¿Qué servicio deseas utilizar?")
    print("1. Insertar dinero")
    print("2. retirar dinero")
    print("3. consultar saldo")

    opcion = input("Elige una operación: ")
    if opcion == "1":
        insertar()
    elif opcion =="2":
        retirar()
    elif opcion == "3":
        consultar()
    else:
        raise ValueError("Opción inválida.")

if __name__ == "main":
    while True:
        correr()