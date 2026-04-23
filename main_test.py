from utils import crear_tablero, pedir_barcos_jugador, colocar_barcos, disparar, crear_lista_barcos 

# VARIABLES JUGADOR
tablero_jugador_disparos = crear_tablero()      # tablero donde se marcan los disparos del jugador
tablero_jugador_barcos = crear_tablero()        # tablero donde se marcan los barcos del jugador
lista_disparos_jugador = []

# VARIABLES RIVAL
tablero_rival_disparos = crear_tablero()        # tablero donde se marcan los disparos del rival
tablero_rival_barcos = crear_tablero()          # tablero donde se marcan los barcos del rival
lista_disparos_rival = []

# FUNCIÓN DE PEDIR BARCOS AL JUGADOR Y AL RIVAL
lista_barcos_jugador = [[(3, 1), (3,2)], [(3, 7),(4, 7), (5, 7)]]
lista_barcos_rival = [[(3, 1), (3,2)], [(3, 7),(4, 7), (5, 7)]]
#-----------------------------

lista_barcos_rival = crear_lista_barcos

# COLOCAR BARCOS JUGADOR
tablero_jugador_barcos = colocar_barcos([barco], lista_barcos_jugador)

#COLOCAR BARCOS RIVAL
tablero_rival_barcos = colocar_barcos(lista_barcos_rival, tablero_rival_barcos)

print(tablero_jugador_disparos)
print("                 ")
print(tablero_jugador_barcos)

# SOY EL RIVAL
tablero_jugador_barcos, lista_disparos_rival = disparar(tablero_jugador_barcos, lista_barcos_rival)

print(tablero_jugador_barcos)
print("                 ")
print(tablero_jugador_rival)

"""
# Funcion de pedir barcos al jugador y al rival
lista_barcos_jugador = [[(0,1), (0,2)], [(3,4), (4,4), (5,4)]]    # No veo los barquitos en la columna 4
lista_barcos_rival = [[(3,1), (3,2)], [(3,7), (4,7), (5,7)]]
# -------------------------------------
"""
