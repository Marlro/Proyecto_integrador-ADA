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
