# Restaurante App

**Nombre:** SHERLYN ANGELICA VARGAS TAPUY
**Asignatura:** Programación
**Actividad:** Estructuras de datos en Python
**Fecha:** 12 de agosto de 2026

## Descripción

Restaurante App es un sistema básico desarrollado en Python para administrar productos y usuarios de un restaurante.

El proyecto utiliza programación orientada a objetos y estructuras de datos de Python para organizar la información del sistema.

## Estructura del proyecto

```text
RESTAURANTE_APP/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
└── README.md
```

## Modelos

### Producto

La clase `Producto` representa un producto del restaurante.

Sus atributos son:

* ID del producto
* Nombre
* Precio
* Categoría

### Usuario

La clase `Usuario` representa de forma general a una persona registrada en el sistema.

Sus atributos son:

* ID del usuario
* Nombre
* Correo electrónico

## Servicio Restaurante

La clase `Restaurante` se encarga de administrar los productos, usuarios y categorías del sistema.

Permite realizar las siguientes operaciones:

* Agregar productos.
* Listar productos.
* Buscar productos.
* Eliminar productos.
* Registrar usuarios.
* Listar usuarios.
* Buscar usuarios.
* Eliminar usuarios.
* Mostrar categorías.

## Estructuras de datos utilizadas

### Lista

Se utiliza una lista para almacenar los productos:

```python
self.productos = []
```

La lista permite guardar varios objetos `Producto`, recorrerlos, buscarlos y eliminarlos.

### Diccionario

Se utiliza un diccionario para almacenar los usuarios:

```python
self.usuarios = {}
```

El ID del usuario funciona como clave y el objeto `Usuario` como valor. Esto facilita la búsqueda de usuarios.

### Tupla

Se utiliza una tupla para almacenar las categorías base:

```python
self.categorias_base = (
    "Entrada",
    "Plato fuerte",
    "Bebida",
    "Postre"
)
```

La tupla permite mantener estos datos sin modificarlos durante la ejecución.

### Conjunto

Se utiliza un conjunto para almacenar las categorías:

```python
self.categorias = set(self.categorias_base)
```

El conjunto evita que una misma categoría aparezca repetida.

## Funcionamiento

Al ejecutar el programa se muestra un menú en la consola.

El usuario puede seleccionar diferentes opciones para administrar los productos y usuarios del restaurante.

## Ejecución

Para ejecutar el programa, abrir una terminal en la carpeta `RESTAURANTE_APP` y utilizar:

```bash
python main.py
```

## Arquitectura

El proyecto mantiene una separación de responsabilidades:

* `modelos/`: contiene las clases `Producto` y `Usuario`.
* `servicios/`: contiene la lógica de administración del restaurante.
* `main.py`: contiene el menú y controla la interacción con el usuario.
* `README.md`: contiene la documentación del proyecto.

## Objetivo

El objetivo del proyecto es aplicar las principales estructuras de datos de Python dentro de un sistema funcional, manteniendo una organización modular y permitiendo futuras ampliaciones del sistema.
# SEMANA-9
