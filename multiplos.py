while True:
    try:
        numero1=int(input("ingrese el primer numero: "))
        numero2=int(input("ingrese el segundo numero: "))
        numero3=int(input("ingrese el tercer numero: "))
        if numero1%3==0 and numero1%5==0 and numero2%3==0 and numero2%5==0 and numero3%3==0 and numero3%5==0 :
            print("Los numeros son multiplos de 3 y 5")
        else:
            print("Los numeros no son multiplos de 3 y 5")
        break
    except ValueError:
        print("Ingresa numeros enteros")
