class Producto:
    def __init__(self, id_producto, nombre, precio, categoria):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def __str__(self):
        return (
            f"ID: {self.id_producto} | "
            f"Nombre: {self.nombre} | "
            f"Precio: ${self.precio:.2f} | "
            f"Categoria: {self.categoria}"
        )