num = int(input("Ingrese un valor que no sea 0: "))
i = 0

while i == 0:
    if num > 0:
        print("El numero es mayor que 0")
        i += 1
    else:
        print("El numero es 0 o menor, ingrese uno mayor")
        num = int(input("Ingrese un valor que no sea 0: "))
