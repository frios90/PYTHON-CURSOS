##import numpy as np

def iniciar ():

    puntosTableroUno =  puntosTablero()
    tableroUno = crearTablero(puntosTableroUno)
    pass

def crearTablero (puntosTableroUno) :
    columnas = ["A","B","C","D","E","F","G","H","I"]
    filas = [1,2,3,4,5,6,7,8,9]

    tablero = []


    print("/  | ", end=" ")
    for ind, columna in enumerate(columnas) :
        if ind+1 < len(columnas):
            print(" " + columna + " ", end=" ")
        else:
            print(" " + columna)
            
    for fila in filas :
        print(fila, end=" | ")
        for ind, columna in enumerate(columnas) :            
            print("[o]", end=" ")                
        print()

def puntosTablero ():
    puntos = []

    columnas = ["A","B","C","D","E","F","G","H","I"]
    filas = [1,2,3,4,5,6,7,8,9]
    for fila in filas :
        for columna in columnas :
            punto = str(columna) + str(fila)
            puntos.append({
                'punto':  punto,
                'valor' : "[o]"
                })        
    print(puntos)
    return puntos
## INICIO

def conversor (numero):
    i

iniciar()
