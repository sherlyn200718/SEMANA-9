class Restaurante:
    def __init__(self):
        # Lista para almacenar productos
        self.productos = []

        # Diccionario para almacenar usuarios
        self.usuarios = {}

        # Tupla para las categorias base
        self.categorias_base = (
            "Entrada",
            "Plato fuerte",
            "Bebida",
            "Postre"
        )

        # Conjunto para evitar categorias repetidas
        self.categorias = set(self.categorias_base)

    # PRODUCTOS

    def agregar_producto(self, producto):
        for producto_existente in self.productos:
            if producto_existente.id_producto == producto.id_producto:
                return False

        self.productos.append(producto)
        self.categorias.add(producto.categoria)
        return True

    def listar_productos(self):
        return self.productos

    def buscar_producto(self, id_producto):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                return producto

        return None

    def eliminar_producto(self, id_producto):
        producto = self.buscar_producto(id_producto)

        if producto is not None:
            self.productos.remove(producto)
            return True

        return False

    # USUARIOS

    def agregar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            return False

        self.usuarios[usuario.id_usuario] = usuario
        return True

    def listar_usuarios(self):
        return self.usuarios.values()

    def buscar_usuario(self, id_usuario):
        return self.usuarios.get(id_usuario)

    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            return True

        return False

    # CATEGORIAS

    def listar_categorias(self):
        return sorted(self.categorias)