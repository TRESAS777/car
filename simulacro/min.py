def grupo_a(grupo1):
    nombre=input("ingrese el nombre: ")
    ingreso=input("mes que ingreso: ")
    grupo=input("cual grupo pertenece: ")
    edad=input("cual es du edad: ")
    coder={"nombre":(nombre),"ingreso":(ingreso),"grupo":(grupo),"edad":(edad)}
    print(coder)
    grupo1.append(coder)
    print("se agrego correctamente")


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
    if opcion==2:
        nombre=input("ingrese el nombre: ")
        ingreso=input("mes que ingreso: ")
        grupo=input("cual grupo pertenece: ")
        edad=input("cual es du edad: ")
        coder={"nombre":(nombre),"ingreso":(ingreso),"grupo":(grupo),"edad":(edad)}
        print(coder)
        grupo2.append(coder)
        print("se agrego correctamente")
    if opcion==3:
        nombre=input("ingrese el nombre: ")
        ingreso=input("mes que ingreso: ")
        grupo=input("cual grupo pertenece: ")
        edad=input("cual es du edad: ")
        coder={"nombre":(nombre),"ingreso":(ingreso),"grupo":(grupo),"edad":(edad)}
        print(coder)
        grupo3.append(coder)
        print("se agrego correctamente")
    else:
        print("error")
main()