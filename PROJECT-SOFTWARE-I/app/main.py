# Importaciones 
from Services.Reserva_Services import crear_reserva, cancelar_reserva, listar_reservas,crear_hotel, agregar_habitacion_a_hotel, Consultar_Disponibilidad
from models.Model_Hoteleria import Persona, Turista, Empleado
import datetime
# Usuarios del sistema
usuarios = {
    "admin": {"password": "1234", "rol": "ADMIN"},
}

# Bases de datos para guardar hoteles, destinos, empleados y reservas
hoteles = []
destinos = []
empleados = []
reservas = []


#MENU PRINCIPAL
def mostrar_menu_principal():
    while True:
        print(" SISTEMA DE VENTAS ")
        print("1 Iniciar ")
        print("2 Registrarse")
        print("3 Salir")
        opcion = input("Opcion: ")
        if opcion in ["1", "2", "3"]:
            return opcion
        else:
            print("Opción inválida, intenta de nuevo.")


#REGISTRAR USUARIO
def registrar():
    user = input("Nuevo usuario: ")
    if user in usuarios:
        print("Ya existe")
        return
    password = input("Contraseña: ")
    usuarios[user] = {"password": password, "rol": "USUARIO"}
    print("Usuario creado")


#LOGIN
def login():
    user = input("Usuario: ")
    password = input("Contraseña: ")

    if user in usuarios and usuarios[user]["password"] == password:
        return user, usuarios[user]["rol"]
    else:
        print("Datos incorrectos")
        return None, None


#AGREGAR HOTEL

def agregar_hotel():
    nombre = input("Hotel: ")
    ciudad = input("Ciudad: ")
    id_hotel = len(hoteles) + 1
    hotel = crear_hotel(id_hotel, nombre, ciudad)
    hoteles.append(hotel)
    print("Hotel creado:", hotel.nombre)



#VER HOTELES
def ver_hoteles():
    if not hoteles:
        print("No hay hoteles")
    else:
        for i, h in enumerate(hoteles):
            print(i+1, h.nombre, "-", h.ciudad)



#DESTINOS 
def agregar_destino():
    destinos.append(input("Destino: "))


#EMPLEADOS
def agregar_empleado():
    nombre = input("Empleado: ")
    cargo = input("Cargo: ")
    empleados.append({"nombre": nombre, "cargo": cargo})


#CREAR RESERVA
def crear_reserva(usuario):
    ver_hoteles()
    if not hoteles:
        return

    i = int(input("Hotel #: ")) - 1
    hotel = hoteles[i]

    # Mostrar habitaciones disponibles
    fecha_inicio = datetime.datetime.strptime(input("Fecha inicio (YYYY-MM-DD): "), "%Y-%m-%d")
    fecha_fin = datetime.datetime.strptime(input("Fecha fin (YYYY-MM-DD): "), "%Y-%m-%d")

    disponibles = Consultar_Disponibilidad(hotel, fecha_inicio, fecha_fin)
    if not disponibles:
        print("No hay habitaciones disponibles")
        return

    for j, hab in enumerate(disponibles):
        print(j+1, "Habitación", hab.numero, "-", hab.precio)

    k = int(input("Habitación #: ")) - 1
    habitacion = disponibles[k]

    turista = Turista(1, usuario, f"{usuario}@mail.com", "PAS123")
    reserva = crear_reserva(len(reservas)+1, turista, habitacion, fecha_inicio, fecha_fin, hotel.ciudad)
    reservas.append(reserva)
    print("Reserva creada:", reserva.destino, reserva.turista.nombre)


#HISTORIAL 
def historial(usuario):

    for r in reservas:
        if r["usuario"] == usuario:
            print(r["hotel"], "-", r["fecha"])


#MENU ADMIN 
def menu_admin(user):

    while True:

        print("1 Hoteles")
        print("2 Destinos")
        print("3 Empleados")
        print("4 Ver reservas")
        print("5 Salir")

        op = input("Opcion: ")

        if op == "1":
            agregar_hotel()

        elif op == "2":
            agregar_destino()

        elif op == "3":
            agregar_empleado()

        elif op == "4":
            print(reservas)

        elif op == "5":
            break


# MENU USUARIO 
def menu_usuario(user):

    while True:

        print("\n1 Ver hoteles")
        print("2 Reservar")
        print("3 Historial")
        print("4 Salir")

        op = input("Opcion: ")

        if op == "1":
            ver_hoteles()

        elif op == "2":
            crear_reserva(user)

        elif op == "3":
            historial(user)

        elif op == "4":
            break


#PROGRAMA PRINCIPAL
def main():

    while True:

        op = mostrar_menu_principal()

        if op == "1":

            user, rol = login()

            if user:
                if rol == "ADMIN":
                    menu_admin(user)
                else:
                    menu_usuario(user)

        elif op == "2":
            registrar()

        elif op == "3":
            break


main()