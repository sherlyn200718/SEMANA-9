from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


def main():
    restaurante = Restaurante()

    while True:
        print("\n===== RESTAURANTE APP =====")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Registrar usuario")
        print("6. Listar usuarios")
        print("7. Buscar usuario")
        print("8. Eliminar usuario")
        print("9. Mostrar categorias")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            try:
                id_producto = int(input("ID del producto: "))
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                categoria = input("Categoria: ")

                producto = Producto(
                    id_producto,
                    nombre,
                    precio,
                    categoria
                )

                if restaurante.agregar_producto(producto):
                    print("Producto agregado correctamente.")
                else:
                    print("Ya existe un producto con ese ID.")

            except ValueError:
                print("Error: ingrese correctamente los datos.")

        elif opcion == "2":
            productos = restaurante.listar_productos()

            if len(productos) == 0:
                print("No hay productos registrados.")
            else:
                for producto in productos:
                    print(producto)

        elif opcion == "3":
            try:
                id_producto = int(input("ID del producto: "))
                producto = restaurante.buscar_producto(id_producto)

                if producto is not None:
                    print(producto)
                else:
                    print("Producto no encontrado.")

            except ValueError:
                print("El ID debe ser un numero entero.")

        elif opcion == "4":
            try:
                id_producto = int(input("ID del producto: "))

                if restaurante.eliminar_producto(id_producto):
                    print("Producto eliminado correctamente.")
                else:
                    print("Producto no encontrado.")

            except ValueError:
                print("El ID debe ser un numero entero.")

        elif opcion == "5":
            try:
                id_usuario = int(input("ID del usuario: "))
                nombre = input("Nombre: ")
                correo = input("Correo: ")

                usuario = Usuario(
                    id_usuario,
                    nombre,
                    correo
                )

                if restaurante.agregar_usuario(usuario):
                    print("Usuario registrado correctamente.")
                else:
                    print("Ya existe un usuario con ese ID.")

            except ValueError:
                print("El ID debe ser un numero entero.")

        elif opcion == "6":
            usuarios = restaurante.listar_usuarios()

            if len(restaurante.usuarios) == 0:
                print("No hay usuarios registrados.")
            else:
                for usuario in usuarios:
                    print(usuario)

        elif opcion == "7":
            try:
                id_usuario = int(input("ID del usuario: "))
                usuario = restaurante.buscar_usuario(id_usuario)

                if usuario is not None:
                    print(usuario)
                else:
                    print("Usuario no encontrado.")

            except ValueError:
                print("El ID debe ser un numero entero.")

        elif opcion == "8":
            try:
                id_usuario = int(input("ID del usuario: "))

                if restaurante.eliminar_usuario(id_usuario):
                    print("Usuario eliminado correctamente.")
                else:
                    print("Usuario no encontrado.")

            except ValueError:
                print("El ID debe ser un numero entero.")

        elif opcion == "9":
            categorias = restaurante.listar_categorias()

            print("\nCategorias disponibles:")
            for categoria in categorias:
                print("-", categoria)

        elif opcion == "0":
            print("Gracias por utilizar Restaurante App.")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()