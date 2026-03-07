#importaciones   
from models.Model_Hoteleria import Hotel, Habitacion
from datetime import datetime

#crea un hotel y lo guarda en la lista de hoteles
def crear_hotel(id_hotel: int, nombre: str, ciudad: str):
    return Hotel(id_hotel, nombre, ciudad)

#agrega una habitacion para ocupar en el hotel 
def agregar_habitacion_a_hotel(hotel: Hotel, numero: int, precio: float):
    habitacion = Habitacion(numero, precio)
    hotel.agregar_habitacion(habitacion)
    return habitacion

#consulta si esta ocupado o no
def Consultar_Disponibilidad(hotel: Hotel, fecha_inicio: datetime, fecha_fin: datetime):
    return hotel.consultar_disponibilidad(fecha_inicio, fecha_fin)