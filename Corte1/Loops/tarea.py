a = input("Ingresa un número para a: ")
a= float(a)

b = input("Ingresa un número para b: ")
b = float(b)

c = a+b

if a == b:
    print("a y b son iguales")
else:
    print("a y b son diferentes")

print("El tipo de a es: ", type(a))
print("El tipo de b es: ", type(b))

print("c = ", c)

if type(a) == type(b):
    print("a y b son del mismo tipo")
else:
    print("a y b son de diferente tipo")