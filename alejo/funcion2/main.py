from funcion2.funcion import agregar_tarea,ver_tarea,actualizar_tarea,eliminar_tarea
def main ():
    tareas=[]
    while True:
        try:
            input("Presione enter para continuar...")
            opcion = int(input("\n ====== Tareas a realizar ======\
                \n 1. Agregar tarea\
                \n 2. Eliminar tarea \
                \n 3. Actualizar tarea\
                \n 4. Ver tareas\
                \n 5. Salir\
                \n Ingrese una opcion: "))
        except:
            print("Ingrese valores del 1 al 5")

        match opcion:
            case 1:
                agregar_tarea(tareas)
            case 2:
                eliminar_tarea(tareas)
            case 3:
                actualizar_tarea(tareas)
            case 4:
                ver_tarea(tareas)
            case 5:
                print("Finalizado")
                break
main()
