##primer intento arrojo el error de que no se puede llamar la variable
# def grupo_a(grupo_a):
#     grupo_a=[]
#     grupo_b=[]
#     grupo_c=[]
#     try:
#         print("funciona bien")
#         nombre = (input("Ingrese el nombre del coder: "))
#         mesingreso = (input("Ingrese el mes que ingreso: "))
#         grupocoder = (input("Ingrese el grupo que pertenece: "))
#         edad = (input("Ingrese la edad del coder: "))
#         print("funciona bien")

#         coder = {"nombre": (nombre.capitalize()), "mes_ingreso": (mesingreso), "edad": (edad)}

#         grupo_a.append(coder)
#         print(grupo_a)

#         print("Se agrego correctamente \n")
#     except :
#         print("Los valores ingresados no son validos")

# def main ():
    # grupo_a=[]
    # grupo_b=[]
    # grupo_c=[]
#     while True:
#         try:
#             input("Presione enter para continuar...")
#             opcion = int(input("Seleccione el grupo: \
#             \n 1. Grupo A\
#             \n 2. Grupo B\
#             \n 3. Grupo C\
#             \n 4. Salir\
#             \n Ingrese una opcion del 1 al 4: "))
#         except : 
#             print("Ingresa valores enteros del 1 al 4")

#         match opcion:
#             case 1:
#                 grupo_a(grupo_a)
#             case 2:
#                 grupo_b()
#             case 3:
#                 grupo_c()
#             case 4:
#                 print("Finalizado")
#                 break
# main()
##segundo intento arrojo el error de que no se puede llamar la variable

# def grupo_a(grupo_a):
#     nombre = str(input("Ingrese el nombre del coder: "))
#     mes_ingreso = str(input("Ingrese el mes que ingreso: "))
#     grupo_coder = str(input("Ingrese el grupo que pertenece: "))
#     edad = int(input("Ingrese la edad del coder: "))

#     coder = {"nombre": (nombre.capitalize()), "mes_ingreso": (mes_ingreso), "grupo_coder": (grupo_coder) , "edad": (edad)}

#     grupo_a(grupo_a.append(coder))
#     print(grupo_a)

#     print("Se agrego correctamente \n")

# def main():
#     grupo_a=[]
#     grupo_b=[]
#     grupo_c=[]
#     while True:
#         try:
#             input("Presione enter para continuar...")
#             opcion = int(input("Seleccione el grupo: \
#             \n 1. Grupo A\
#             \n 2. Grupo B\
#             \n 3. Grupo C\
#             \n 4. Salir\
#             \n Ingrese una opcion del 1 al 4: "))
#         except : 
#             print("Ingresa valores enteros del 1 al 4")
        
#         if opcion==1:
#             grupo_a(grupo_a)
#         elif opcion==2:
#             grupo_b(grupo_b)
#         elif opcion==3:
#             grupo_c(grupo_c)
#         else:
#             print("finalizado")
#             break
# main()

# #tercer intento descubri que el error fue de identificacion,
# #ya que estaba llamando igual que la funcion y por eso no se podia llamar
# #hora que descubri el error 8:50, por lo que apenas estoy haciendo el primer punto

def grupo_a(grupo1):
    nombre=input("ingrese el nombre: ")
    ingreso=input("mes que ingreso: ")
    grupo=input("cual grupo pertenece: ")
    edad=input("cual es du edad: ")
    coder={"nombre":(nombre),"ingreso":(ingreso),"grupo":(grupo),"edad":(edad)}
    print(coder)
    grupo1.append(coder)
    print("se agrego correctamente")

def grupo_b(grupo2):
    nombre=input("ingrese el nombre: ")
    ingreso=input("mes que ingreso: ")
    grupo=input("cual grupo pertenece: ")
    edad=input("cual es du edad: ")
    coder={"nombre":(nombre),"ingreso":(ingreso),"grupo":(grupo),"edad":(edad)}
    print(coder)
    grupo2.append(coder)
    print("se agrego correctamente")

def grupo_c(grupo3):
    nombre=input("ingrese el nombre: ")
    ingreso=input("mes que ingreso: ")
    grupo=input("cual grupo pertenece: ")
    edad=input("cual es du edad: ")
    coder={"nombre":(nombre),"ingreso":(ingreso),"grupo":(grupo),"edad":(edad)}
    print(coder)
    grupo3.append(coder)
    print("se agrego correctamente")

def mostrar_coders(opcion):
    if not opcion:
        print("grupo vacio")
    else:
        print("lista de coders")
        for index, valor in enumerate(opcion):
            print(index,"-",valor["nombre"],"-",valor["ingreso"],"-",valor["grupo"],"-",valor["edad"])

def main():
    grupo1=[]
    grupo2=[]
    grupo3=[]
    opcion=int(input("seleccione el grupo: \
        \n 1. grupo a\
        \n 2. grupo b\
        \n 3. grupo c\
        \n ingrese una opcion: "))

    if opcion==1:
        grupo_a(grupo1)
    elif opcion==2:
        grupo_b(grupo2)
    elif opcion==3:
        grupo_c(grupo3)
    else:
        print("error")
    
    opcion2=input("seleccione la accion a realizar: \
        \n 1. listar coders del grupo\
        \n 2. eliminar coders del grupo\
        \n 3. agregar mas coders\
        \n ingrese una opcion: ")

    if opcion2==1:
        mostrar_coders(opcion)
    elif opcion2==3:
        return(opcion)
    else:
        print("no hay")

main()