import cajero

while True:
    cajero.correr()
    try:
        seguir = input("¿Deseas continuar utilizando nuestros servicios? (s/n): ").lower()
        if seguir != "s":
            break
    except ValueError:
        print("Error, opción no válida")