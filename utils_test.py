import numpy as np


# Funcion para crear tableros
def crear_tablero():
    tablero = np.full((10, 10), " ")
    return tablero

# Funcion para pedir barcos al jugador
def pedir_barcos_jugador():
        pos_inicio_f = int(input("fila"))
    pos_inicio_c = int(input("columna"))
    inicio = (pos_inicio_f, pos_inicio_c)
    print(inicio)

# Funcion para crear tablero con barcos
def colocar_barcos(lista_barcos, tablero):
    for i in lista_barcos:
    #print(i)
        for j in i:
        #print(j)    # conozco las posiciones
            tablero[j] = "O"
    return tablero
    
# Funcion para disparar
def disparar(tablero, lista):
    fila = int(input("Fila: "))
    columna = int(input("Columna: "))

    if tablero[fila][columna] == "O":
        tablero[fila][columna] == "X"
    else:
        tablero[fila][columna] == "#"
    
    lista.append((fila, columna))
    
    return tablero, lista

def crear_barco(eslora):
    pos_inicial = (np.random.randint(9), np.random.randint(9))
    orientacion = np.random.choice(["H", "V"])
    
    lista_barco = [pos_inicial]
        pos = pos_inicial

while len(lista_barco) < eslora:
    if orientacion == "V":
        pos = (pos[0] +1, pos[1])
        lista_barco.append(pos)
    else:
        pos = (pos[0], pos[1] + 1)
        lista_barco.append(pos)

return lista_barco



def crear_lista_barcos():
    lista_esloras = [2, 2, 2, 3, 3, 4]
    lista_barcos = []

    for i in lista_esloras:
        barco = crear_barco(i)
        lista_barcos.append(barco)

    return lista_barcos
