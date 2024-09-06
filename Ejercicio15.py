
num2=int(input("Ingrese un numero entero: "))
x=False
y=False
num1=num2
num=num1

#divisible en 2
if num % 2 == 0:
    print("Cumple el criterio de divisibilidad del 2")
    x=True
else:
    x=False

#divisible en 3
suma=0
while num>0: 
    resto= num % 10
    suma= suma + resto 
    num=num // 10 

if suma % 3 ==0: 
    print("Cumple con el criterio de divisibilidad del 3 ")  
    y=True
else:
    y=False

#divisible en 5

if num1 % 5 == 0 and 5:
     print("Cumple con el criterio de divisibilidad del 5")

#divisible en 6

if x==True and y== True:
    print("Cumple con el criterio de divisibilidad del 6")

#divisible en 9
sumar=0
while num1>0:
    sobra=num1%10
    sumar=sumar+sobra
    num1=num1//10
    
if sumar % 9==0:
    print("Cumple con los criterios de divisibilidad de 9")

#divisible en 10

if num2%10==0:
    print("Cumple con los criterios de divisibilidad de 10")