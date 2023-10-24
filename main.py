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
