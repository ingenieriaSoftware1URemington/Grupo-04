from models.Model_Hoteleria import Hotel, Habitacion, Reserva, Sucursal
import datetime

reservas = []
hoteles = [] 

def crear_reserva(id_reserva: int, turista, habitacion: Habitacion, fecha_inicio: datetime, fecha_fin: datetime, destino: str):
    reserva = Reserva(id_reserva, turista, habitacion, fecha_inicio, fecha_fin, destino)
    reservas.append(reserva)
    return reserva

def cancelar_reserva(reserva: Reserva):
    reserva.cancelar()
    reservas.remove(reserva)
    return True

def listar_reservas(): 
    return reservas

## Hoteles 

def crear_hotel(id_hotel: int, nombre: str, ciudad: str): 
    hotel = Hotel(id_hotel, nombre, ciudad) 
    hoteles.append(hotel) 
    return hotel

def agregar_habitacion_a_hotel(hotel: Hotel, numero_de_habitacion: int, tipo: str, precio: float):
    habitacion = Habitacion(numero_de_habitacion, tipo, precio)
    hotel.agregar_habitacion(habitacion)
    return habitacion

def Consultar_Disponibilidad(hotel: Hotel, fecha_inicio: datetime, fecha_fin: datetime):
    return hotel.consultar_disponibilidad(fecha_inicio, fecha_fin)

#