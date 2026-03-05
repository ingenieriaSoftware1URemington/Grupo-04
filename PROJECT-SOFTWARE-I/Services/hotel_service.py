from models.Model_Hoteleria import Hotel, Habitacion
from datetime import datetime

def crear_hotel(id_hotel: int, nombre: str, ciudad: str):
    return Hotel(id_hotel, nombre, ciudad)

def agregar_habitacion_a_hotel(hotel: Hotel, numero: int, tipo: str, precio: float):
    habitacion = Habitacion(numero, precio)
    hotel.agregar_habitacion(habitacion)
    return habitacion

def Consultar_Disponibilidad(hotel: Hotel, fecha_inicio: datetime, fecha_fin: datetime):
    return hotel.consultar_disponibilidad(fecha_inicio, fecha_fin)
