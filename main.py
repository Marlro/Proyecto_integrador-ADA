def pedir_nombre():
    nombre = input("Por favor, ingresa tu nombre: ")
    return nombre

def mostrar_mensaje_bienvenida(nombre):
    print(f"Bienvenido, {nombre}!")

if __name__ == "__main__":
    nombre = pedir_nombre()
    mostrar_mensaje_bienvenida(nombre)
