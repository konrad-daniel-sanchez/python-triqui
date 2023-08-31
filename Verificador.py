# Parámetros de mi Juego de Triqui:
TAMANO = 3
SIMBOLO_JUGADOR_A = 'X'
SIMBOLO_JUGADOR_B = 'O'
esTurnoJugadorA = True
x = 0
y = 0
simbolo = SIMBOLO_JUGADOR_A
esTriqui = False

if not esTurnoJugadorA:
    simbolo = SIMBOLO_JUGADOR_B

# Tablero:
matriz = [
    ['X', 'O', 'O'],
    [' ', 'X', ' '],
    [' ', ' ', 'X']
]

for i in range(0, TAMANO, 1):
    linea = []
    for i in range(0, TAMANO, 1):
        linea.append(' ')
    matriz.append(linea)

# Verificación:

# Se verifica la línea horizontal:
contador = 0
for i in range(0, TAMANO, 1):
    if matriz[y][i] == simbolo:
        contador += 1
esTriqui = (contador == 3)

# Se verifica la línea vertical:
if not esTriqui:
    contador = 0
    for j in range(0, TAMANO, 1):
        if matriz[j][x] == simbolo:
            contador += 1
        j += 1
    esTriqui = (contador == 3)

# Se verifica la diagonal principal (si aplica):
if not esTriqui and x == y:
    contador = 0
    for i in range(0, TAMANO, 1):
        if matriz[i][i] == simbolo:
            contador += 1
    esTriqui = (contador == 3)

# Se verifica la diagonal invertida (si aplica):
if not esTriqui and x + y == TAMANO -1:
    contador = 0
    for i in range(0, TAMANO, 1):
        if matriz[i][TAMANO - 1 - i] == simbolo:
            contador += 1
    esTriqui = (contador == 3)

# Se imprime la matriz en consola:
for i in range(0, TAMANO, 1):
    print(matriz[i])

if esTriqui:
    print('Es triqui')
else:
    print('NO es triqui')
