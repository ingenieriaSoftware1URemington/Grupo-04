## PROYECTO HOTELERIA
# Hecho Por 
Esteban Ocampo - Alexis - Daniel



# 🏨 Sistema de Gestión de Reservas Hoteleras

Este es un sistema de gestión hotelera desarrollado en **Python** que utiliza Programación Orientada a Objetos (POO). Permite administrar hoteles, habitaciones y procesar reservas de turistas mediante una interfaz de línea de comandos.

---

## 🚀 Características Principales

* **Autenticación de Usuarios:** Sistema de inicio de sesión con roles (Administrador y Turista).
* **Gestión de Catálogo:** Visualización de hoteles y habitaciones con precios dinámicos.
* **Motor de Reservas:** Verificación de disponibilidad basada en fechas específicas.
* **Historial Personalizado:** Registro detallado de viajes por usuario.
* **Estructura Modular:** Separación de responsabilidades entre Modelos, Servicios y Lógica Principal.

---

## 📂 Estructura del Proyecto

El proyecto está organizado en carpetas para facilitar su escalabilidad:

* **`models/`**: Contiene las clases `Hotel`, `Habitacion` y `Turista`.
* **`Services/`**: Lógica de negocio (creación de hoteles, validación de disponibilidad y reservas).
* **`main.py`**: Interfaz de usuario y flujo principal del programa.

---

## 🛠️ Instalación y Ejecución

1. Asegúrate de tener instalado **Python 3.x**.
2. Clona o descarga este repositorio.
3. Navega hasta la carpeta raíz del proyecto.
4. Ejecuta el sistema con el siguiente comando:

```bash
python main.py