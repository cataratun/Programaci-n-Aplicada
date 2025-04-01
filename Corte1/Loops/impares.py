for i in range (1,21):
    residual = i%2
    if residual == 0:
        print(f'{i} es par')
    else:
        print(f'{i} es impar')
        print(str(i) + "es impar")

for i in range (0,6):
    resultado = i**3
    print(resultado)

times = input("Ingresa un número para times")
times = float(times)
times = int(times)
print(type(times))
print(times)

if times == 0:
    print("No hagas nada")
else:
    for i in range(1, times+1):
        print("i = ", i)