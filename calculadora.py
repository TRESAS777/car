opcion = ""
resultado_actual= 0

def mostrarMenu ():
    print("================================")
    print("====== Menú de Opciones ========")
    print("================================")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def sumar(lista, resultado_actual):
        # Suma la lista de números
        total=0
        numeros_sumados=""
        for indice in lista:
            total += indice + resultado_actual
            numeros_sumados += str(indice) + "+"
        # Muestra en pantalla la lista de números y su resultado
        print("La suma de", numeros_sumados[0:len(numeros_sumados)-1], "es:", total)

def restar(lista, resultado_actual):
        # Resta la lista de números
        total=lista[0]
        numeros_restados=""
        for indice in lista[1:]:
            total = total - indice 
            numeros_restados += str(indice) + "-"
        # Muestra en pantalla la lista de números y su resultado
        print("La suma de", numeros_restados[0:len(numeros_restados)-1], "es:", total)

def multiplicar(lista, resultado_actual):
        # multiplica la lista de números
        total=lista[0]
        numeros_multiplicados=""
        for indice in lista[1:]:
            total = total * indice 
            numeros_multiplicados += str(indice) + "*"
        # Muestra en pantalla la lista de números y su resultado
        print("La multiplicacion de", numeros_multiplicados[0:len(numeros_multiplicados)-1], "es:", total)

def division(lista, resultado_actual):
        # Divide la lista de números
        total=lista[0]
        numeros_divididos=""
        for indice in lista[1:]:
            total = total / indice 
            numeros_dividos += str(indice) + "/"
        # Muestra en pantalla la lista de números y su resultado
        print("La division de", numeros_divididos[0:len(numeros_divididos)-1], "es:", total)

flag = True
flag2 = True
flag3 = True
flag4 = True
flag5 = True

while flag:
    mostrarMenu()
    opcion=input("Ingrese una opcion: ")
    
    if(opcion== "1"):
        lista_numeros = []
        while flag2:
            nuevo_numero = float(input("Ingrese el número a sumar: "))
            lista_numeros.append(nuevo_numero)
            seguir = input("Desea continuar? SI(S)/ NO(N): ")
            if (seguir.lower()=="n"):
                flag2=False
            sumar(lista_numeros, resultado_actual)
            
    if(opcion== "2"):
        lista_numeros = []
        while flag3:
            nuevo_numero = float(input("Ingrese el número a restar: "))
            lista_numeros.append(nuevo_numero)
            seguir = input("Desea continuar? SI(S)/ NO(N): ")
            if (seguir.lower()=="n"):
                flag3=False
            restar(lista_numeros, resultado_actual)

    if(opcion== "3"):
        lista_numeros = []
        while flag4:
            nuevo_numero = float(input("Ingrese el número a multiplicar: "))
            lista_numeros.append(nuevo_numero)
            seguir = input("Desea continuar? SI(S)/ NO(N): ")
            if (seguir.lower()=="n"):
                flag4=False
            multiplicar(lista_numeros, resultado_actual)    

    if(opcion== "4"):
        lista_numeros = []
        while flag5:
            nuevo_numero = float(input("Ingrese el número a dividir: "))
            lista_numeros.append(nuevo_numero)
            seguir = input("Desea continuar? SI(S)/ NO(N): ")
            if (seguir.lower()=="n"):
                flag5=False
            division(lista_numeros, resultado_actual)    
    
    if (opcion == 5):
        flag = False
        
    
    
        