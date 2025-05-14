import CalcuPython

while True:
    CalcuPython.calculadora()
    continuar = input("¿Quieres realizar otra operación? (s/n): ").lower()
    if continuar != 's':
        print("Gracias por usar CalcuPython")
        break