peso=float(input("ingrese su masa en k: "))
altura= float(input("ingrese au altura en metros: "))

imc=peso/(altura*altura)
print(imc)
if imc < 18.5:
    print("esta bajo de peso")
elif imc > 18.5 and imc<24.9:
    print("esta en buen estado mantente en forma")
elif imc > 24.9 and imc<29.9:
    print("esta en sobrepeso")
elif imc > 29.9 and imc<34.9:
    print("esta comenzando la obesidad")
elif imc > 34.9 and imc<39.9:
    print("vas para obesidad morbida")
else :
    print("estas en obesidad morbida, haz ejercicio y cuida tu salud")