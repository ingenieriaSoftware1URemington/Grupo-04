from datetime import datetime
from typing import List

class Persona:
    # esta clase es como una persona normal
    # tiene nombre y correo y ya
    # la usamos para no repetir cosas despues

    def __init__(self, id_persona: int, nombre: str, email: str):
        if not nombre:
            raise ValueError("no puede estar vacio el nombre")

        self.id_persona = id_persona
        self.nombre = nombre
        self.email = email

    def __str__(self):
        # esto es solo para que se vea bonito cuando lo imprimimos
        return f"{self.nombre} ({self.email})"


class Turista(Persona):
    # el turista es una persona que quiere viajarrr y quedarse en el hotel
    # hereda lo de persona porque tambien es persona obvio

    def __init__(self, id_persona: int, nombre: str, email: str, pasaporte: str):
        super().__init__(id_persona, nombre, email)

        if not pasaporte:
            raise ValueError("necesita pasaporte si o si")

        self.pasaporte = pasaporte

        # aqui guardamos sus reservitas
        self.reservas: List["Reserva"] = []

    def agregar_reserva(self, reserva: "Reserva"):
        # mete una reserva en su cajita
        self.reservas.append(reserva)

    def consultar_reservas(self):
        # devuelve todo lo que tenga guardado
        return self.reservas


class Empleado(Persona):
    # este es el señor o señora que trabaja ahi

    def __init__(self, id_persona: int, nombre: str, email: str, cargo: str):
        super().__init__(id_persona, nombre, email)
        self.cargo = cargo  # su trabajito

    def generar_reporte(self):
        # solo dice que hizo algo jeje
        return f"reporte hecho por {self.nombre}"
    
    def reservas_vuelos(self):
        # esto es para que el empleado pueda ver las reservas de vuelos
        return "aqui van las reservas de vuelos (en construccion)"
    
    def crear_usuario(self, id_persona: int, nombre: str, email: str, tipo: str):
        # esto es para que el empleado pueda crear nuevos usuarios
        return "usuario creado (en construccion)"

## Model - Persona
# RESERVAS VUELOS Y CREA USUSARIOS 

class Hotel:
    # el hotel es como una casa grande con muchos cuartos

    def __init__(self, id_hotel: int, nombre: str, ciudad: str): # FECHAS 
        if not nombre:
            raise ValueError("el hotel necesita nombre")

        self.id_hotel = id_hotel
        self.nombre = nombre
        self.ciudad = ciudad

        # aqui viven las habitaciones
        self.habitaciones: List["Habitacion"] = []

    def agregar_habitacion(self, habitacion: "Habitacion"):
        # metemos un cuarto nuevo
        self.habitaciones.append(habitacion)

    def consultar_disponibilidad(self, fecha_inicio: datetime, fecha_fin: datetime):
        # FECHAS DE DISPONIBILIDAD - HABITACIONES
        disponibles = []
        for h in self.habitaciones:
            if h.esta_disponible(fecha_inicio, fecha_fin):
                disponibles.append(h)
        return disponibles


class Habitacion:
    # esto es un cuartito del hotel

    def __init__(self, numero: int, precio: float): # FECHAS 
        if precio <= 0:
            raise ValueError("no puede valer 0 o menos eso esta mal")

        self.numero = numero
        self.precio = precio
        self.disponible = True  # empieza libre
        self.fechas_reservadas: List[tuple] = []

    def esta_disponible(self, fecha_inicio: datetime, fecha_fin: datetime):
        for inicio, fin in self.fechas_reservadas:
            if (fecha_inicio <= fin and fecha_fin >= inicio):
                return False
        return True

    def reservar(self, fecha_inicio: datetime, fecha_fin: datetime):
        # si ya esta ocupado en esas fechas no se puede otra vez
        if not self.esta_disponible(fecha_inicio, fecha_fin):
            raise Exception("ya esta ocupadooo")

        self.fechas_reservadas.append((fecha_inicio, fecha_fin))
        self.disponible = False

    def liberar(self, fecha_inicio: datetime, fecha_fin: datetime):
        # lo dejamos libre otra ves
        self.fechas_reservadas = [
            (inicio, fin)
            for inicio, fin in self.fechas_reservadas
            if not (inicio == fecha_inicio and fin == fecha_fin)
        ]
        if not self.fechas_reservadas:
            self.disponible = True

# model reserva
class Reserva:
    # la reserva es cuando el turista dice: quiero ese cuarto 

    def __init__(self, id_reserva: int, turista: Turista, habitacion: Habitacion,
                 fecha_inicio: datetime, fecha_fin: datetime, destino: str):# FECHAS - DESTINO 
        if not habitacion.esta_disponible(fecha_inicio, fecha_fin):
            raise Exception("no se puede porque ya esta ocupado")

        self.id_reserva = id_reserva
        self.turista = turista
        self.habitacion = habitacion
        self.destino = destino
        self.fecha = datetime.now()  # guardamos cuando paso
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

        # marcamos el cuarto como ocupado
        habitacion.reservar(fecha_inicio, fecha_fin)

        # y se la damos al turista
        turista.agregar_reserva(self)

    def cancelar(self):
        # si se arrepiente lo soltamos
        self.habitacion.liberar(self.fecha_inicio, self.fecha_fin)

# model sucursal
class Sucursal:
    # esto es como la oficina grande donde estan los hoteles y empleados

    MAX_SUCURSALES = 2  # SUCURSARL 2 SUCUARSALES COMO MUCHO
    total_sucursales = 0

    def __init__(self, id_sucursal: int, nombre: str):
        if Sucursal.total_sucursales >= Sucursal.MAX_SUCURSALES:
            raise Exception("no se pueden crear mas sucursales")

        self.id_sucursal = id_sucursal
        self.nombre = nombre

        self.hoteles: List[Hotel] = []
        self.empleados: List[Empleado] = []

        Sucursal.total_sucursales += 1

    def agregar_hotel(self, hotel: Hotel):
        # guardamos el hotel aqui
        self.hoteles.append(hotel)

    def agregar_empleado(self, empleado: Empleado):
        # guardamos el trabajador aqui tambien
        self.empleados.append(empleado)

    def listar_hoteles(self):
        # muestra todos los hoteles que tiene
        return self.hoteles
    