tabla1=""
tabla2=""

numero = int(input("Ingrese el numero de la tabla de multiplicar que quiere conocer: "))
fin = int(input("ingrese hasta que numero quiere conocer: "))

for i in range(fin + 1):
    resultado = numero*i
    tabla1 += "\n" + str(numero) + "*" + str(i) + "=" + str(resultado) 
    
    resultado = (numero+1)*i
    tabla1 += "\t" + str(numero+1) + "*" + str(i) + "=" + str(resultado) 

print(tabla1)