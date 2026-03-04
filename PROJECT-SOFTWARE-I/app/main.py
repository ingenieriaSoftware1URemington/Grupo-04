# Usuario de prueba

usuarios = {
    "admin": {"password": "1234", "rol": "ADMIN"},
    "juan": {"password": "0000", "rol": "USUARIO"}
}

# Funciones
def mostrar_menu_principal():
    while True:
        print(" SISTEMA DE VENTAS ")
        print("1 Iniciar sesion")
        print("2 Salir")

        opcion = input("Seleccione una opcion")

        if opcion in ["1", "2"]:
            return opcion
        else:
            print("Opcion invalida")


def login():
    print("INICIO DE SESION")
    username = input("Usuario:")
    password = input("Contraseña:")

    if username in usuarios and usuarios[username]["password"] == password:
        print(f"\nBienvenido {username}")
        return username, usuarios[username]["rol"]
    else:
        print("Usuario o contraseña incorrectos")
        return None, None


def menu_admin(usuario):
    while True:
        print(f" MENU ADMIN ({usuario}) ")
        print("1 Gestionar Usuarios")
        print("2 Gestionar Inventario")
        print("3 Gestionar Ventas")
        print("4 Facturacion")
        print("5 Cerrar sesion")

        try:
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 5:
                print("Cerrando sesion..")
                break
            elif 1 <= opcion <= 4:
                print("Funcion en construccion..")
            else:
                print("Opcion invalida")

        except ValueError:
            print("Debe ingresar un numero")


def menu_usuario(usuario):
    while True:
        print(f" MENU USUARIO ({usuario})")
        print("1 Comprar")
        print("2 Ver historial")
        print("3 Cerrar sesion")

        try:
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 3:
                print("Cerrando sesion...")
                break
            elif opcion in [1, 2]:
                print("Funcion en construccion...")
            else:
                print("Opcion invalida")

        except ValueError:
            print("Debe ingresar un numero")


# PROGRAMA PRINCIPAL

def main():
    while True:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            usuario, rol = login()

            if usuario:
                if rol == "ADMIN":
                    menu_admin(usuario)
                else:
                    menu_usuario(usuario)

        elif opcion == "2":
            print("Saliendo del sistema..")
            break


if __name__ == "__main__":
    main()