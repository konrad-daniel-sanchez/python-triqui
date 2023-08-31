'''
El código comienza con la definición de algunos parámetros del juego,
como el tamaño del tablero (TAMANO) y los símbolos que usarán
los jugadores (SIMBOLO_JUGADOR_A y SIMBOLO_JUGADOR_B).
Además, se inicializa una variable booleana llamada esTurnoJugadorA
que determinará de quién es el turno.

A continuación, se define una matriz vacía que representará el tablero del Triqui.

Luego, el código inicia un bucle para inicializar la matriz con
espacios en blanco (' ') en todas las casillas.
Esto se hace mediante dos bucles anidados que recorren cada fila y columna de la matriz.

Después de inicializar la matriz, se imprime en la consola para mostrar el tablero vacío.

El siguiente bloque de código implementa la lógica principal del juego
en un bucle while infinito. Dentro de este bucle,
el código solicita al jugador actual que ingrese la posición
donde desea colocar su símbolo.
Esto se hace pidiendo las coordenadas (x, y) de la casilla en la que quieren
colocar su símbolo ('X' o 'O').

Una vez que el jugador proporciona las coordenadas,
el código coloca el símbolo en la matriz en la posición indicada.

Luego, el código imprime nuevamente la matriz actualizada
para mostrar el estado actual del tablero con los símbolos de ambos jugadores.

Finalmente, la variable esTurnoJugadorA se invierte
para alternar los turnos entre los jugadores.
'''

# Parámetros del juego:
TAMANO = 3
SIMBOLO_JUGADOR_A = 'X'
SIMBOLO_JUGADOR_B = 'O'
esTurnoJugadorA = True

# Tablero:
matriz = []

# Inicializa la matriz:
# Recuerda que en Python debemos realizar este paso, porque realmente es una lista de listas
for i in range(0, TAMANO, 1):
    linea = []
    for i in range(0, TAMANO, 1):
        linea.append(' ')
    matriz.append(linea)

# Imprimir matriz:
for i in range(0, TAMANO, 1):
    for j in range(0, TAMANO, 1):
        print(matriz[i][j], end=" ")
    print()

# Lógica del Juego:
while True:
    simbolo = 'X'
    if esTurnoJugadorA == False:
        simbolo = 'O'
    # Lee la posición:
    print('Ingresa tu posición (x) ')
    x =int(input())
    print('Ingresa tu posición (y) ')
    y = int(input())

    # Ingresa la posición en el triqui:
    matriz[y][x] = simbolo

    # Imprimir matriz:
    for i in range(0, TAMANO, 1):
        for j in range(0, TAMANO, 1):
            print(matriz[i][j], end=" ")
        print()

    esTurnoJugadorA = not esTurnoJugadorA
