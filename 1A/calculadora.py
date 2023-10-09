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

flag = True
flag2 = True
flag3 = True

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
    
    if (opcion == 5):
        flag = False
        
    
    
        