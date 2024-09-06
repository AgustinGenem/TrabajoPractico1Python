def es_dia_laboral(dia):
    switch = {
        1: "Lunes es un dia laboral.",
        2: "Martes es un dia laboral.",
        3: "Miercoles es un dia laboral.",
        4: "Jueves es un dia laboral.",
        5: "Viernes es un dia laboral.",
        6: "Sábado no es un dia laboral.",
        7: "Domingo no es un dia laboral.",
    }
    return switch.get(dia, "Dia Ingresado no valido.")

while True:
        dia = int(input("Ingrese un numero del 1 al 7 para el dia de la semana: "))
        if 1 <= dia <= 7:
            print(es_dia_laboral(dia))
            break
        else:
            print("El numero ingresado no es valido. Por favor, ingrese un numero entre 1 y 7.")

