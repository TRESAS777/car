def saludar (nombre):
    print("Hola",nombre,"es un bonito dia")

def charla(nombre):
    print("¿Cómo va tu dia",nombre,"?")
    input("")
    print("Muy bien gracias")
    input("Que vas a hacer hoy? ")
    print("Que tengas mucho exito en tu dia")

def despedir(nombre):
    print("Hasta la proxima",nombre)

def main():
    nombre=str(input("Ingrese su nombre para continuar: "))
    saludar(nombre)
    
    charla(nombre)
    
    despedir(nombre)

main()