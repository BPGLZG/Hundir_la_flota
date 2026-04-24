import numpy as np

# Función para crear tablero
def crear_tablero(size = 10):    # por default está en 10, así que se pueden cambiar las dimensiones para la "demo"
    return np.full((size, size), "_")


# Función para pedir barco a jugador
def pedir_barco_jugador(eslora):
    fila = int(input("Fila inicial: "))
    columna = int(input("Columna inicial: "))
    direccion = input("Dirección (h/v): ")

    barco = []

    for i in range(eslora):
        if direccion == "h":
            barco.append((fila, columna + i))
        else:
            barco.append((fila + i, columna))

    return barco

# Función para validar barco
def validar_barco(barco, tablero):
    size = len(tablero)

    for fila, columna in barco:
        if fila < 0 or fila >= size or columna < 0 or columna >= size:
            return False
        if tablero[fila][columna] != "_":
            return False

    return True

# Función para colocar barco en el tablero del jugador
def colocar_barco(barco, tablero):
    for fila, columna in barco:
        tablero[fila][columna] = "O"

# Función para crear el barco de la máquina
def crear_barco(eslora, size = 10):             # si no jala, quitarl el size = 10
    direccion = np.random.choice(["h", "v"])
    fila = np.random.randint(0, size)           # si no jala, regresar a 10
    columna = np.random.randint(0, size)        # si no jala, regresar a 10

    barco = []

    for i in range(eslora):
        if direccion == "h":
            barco.append((fila, columna + i))
        else:
            barco.append((fila + i, columna))

    return barco

# Función para colocar barcos del jugador
def colocar_barcos_jugador(tablero):
    for eslora in [2, 2, 2, 3, 3, 4]:
        valido = False

        while valido == False:
            print(f"Coloca un barco de tamaño {eslora}")
            barco = pedir_barco_jugador(eslora)

            if validar_barco(barco, tablero):
                colocar_barco(barco, tablero)
                valido = True
            else:
                print("Barco inválido")

# Función para colocar barcos de la máquina
def colocar_barcos_maquina(tablero):
    for eslora in [2, 2, 2, 3, 3, 4]:
        valido = False

        while valido == False:
            barco = crear_barco(eslora)

            if validar_barco(barco, tablero):
                colocar_barco(barco, tablero)
                valido = True

# Función para disparar
def disparar(casilla, tablero_objetivo, tablero_disparos):
    fila, columna = casilla

    if tablero_disparos[fila][columna] != "_":
        print("Ya disparaste ahí")
        return

    if tablero_objetivo[fila][columna] == "O":
        tablero_objetivo[fila][columna] = "X"
        tablero_disparos[fila][columna] = "X"
        print("Acertaste")
    else:
        tablero_disparos[fila][columna] = "A"
        print("Agua")

# Función para pedir disparo
def pedir_disparo():
    fila = int(input("Fila: "))
    columna = int(input("Columna: "))
    return (fila, columna)

# Funcion de disparo de la máquina
def disparo_maquina(tablero_disparos):
    size = len(tablero_disparos)
    while True:
        fila = np.random.randint(0, size)
        columna = np.random.randint(0, size)

        if tablero_disparos[fila][columna] == "_":
            return (fila, columna)

# Función para comprobar si quedan barcos
def quedan_barcos(tablero):
    return "O" in tablero