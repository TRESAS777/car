import random
saldo_inicial = 100
puntos_jugador=()
numero_computadora=()
def lanzar_dado():
    dado = random.randint(1,6)
    return dado

def lanzamiento_computadora():
    numero_computadora = lanzar_dado
    return numero_computadora

def jugador():
    input("Presione enter para lanzar dado")
    puntos_jugador=lanzar_dado()
    print(puntos_jugador)

def jugar_turno():
    if puntos_jugador<lanzamiento_computadora:
        print("Gano el jugador")
    else:
        print("Gano la maquina")
        
jugador()




