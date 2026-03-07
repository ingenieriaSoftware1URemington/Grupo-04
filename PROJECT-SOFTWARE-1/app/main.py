# Importamos funciones de servicios del sistema
from Services.hotel_service import crear_hotel, Consultar_Disponibilidad
from Services.Reserva_Services import crear_reserva
from models.Model_Hoteleria import Hotel, Habitacion, Turista # Importamos las clases del modelo

import datetime

# Diccionario donde guardamos los usuarios del sistema
usuarios = {
    "admin": {"password": "1234", "rol": "ADMIN"},
    "dani": {"password": "456", "rol": "turista"},
}

# Listas donde guardamos información del sistema
hoteles = []
reservas = []
empleados = []
destinos = []

# Creamos algunos hoteles de ejemplo
hotel1 = Hotel(1, "Hotel Esteban de Campo amor", "Manizales")
hotel2 = Hotel(2, "Hotel Alexis de las delicias", "Medellín")
# Creamos habitaciones
hab1 = Habitacion(101, 150.0)
hab2 = Habitacion(102, 200.0)
# Agregamos habitaciones al hotel
hotel1.agregar_habitacion(hab1)
hotel1.agregar_habitacion(hab2)

hoteles.extend([hotel1, hotel2])# Guardamos los hoteles en la lista

# Funcion que muestra el menú principal del sistema
def mostrar_menu_principal():

    print("\nSISTEMA DE RESERVAS")
    print("1 Iniciar")
    print("2 Registrarse")
    print("3 Salir")
    return input("Opcion: ")

# Funcion para registrar un nuevo usuario
def registrar():

    user = input("Nuevo usuario: ")
    password = input("Contraseña: ")
    usuarios[user] = {"password": password, "rol": "turista"}
    print("Usuario creado")

# Funcion para iniciar sesión
def login():

    user = input("Usuario: ")
    password = input("Contraseña: ")
     # Verificamos si el usuario existe y la contraseña coincide
    if user in usuarios and usuarios[user]["password"] == password: 
        return user, usuarios[user]["rol"]
    else:
        print("Datos incorrectos")
        return None, None

# Funcion para mostrar los hoteles disponibles
def ver_hoteles():

    for i, h in enumerate(hoteles):
        print(i + 1, h.nombre, "-", h.ciudad)

# Función para que un usuario cree una reserva
def crear_reserva_usuario(usuario):
    ver_hoteles() # Mostramos hoteles disponibles
    i = int(input("Hotel #: ")) - 1
    hotel = hoteles[i]
    fecha_inicio = datetime.datetime.strptime(
        input("Fecha inicio YYYY-MM-DD: "), "%Y-%m-%d"# Pedimos fechas de reserva
    )
    fecha_fin = datetime.datetime.strptime(input("Fecha fin YYYY-MM-DD: "), "%Y-%m-%d")
    disponibles = Consultar_Disponibilidad(hotel, fecha_inicio, fecha_fin)# Buscamos habitaciones disponibles
    for j, hab in enumerate(disponibles):# Mostramos habitaciones disponibles
        print(j + 1, hab.numero, "-", hab.precio)
    k = int(input("Habitacion #: ")) - 1  # El usuario elige habitación
    habitacion = disponibles[k]
    turista = Turista(1, usuario, f"{usuario}@mail.com", "PAS123")# Creamos un turista temporal
    reserva = crear_reserva(
        len(reservas) + 1, turista, habitacion, fecha_inicio, fecha_fin, hotel.ciudad # Creamos la reserva
    )
    reservas.append(reserva)# Guardamos la reserva
    print("Reserva creada en", reserva.destino)

# Funcion para ver historial de reservas del usuario
def historial(usuario):

    print("\nHISTORIAL")

    for r in reservas:
        if r.turista.nombre == usuario:
            print(r.destino, r.fecha_inicio.date(), "a", r.fecha_fin.date())


# Menu del usuario cuando ya inicio sesion
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
            crear_reserva_usuario(user)

        elif op == "3":
            historial(user)

        elif op == "4":
            break

# Funcion principal del programa
def main():

    while True:
        op = mostrar_menu_principal()

        if op == "1":
            user, rol = login()

            if user:
                menu_usuario(user)

        elif op == "2":
            registrar()

        elif op == "3":
            break
main()
