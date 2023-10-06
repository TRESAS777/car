while True:
    try:
        numero=int(input("ingrese el numero: "))
        if numero%2==0 and numero>10:
            print("El numero es par y mayor a 10")
        elif numero%2==0 and numero<10:
            print("El numero es par y menor a 10")
        elif numero%2!=0 and numero>10:
            print("El numero es impar y mayor a 10")
        elif numero%2!=0 and numero<10:
            print("El numero es impar y menor a 10")
        else:
            print("Ingresa un numero entero")
        break
    except ValueError:
        print("Solo puedes ingresar numeros")
