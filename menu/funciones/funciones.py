def mostrar_inventario(inventario):
    if not  inventario:
        print("\n El inventario esta vacio \n")
    else:
        print("\n Lista de productos: \n")
        for index, valor in enumerate(inventario):
            print(index+1,"-",valor["nombre"],"-",valor["cantidad"],"-",valor["precio"])

def agregar_producto(inventario):
    try:
        nombre = str(input("Ingrese el nombre del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio del producto: "))

        producto = {"nombre": (nombre.capitalize()), "cantidad": (cantidad), "precio": (precio)}

        inventario.append(producto)
        print(inventario)

        print("Producto agregado exitosamente \n")
    except :
        print("Los valores ingresados no son validos")

def actualizar_producto(inventario):
    mostrar_inventario(inventario)

    if not inventario:
        return
    else:
        try:
            indice = int(input("Ingrese el indice del producto que desea actualizar: "))
            if (indice > 0 or indice <= len(inventario)):
                print("Actualizando el producto -", inventario[indice]["nombre"])

                nombre = str(input("Ingrese el nombre del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = float(input("Ingrese el precio del producto: "))

                inventario[indice]["nombre"] = (nombre)
                inventario[indice]["cantidad"] = (cantidad)
                inventario[indice]["precio"] = (precio)

                print("El producto fue actualizado")

            else :
                print("El indice ingresado no corresponde con ningun producto")
        except :
            print("Ingresa valores dentro del rango del indice")

