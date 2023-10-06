while True:
    try:
        a=int(input("ingrese el primer numero: \n"))
        b=int(input("ingrese el segundo numero: "))
        if a==b :
            print(a,"es igual a",b)
        elif a > b :
            print(a,"es mayor que",b)
        else:
            print(b,"es mayor que",a)
        break
    except ValueError:
        print("solo puedes ingresar numeros enteros")
