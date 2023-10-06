while True:
    try:
        nota=int(input("ingresa la nota numerica entre 0 y 100: "))
        if nota >= 0 and nota<=100:
            if nota>=0 and nota<=20:
                print("Su calificacion es: F")
            elif nota>20 and nota<=40:
                print("Su calificacion es: D")
            elif nota>40 and nota<=60:
                print("Su calificacion es: C")
            elif nota>60 and nota<=80:
                print("Su calificacion es: B")
            elif nota>80 and nota<=100:
                print("Su calificacion es: A")
            break
    except ValueError:
        print("Solo puedes ingresar numeros enteros")
        