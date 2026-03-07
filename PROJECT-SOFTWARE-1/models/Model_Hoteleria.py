from datetime import datetime
from typing import List


#cualquier persona del sistema
class Persona:

    def __init__(self, id_persona: int, nombre: str, email: str):

        # revisa que el nombre exista
        if not nombre:
            raise ValueError("no puede estar vacio el nombre")

        # guardamos datos de la persona
        self.id_persona = id_persona
        self.nombre = nombre
        self.email = email

    # para imprimir bonito
    def __str__(self):
        return f"{self.nombre} ({self.email})"

# Turista = persona que viaja
class Turista(Persona):

    def __init__(self, id_persona: int, nombre: str, email: str, pasaporte: str):

        # usa lo de persona
        super().__init__(id_persona, nombre, email)

        # necesita pasaporte
        if not pasaporte:
            raise ValueError("necesita pasaporte")

        self.pasaporte = pasaporte

        # caja donde guarda sus reservas
        self.reservas: List["Reserva"] = []

    # guarda una reserva
    def agregar_reserva(self, reserva: "Reserva"):
        self.reservas.append(reserva)

    # muestra reservas
    def consultar_reservas(self):
        return self.reservas


#  clase hotel con habitaciones
class Hotel:
    def __init__(self, id_hotel: int, nombre: str, ciudad: str):
        if not nombre:
            raise ValueError("el hotel necesita nombre")

        self.id_hotel = id_hotel
        self.nombre = nombre
        self.ciudad = ciudad

        # lista de habitaciones
        self.habitaciones: List["Habitacion"] = []

    # agrega una habitación
    def agregar_habitacion(self, habitacion: "Habitacion"):
        self.habitaciones.append(habitacion)

    # mira habitaciones libres
    def consultar_disponibilidad(self, fecha_inicio: datetime, fecha_fin: datetime):

        disponibles = []
        for h in self.habitaciones:
            if h.esta_disponible(fecha_inicio, fecha_fin):
                disponibles.append(h)
        return disponibles


# Habitacion = cuarto del hotel
class Habitacion:
    def __init__(self, numero: int, precio: float):
        # revisa que el precio sea valido
        if precio <= 0:
            raise ValueError("no puede valer 0")

        self.numero = numero
        self.precio = precio

        # empieza libre
        self.disponible = True

        # guarda fechas ocupadas
        self.fechas_reservadas: List[tuple] = []

    # mira si la habitación está libre
    def esta_disponible(self, fecha_inicio: datetime, fecha_fin: datetime):

        for inicio, fin in self.fechas_reservadas:

            if fecha_inicio <= fin and fecha_fin >= inicio:
                return False
        return True

    # reserva la habitación
    def reservar(self, fecha_inicio: datetime, fecha_fin: datetime):
        if not self.esta_disponible(fecha_inicio, fecha_fin):
            raise Exception("ya esta ocupado")
        self.fechas_reservadas.append((fecha_inicio, fecha_fin))
        self.disponible = False

    # libera la habitación
    def liberar(self, fecha_inicio: datetime, fecha_fin: datetime):
        self.fechas_reservadas = [
            (inicio, fin)
            for inicio, fin in self.fechas_reservadas
            if not (inicio == fecha_inicio and fin == fecha_fin)

        ]

        if not self.fechas_reservadas:
            self.disponible = True


# hace una reserva cuando alguien aparta una habitación
class Reserva:

    def __init__(self, id_reserva: int, turista: Turista, habitacion: Habitacion,
                 fecha_inicio: datetime, fecha_fin: datetime, destino: str):
        # revisa si está libre
        if not habitacion.esta_disponible(fecha_inicio, fecha_fin):
            raise Exception("habitacion ocupada")
        # datos de la reserva
        self.id_reserva = id_reserva
        self.turista = turista
        self.habitacion = habitacion
        self.destino = destino
        # guarda fecha actual
        self.fecha = datetime.now()

        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

        # marca habitación como reservada
        habitacion.reservar(fecha_inicio, fecha_fin)

        # guarda reserva en el turista
        turista.agregar_reserva(self)

    # cancelar reserva
    def cancelar(self):
        self.habitacion.liberar(self.fecha_inicio, self.fecha_fin)


class Sucursal:
    # esto es como la oficina grande donde estan los hoteles

    MAX_SUCURSALES = 2  # SUCURSARL 2 SUCUARSALES COMO MUCHO
    total_sucursales = 0

    def __init__(self, id_sucursal: int, nombre: str):
        if Sucursal.total_sucursales >= Sucursal.MAX_SUCURSALES:
            raise Exception("no se pueden crear mas sucursales")
        self.id_sucursal = id_sucursal
        self.nombre = nombre
        self.hoteles: List[Hotel] = []
        Sucursal.total_sucursales += 1

    def agregar_hotel(self, hotel: Hotel):
        # guardamos el hotel aqui
        self.hoteles.append(hotel)

    def listar_hoteles(self):
        # muestra todos los hoteles que tiene
        return self.hoteles
    