from utils import *

# 1. Crear tableros (5x5)
tablero_jugador = crear_tablero(5)
tablero_maquina = crear_tablero(5)

print("Tablero jugador")
print(tablero_jugador)
print("            ")

print("Tablero máquina")
print(tablero_maquina)
print("            ")

tablero_disparos_jugador = crear_tablero(5)
tablero_disparos_maquina = crear_tablero(5)

print("Tablero disparos jugador")
print(tablero_disparos_jugador)
print("            ")

print("Tablero disparos maquina")
print(tablero_disparos_maquina)


# 2. Colocar barcos (DEMO: solo 2 barcos)
print("Coloca tus barcos")

for eslora in [2, 3]:
    valido = False

    while valido == False:
        print(f"Barco de tamaño {eslora}")
        barco = pedir_barco_jugador(eslora)

        if validar_barco(barco, tablero_jugador):
            colocar_barco(barco, tablero_jugador)
            valido = True
        else:
            print("Barco inválido, intenta otra vez")


# Máquina (también solo 2 barcos)
for eslora in [2, 3]:
    valido = False

    while valido == False:
        barco = crear_barco(eslora)

        if validar_barco(barco, tablero_maquina):
            colocar_barco(barco, tablero_maquina)
            valido = True


print("           ")
print("Tablero jugador")
print(tablero_jugador)

print("          ")
print("¡Qué inicie el juego!")
# 3. Juego (limitado para demo)
turnos = 0
MAX_TURNOS = 5

while turnos < MAX_TURNOS:

    # Mostrar tableros
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

    # Comprobar si gana
    if quedan_barcos(tablero_maquina) == False:
        print("¡Has ganado!")
        break

    # Turno de la máquina
    print("          ")
    print("Turno de la máquina")
    casilla_maquina = disparo_maquina(tablero_disparos_maquina)
    print("La máquina dispara en: ", casilla_maquina)

    disparar(casilla_maquina, tablero_jugador, tablero_disparos_maquina)

    print("Disparos de la máquina:")
    print(tablero_disparos_maquina)

    # Comprobar si pierdes
    if quedan_barcos(tablero_jugador) == False:
        print("Has perdido")
        break

    turnos += 1


print("Fin de la demo")