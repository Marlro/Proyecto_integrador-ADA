def pedir_nombre():
    nombre = input("Por favor, ingresa tu nombre: ")
    return nombre

def mostrar_mensaje_bienvenida(nombre):
    print(f"Bienvenid@, {nombre}!")

if __name__ == "__main__":
    nombre = pedir_nombre()
    mostrar_mensaje_bienvenida(nombre)

import readchar

def main():
    while True:
        key = readchar.readkey()
        print(f'Key pressed: {key}')
        if key == '\x1b[A':  # Código para la tecla de arriba (UP)
            break

if __name__ == "__main__":
    main()

import os
import readchar

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    number = 0
    while number <= 50:
        clear_screen()
        print(f'Número actual: {number}')
        key = readchar.readkey()
        if key == 'n':
            number += 1

if __name__ == "__main__":
    main()
def convertir_mapa_a_matriz(mapa):
    matriz = [list(fila) for fila in mapa.split("\n")]
    return matriz

def mostrar_mapa(mapa):
    for fila in mapa:
        print("".join(fila))

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_loop(mapa, posicion_inicial, posicion_final):
    px, py = posicion_inicial
    
    while (px, py) != posicion_final:
        mapa[py][px] = 'P'
        limpiar_pantalla()
        mostrar_mapa(mapa)

        # Leer teclas y procesar movimiento
        key = readchar.readkey()
        nueva_px, nueva_py = px, py

        if key == '\x1b[A':  # Flecha arriba
            nueva_py = max(0, py - 1)
        elif key == '\x1b[B':  # Flecha abajo
            nueva_py = min(len(mapa) - 1, py + 1)
        elif key == '\x1b[C':  # Flecha derecha
            nueva_px = min(len(mapa[0]) - 1, px + 1)
        elif key == '\x1b[D':  # Flecha izquierda
            nueva_px = max(0, px - 1)
        
        if mapa[nueva_py][nueva_px] != '#':
            mapa[py][px] = '.'
            px, py = nueva_px, nueva_py

# Ejemplo de uso
mapa = """
##########
#........#
#.#.######
#.#.#....#
#.#.#.##.#
#...#....#
########.#
#........#
########.#
"""
mapa_matriz = convertir_mapa_a_matriz(mapa)
posicion_inicial = (0, 0)
posicion_final = (9, 9)

main_loop(mapa_matriz, posicion_inicial, posicion_final)
