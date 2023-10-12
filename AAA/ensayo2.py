import random

def lanzar_dado(dado):
    dado=random.randint(1,6)
    return dado

def lanzamiento_computadora():
    valor_maquina=lanzar_dado()
    return valor_maquina

def lanzamiento_jugador():
    valor_jugador=lanzar_dado()
    return valor_jugador

def jugador_turno():
    saldo_jugador=100
    saldo_maquina=100
    gano_jugador=0
    gano_maquina=0
    while saldo_jugador>0:
        try:
            apuesta=int(input("Cuanto desea apostar? debe ser multiplo de 10: "))
            apuesta==apuesta%10==0
            if apuesta>=10 and apuesta<saldo_jugador:
                suma_apuesta=apuesta*2
                saldo_jugador=saldo_jugador-apuesta
                saldo_maquina=saldo_maquina-suma_apuesta
                print(saldo_jugador)
                print(saldo_maquina)
                input("Presione enter para lanzar dado...")
                jugador=lanzamiento_jugador()
                maquina=lanzamiento_computadora()
                if jugador>maquina:
                    gano_jugador+=1
                    saldo_jugador=saldo_jugador+suma_apuesta
                    print("ganaste")
                    print(saldo_jugador)
                else:
                    gano_maquina+=1
                    saldo_maquina=saldo_maquina+suma_apuesta
                    print("gano la maquina")
                    print(saldo_maquina)
            else:
                print("Ingresa un valor multiplo de 10")   
        except:
            print("ingrese valores enteros multiplos de 10")
    else: 
        print("no tienes saldo para jugar")        
        
jugador_turno()

