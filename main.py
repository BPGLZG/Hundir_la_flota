from utils import *

# 1. Crear tableros
tablero_jugador = crear_tablero()
tablero_maquina = crear_tablero()
print("Tablero jugador")
print(tablero_jugador)
print("            ")

print("Tablero máquina")
print(tablero_maquina)
print("            ")

tablero_disparos_jugador = crear_tablero()
tablero_disparos_maquina = crear_tablero()

print("Tablero disparos jugador")
print(tablero_disparos_jugador)
print("            ")

print("Tablero disparos maquina")
print(tablero_disparos_maquina)

# 2. Colocar barcos
colocar_barcos_jugador(tablero_jugador)
colocar_barcos_maquina(tablero_maquina)

print("           ")
print("Tablero jugador")
print(tablero_jugador)

# 3. Juego
while True:

    # Mostrat tableros
    print("¡Qué inicie el juego!")

    print("          ")
    print("Tablero jugador:")
    print(tablero_jugador)

    print("          ")
    print("Disparos del jugador:")
    print(tablero_disparos_jugador)

    # Turno del jugador
    print("Turno del jugador")
    casilla = pedir_disparo()
    disparar(casilla, tablero_maquina, tablero_disparos_jugador)

    # Comprobar si gana y se acaba el juego
    if quedan_barcos(tablero_maquina) == False:
        print("¡Has ganado!")
        break

    # Turno de la máquina
    print("          ")
    print("Turno de la máquina")
    casilla_maquina = disparo_maquina(tablero_disparos_maquina)
    print("La máquina dispara en: ", casilla_maquina)

    disparar(casilla_maquina, tablero_jugador, tablero_disparos_maquina)

    print("\Disparos de la máquina: ")
    print(tablero_disparos_maquina)

    # Comprobar si pierdes
    if quedan_barcos(tablero_jugador) == False:
        print("Has perdido")
        break