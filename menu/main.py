# Sistema de inventario para una tienda
from funciones.funciones import mostrar_inventario, agregar_producto, actualizar_producto

def main():
    inventario = []
    while True:
        try:
            input("Presione enter para continuar...")   
            opcion = int(input("\n ====== Sistema de inventario ======\
                               \n 1. Mostrar inventario\
                               \n 2. Agregar producto\
                               \n 3. Actualizar producto\
                               \n 4. Eliminar producto\
                               \n 5. Exportar a Excel\
                               \n 6. Salir\
                               \n Ingrese una opcion del 1 al 6: "))
        except : 
            print("Ingrese valores enteros del 1 al 6")
        
        match opcion :
            case 1:
                mostrar_inventario(inventario)
            case 2:
                agregar_producto(inventario)
            case 3:
                actualizar_producto(inventario)
            case 4:
                eliminar_producto(inventario)
            case 5:
                Exportar_excel(inventario)
            case 6:
                print("Finalizado")
                break

main()
