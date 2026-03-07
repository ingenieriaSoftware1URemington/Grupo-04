# Importamos las clases del modelo
from models.Model_Hoteleria import Hotel, Habitacion, Reserva, Sucursal
import datetime
# Listas donde guardamos Reservas y Hoteles
reservas = []
hoteles = [] 
# Función para crear una reserva
def crear_reserva(id_reserva: int, turista, habitacion: Habitacion, fecha_inicio: datetime, fecha_fin: datetime, destino: str):
    reserva = Reserva(id_reserva, turista, habitacion, fecha_inicio, fecha_fin, destino)  # Creamos el objeto reserva
    reservas.append(reserva)# Guardamos la reserva en la lista
    return reserva   # Retornamos la reserva creada

# Función para cancelar una reserva
def cancelar_reserva(reserva: Reserva):
    reserva.cancelar()
    reservas.remove(reserva)
    return True
# Función que devuelve todas las reservas
def listar_reservas(): 
    return reservas


# Función para crear un hotel
def crear_hotel(id_hotel: int, nombre: str, ciudad: str): 
    hotel = Hotel(id_hotel, nombre, ciudad) # Creamos el objeto hotel

    hoteles.append(hotel) # Guardamos el hotel en la lista
    return hotel # Retornamos el hotel creado

def agregar_habitacion_a_hotel(hotel: Hotel, numero_de_habitacion: int, tipo: str, precio: float):
    habitacion = Habitacion(numero_de_habitacion, tipo, precio)# Creamos el objeto habitacion
    hotel.agregar_habitacion(habitacion)# Guardamos el hotel en la lista
    return habitacion # Retornamos el hotel creado

def Consultar_Disponibilidad(hotel: Hotel, fecha_inicio: datetime, fecha_fin: datetime):
    return hotel.consultar_disponibilidad(fecha_inicio, fecha_fin)

#