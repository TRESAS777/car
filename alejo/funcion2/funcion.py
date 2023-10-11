def ver_tarea(tareas):
    if not tareas:
        print("\n No hay tareas \n")
    else:
        print("\n Lista de tareas: \n")
        for index, tarea in enumerate (tareas):
            print(index+1,"-", tarea["nombre"])

def agregar_tarea(tareas):
        nombre = str(input("ingrese el nombre de la tarea a relizar: "))

        añadir = {"nombre" : (nombre.capitalize())}

        tareas.append(añadir)
        for tarea in tareas:
            print(tarea["nombre"])

        print("\t\n Tarea agregada exitosamente \n")

def actualizar_tarea(tareas):
    ver_tarea(tareas)

    if not tareas:
        return
    else:
        try:
            indice = int(input("Ingrese el indice de la tarea a actualizar: "))
            if (indice > 0 or indice <= len(tareas)):
                print("Actualizando el producto -", tareas[indice-1]["nombre"])
                nombre = str(input("ingrese el nuevo nombre de la tarea: "))

                tareas[indice-1]["nombre"]=(nombre)

                print("\t Tarea actualizada exitosamente \n")
            else:
                print("El indice ingresado no corresponde a ninguna tarea")
        except:
            print("Ingresa dentro del rango del indice")

def eliminar_tarea(tareas):
    ver_tarea(tareas)

    try:
        if not tareas:
            return
        else:
            indice = int(input("Ingrese el indice de la tarea a eliminar: "))
            if (indice > 0 or indice <= len(tareas)):
                print("Eliminando el producto -", tareas[indice-1]["nombre"])

                tareas.pop(indice-1)

                print("\t Tarea eliminada exitosamente \n")
            else:
                print("El indice no corresponde a ninguna tarea")
    except:
        print("El indice no es valido")        




    