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

import os
import random

class Juego:
    def __init__(self, mapa, posicion_inicial, posicion_final):
        self.mapa = mapa
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final
        self.px, self.py = posicion_inicial
    
    def convertir_mapa_a_matriz(self):
        # (La función convertir_mapa_a_matriz se mantiene igual)
        pass

    def mostrar_mapa(self):
        # (La función mostrar_mapa se mantiene igual)
        pass

    def limpiar_pantalla(self):
        # (La función limpiar_pantalla se mantiene igual)
        pass

    def main_loop(self):
        # (La función main_loop se mantiene igual)
        pass

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        # Lista de archivos de mapas en la carpeta especificada
        lista_archivos = os.listdir(path_a_mapas)
        # Elegir un archivo aleatorio
        nombre_archivo = random.choice(lista_archivos)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)

        with open(path_completo, 'r') as archivo:
            contenido = archivo.read()

        # Obtener mapa, posición inicial y posición final desde el archivo
        contenido = contenido.strip().split('\n')
        mapa = "\n".join(contenido[:-2])
        pos_inicial = tuple(map(int, contenido[-2].split()))
        pos_final = tuple(map(int, contenido[-1].split()))

        super().__init__(mapa, pos_inicial, pos_final)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de JuegoArchivo con la ruta a la carpeta de mapas
    juego = JuegoArchivo('ruta/a/tu/carpeta/de/mapas')

    # Ejecutar el juego
    juego.main_loop()

from functools import reduce

class Juego:
    # (Otras funciones se mantienen igual)
    
    def convertir_mapa_a_matriz(self):
        return list(map(list, self.mapa.split("\n")))

    def cargar_mapa_desde_archivo(self, archivo):
        with open(archivo, 'r') as file:
            contenido = file.readlines()

        # Obtener mapa, posición inicial y posición final desde el archivo
        contenido = list(map(str.strip, contenido))
        mapa = "\n".join(contenido[:-2])
        pos_inicial = tuple(map(int, contenido[-2].split()))
        pos_final = tuple(map(int, contenido[-1].split()))

        self.mapa = mapa
        self.posicion_inicial = pos_inicial
        self.posicion_final = pos_final
        self.px, self.py = pos_inicial

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        # Lista de archivos de mapas en la carpeta especificada
        lista_archivos = os.listdir(path_a_mapas)
        # Elegir un archivo aleatorio
        nombre_archivo = random.choice(lista_archivos)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)

        self.cargar_mapa_desde_archivo(path_completo)
