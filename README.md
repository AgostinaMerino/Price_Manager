# Price Manager - Sprint 2

## Objetivo

El objetivo principal del proyecto es aplicar los conocimientos
adquiridos sobre:

- Programación Orientada a Objetos
- Persistencia de datos
- SQLAlchemy ORM
- Bases de datos relacionales
- Consumo de APIs externas
- Arquitectura modular
- Control de versiones con Git y GitHub

---

## Introducción

La empresa necesita un sistema moderno para la gestión de inventario
de productos electrónicos.

El sistema permite administrar:

- Productos
- Categorías
- Proveedores
- Stock
- Monedas
- Cotizaciones del dólar

Además, permite:

- Persistencia en SQLite mediante SQLAlchemy
- Migración de datos desde CSV
- Consulta de cotizaciones desde API externa
- Exportación de información a CSV
- Gestión mediante interfaz de consola (CLI)

---

## Tecnologías utilizadas

- Python 3
- SQLAlchemy
- SQLite
- Requests
- dotenv
- Git
- GitHub

---

## Sprint actual

Sprint 2

---

## Funcionalidades implementadas

### CRUD completo
- Categorías
- Proveedores
- Monedas
- Tipos de cotización
- Productos
- Stock
- Cotizaciones

### Persistencia
- Base de datos SQLite
- ORM SQLAlchemy
- Migraciones SQL

### API externa
- Consulta automática de cotizaciones del dólar

### Exportaciones
- Exportación de productos a CSV

### Consola
- Menú interactivo CLI

---

## Consideraciones

Para simplificar el alcance del Sprint 2 y mantener compatibilidad
con el Sprint 1, el sistema modela un único stock por producto,
sin contemplar múltiples almacenes físicos.
