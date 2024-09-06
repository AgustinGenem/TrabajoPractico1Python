import random

numeroRandom = random.randint(0, 100)
encontrado = False
intentos = 0

while encontrado == False:
    num = input("Ingrese un número entre 0 y 100: ")
    num = int(num)
    intentos+=1
    if(num==numeroRandom):
        print(f"Correcto, número encontrado, cantidad de intentos {intentos}")
        encontrado = True 
    elif(num>numeroRandom):
        print("Es muy alto.")  
    elif(num<numeroRandom):
        print("Es muy bajo.")  
