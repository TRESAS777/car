while True:
        
    try:
        print("Ingrese valores desde 0.0 a 5.0")
        parcial=float(input("ingrese la calificacion del parcial: "))
        trabajos=float(input("ingrese la calificacion del trabajos: "))
        promedio=parcial*0.8 + trabajos*0.2
        if promedio>=0 and promedio<=5:
            
            if  promedio<3.0:
                print("Reprobro el semestre")
            elif promedio>=3.0 and promedio<=5.0:
                print("Aprobo el semestre")
            else:
                print("ingrese valores desde 0.0 a 5.0")
            break
    except :
        print("solo puedes ingresar numeros")
