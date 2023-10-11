from funcion import comienza_el_juego
def main():
    preguntas=[]
    
    while True:
        try:
            input("Presione enter para continuar...")
            opcion = int(input("\n ====== Tareas a realizar ======\
                \n 1. Jugar\
                \n 2. Salir\
                \n Ingrese una opcion: "))
        except:
            print("Ingrese 1 o 2")
        
        match opcion:
            case 1:
                comienza_el_juego(preguntas)
            case 2:
                print("Finalizado")
                break

main()