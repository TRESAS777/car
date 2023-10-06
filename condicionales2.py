while True:
    try:
        edad=int(input("ingrese su edad en años: "))
        if edad < 0:
            print("Debe ingresar numeros positivos")
        elif edad >= 18:
            print("Eres mayor de edad")
        else:
            print("Eres menor de edad")
        break
    except ValueError:
        print("Edad no valida")
