laberinto_original = [
    ["F",  1,  1,  1,  0,  1,  1,  1,  1],
    [-2,  0,  0, -1,  0,  1,  0,  1,  0],
    [ 1,  1,  0,  1,  1,  1,  0,  1,  1],
    [ 0,  1,  0, -1,  0,  0,  0, -1,  1],
    [ 1,  1,  1,  1,  1,  1,  1,  1,  0],
    [-1,  0,  0,  0,  0,  0,  0,  1,  1],
    [ 1,  1,  1,  1, -1,  1,  1,  1,  0],
    [ 1,  0,  0,  1,  0,  1,  0,  1,  1],
    ["I",  1, -1,  1,  1,  1,  0,  1,  1],
]

FILAS = len(laberinto_original)
COLS = len(laberinto_original[0])

INICIO = (8, 0)   
META = (0, 0)    
VIDAS_INICIALES = 3
MOVIMIENTOS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
NOMBRES_MOV = {(1, 0): "abajo", (0, 1): "derecha", (-1, 0): "arriba", (0, -1): "izquierda"}


def valor_celda(fila, col):
    valor = laberinto_original[fila][col]
    if valor == "I" or valor == "F":
        return 1
    return valor


def imprimir_laberinto_original():
    print("Laberinto original (9x9):")
    for fila in laberinto_original:
        print(" ".join(str(c).rjust(2) for c in fila))
    print()


def imprimir_matriz_camino(camino):
    matriz = [["." for _ in range(COLS)] for _ in range(FILAS)]
    for paso, (f, c) in enumerate(camino):
        matriz[f][c] = "*"
    matriz[INICIO[0]][INICIO[1]] = "I"
    matriz[META[0]][META[1]] = "F"

    print("Matriz que indica la ruta de salida (* = camino recorrido):")
    for fila in matriz:
        print(" ".join(str(c).rjust(2) for c in fila))
    print()


def es_valida(fila, col):
    return 0 <= fila < FILAS and 0 <= col < COLS and valor_celda(fila, col) != 0


def resolver(fila, col, vidas, visitado, camino, paso):
    print(f"Paso {paso}: ratón en ({fila},{col}) | valor={valor_celda(fila, col)} | vidas={vidas}")

    if (fila, col) == META:
        camino.append((fila, col))
        print(f"  -> ¡Llegó a la meta F con {vidas} vida(s)!\n")
        return True

    visitado[fila][col] = True
    camino.append((fila, col))

    for mov in MOVIMIENTOS:
        nf, nc = fila + mov[0], col + mov[1]

        if not es_valida(nf, nc):
            continue
        if visitado[nf][nc]:
            continue

        valor = valor_celda(nf, nc)
        vidas_restantes = vidas
        if valor == -1:
            vidas_restantes -= 1
        elif valor == -2:
            vidas_restantes -= 2

        if vidas_restantes <= 0:
            print(f"  Intento hacia {NOMBRES_MOV[mov]} ({nf},{nc}) -> "
                  f"perdería todas las vidas (camino inviable, se descarta)")
            continue

        print(f"  Avanza hacia {NOMBRES_MOV[mov]}: ({nf},{nc})")
        if resolver(nf, nc, vidas_restantes, visitado, camino, paso + 1):
            return True
    print(f"  Retrocede desde ({fila},{col}) [sin salida por aquí]")
    camino.pop()
    visitado[fila][col] = False
    return False


def main():
    imprimir_laberinto_original()

    visitado = [[False] * COLS for _ in range(FILAS)]
    camino = []

    
    encontrado = resolver(INICIO[0], INICIO[1], VIDAS_INICIALES, visitado, camino, paso=1)

    print("=" * 50)
    if encontrado:
        print(f"RESULTADO: El ratón SÍ logró salir del laberinto.")
        print(f"Camino encontrado ({len(camino)} pasos): {camino}\n")
    else:
        print("RESULTADO: El ratón NO logró salir del laberinto "
              "(no existe camino que conserve al menos 1 vida).\n")

    imprimir_matriz_camino(camino)


if __name__ == "__main__":
    main()