con = str (1234)

ing = input("Ingrese la contraseña: ")
ing = str (ing)
i = int (1)
c = bool (False)

while i <= 3:
    if con == ing:
        print ("Contraseña correcta, Bienvenido Usuario")
        i -= 1
        break
    if con != ing:
        print ("Contraseña erronea")
        ing = input("Ingrese la contraseña: ")
        i += 1
if i >= 3 :
 print ("Demasiados intentos, intentelo mas tarde")
