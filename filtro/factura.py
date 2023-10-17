
def registar_producto(lista_productos,lista):
    producto=input("Ingrese el nombre del producto: ")
    precio=input("Ingrese el valor del producto: ")
    lista={"producto":producto,"precio":precio}
    lista_productos.append(lista)
    print(lista_productos)

def listar_productos(lista_productos,lista):
    for indice in lista_productos:
            print(indice )
        
def mostrar_factura(lista_productos,lista):
    return lista and lista_productos
    
   
def main():
    precio=[]
    lista={"producto","precio"}
    lista_productos=[]
    print("Ingrese los datos del cliente a continuacion:")
    nombre=input("Ingrese su(s) nombre(s) y apellidos: ")
    documento=input("Ingrese su numero de documento: ")
    while True:
        opcion=int(input(" 1. Registrar usuario\
                \n 2. Registar nuevo producto a la factura\
                \n 3. Listar productos de la factura\
                \n 4. Mostrar factura\
                \n 5. Salir\
                \n Elige una opcion: \n"))
        if (opcion==1 or opcion==5):
            break 
        elif (opcion==2):
            registar_producto(lista_productos,lista)
        elif (opcion==3):
            listar_productos(lista_productos,lista)
        elif (opcion==4):
            mostrar_factura(lista_productos,lista)
        else:
            print("Ingresa solo numeros del indice")


main()