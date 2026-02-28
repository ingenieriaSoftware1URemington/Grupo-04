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


class Hotel:
    # el hotel es como una casa grande con muchos cuartos

    def __init__(self, id_hotel: int, nombre: str, ciudad: str):
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

    def consultar_disponibilidad(self):
        # mira cuales cuartos estan libres
        return [h for h in self.habitaciones if h.disponible]


class Habitacion:
    # esto es un cuartito del hotel

    def __init__(self, numero: int, precio: float):
        if precio <= 0:
            raise ValueError("no puede valer 0 o menos eso esta mal")

        self.numero = numero
        self.precio = precio
        self.disponible = True  # empieza libre

    def reservar(self):
        # si ya esta ocupado no se puede otra vez
        if not self.disponible:
            raise Exception("ya esta ocupadooo")

        self.disponible = False

    def liberar(self):
        # lo dejamos libre otra ves
        self.disponible = True


class Reserva:
    # la reserva es cuando el turista dice: quiero ese cuarto 

    def __init__(self, id_reserva: int, turista: Turista, habitacion: Habitacion):
        if not habitacion.disponible:
            raise Exception("no se puede porque ya esta ocupado")

        self.id_reserva = id_reserva
        self.turista = turista
        self.habitacion = habitacion
        self.fecha = datetime.now()  # guardamos cuando paso

        # marcamos el cuarto como ocupado
        habitacion.reservar()

        # y se la damos al turista
        turista.agregar_reserva(self)

    def cancelar(self):
        # si se arrepiente lo soltamos
        self.habitacion.liberar()


class Sucursal:
    # esto es como la oficina grande donde estan los hoteles y empleados

    def __init__(self, id_sucursal: int, nombre: str):
        self.id_sucursal = id_sucursal
        self.nombre = nombre

        self.hoteles: List[Hotel] = []
        self.empleados: List[Empleado] = []

    def agregar_hotel(self, hotel: Hotel):
        # guardamos el hotel aqui
        self.hoteles.append(hotel)

    def agregar_empleado(self, empleado: Empleado):
        # guardamos el trabajador aqui tambien
        self.empleados.append(empleado)

    def listar_hoteles(self):
        # muestra todos los hoteles que tiene
        return self.hoteles