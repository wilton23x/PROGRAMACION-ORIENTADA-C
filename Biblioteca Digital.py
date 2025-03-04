# Clase Libro: Representa un libro con atributos como título, autor, categoría y ISBN.
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = tuple(autor)  # Autor como tupla (nombre, apellido).
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.titulo}' de {self.autor[0]} {self.autor[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"

# Clase Usuario: Representa un usuario con atributos como nombre, ID de usuario y libros prestados.
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados.

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros Prestados: {[libro.titulo for libro in self.libros_prestados]}"

# Clase Biblioteca: Gestiona la colección de libros, usuarios y préstamos.
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario de libros con el ISBN como clave.
        self.usuarios = set()  # Conjunto de usuarios registrados.

    def agregar_libro(self, libro):
        """Añadir un libro a la biblioteca."""
        if libro.isbn in self.libros:
            print("El libro ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido con éxito.")

    def quitar_libro(self, isbn):
        """Eliminar un libro de la biblioteca."""
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        """Registrar un nuevo usuario."""
        if usuario.id_usuario in [u.id_usuario for u in self.usuarios]:
            print("El usuario ya está registrado.")
        else:
            self.usuarios.add(usuario)
            print(f"Usuario {usuario.nombre} registrado con éxito.")

    def dar_baja_usuario(self, id_usuario):
        """Dar de baja un usuario de la biblioteca."""
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            self.usuarios.remove(usuario)
            print(f"Usuario {usuario.nombre} dado de baja.")
        else:
            print("El usuario no existe.")

    def prestar_libro(self, isbn, id_usuario):
        """Prestar un libro a un usuario."""
        if isbn in self.libros:
            libro = self.libros[isbn]
            usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
            if usuario:
                if libro not in usuario.libros_prestados:
                    usuario.libros_prestados.append(libro)
                    print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
                else:
                    print(f"El usuario ya tiene prestado el libro '{libro.titulo}'.")
            else:
                print("Usuario no encontrado.")
        else:
            print("El libro no está disponible en la biblioteca.")

    def devolver_libro(self, isbn, id_usuario):
        """Devolver un libro prestado."""
        libro = next((libro for libro in self.libros.values() if libro.isbn == isbn), None)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if libro and usuario:
            if libro in usuario.libros_prestados:
                usuario.libros_prestados.remove(libro)
                print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
            else:
                print("Este libro no está prestado al usuario.")
        else:
            print("Libro o usuario no encontrado.")

    def buscar_libro(self, termino):
        """Buscar libros por título, autor o categoría."""
        resultados = []
        for libro in self.libros.values():
            if termino.lower() in libro.titulo.lower() or termino.lower() in libro.categoria.lower() or termino.lower() in ' '.join(libro.autor).lower():
                resultados.append(libro)
        if resultados:
            print("Resultados de búsqueda:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron resultados.")

    def listar_libros_prestados(self, id_usuario):
        """Listar los libros prestados a un usuario."""
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(libro)
        else:
            print("Usuario no encontrado.")

# Función para mostrar el menú y ejecutar las opciones
def mostrar_menu():
    print("\n--- Menú de Biblioteca ---")
    print("1. Agregar Libro")
    print("2. Eliminar Libro")
    print("3. Registrar Usuario")
    print("4. Dar Baja Usuario")
    print("5. Prestar Libro")
    print("6. Devolver Libro")
    print("7. Buscar Libro")
    print("8. Listar Libros Prestados")
    print("9. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

# Función principal para interactuar con el sistema
def ejecutar_sistema():
    biblioteca = Biblioteca()

    # Agregar libros predefinidos
    libro1 = Libro("Cien Años de Soledad", ("Gabriel", "García Márquez"), "Ficción", "978-3-16-148410-0")
    libro2 = Libro("El Principito", ("Antoine", "de Saint-Exupéry"), "Infantil", "978-3-16-148411-7")
    libro3 = Libro("1984", ("George", "Orwell"), "Distopía", "978-0-452-28423-4")
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Crear usuarios predefinidos
    usuario1 = Usuario("Juan Pérez", "U001")
    usuario2 = Usuario("Ana García", "U002")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':  # Agregar libro
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el nombre del autor: ").split()
            categoria = input("Ingrese la categoría del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)

        elif opcion == '2':  # Eliminar libro
            isbn = input("Ingrese el ISBN del libro a eliminar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == '3':  # Registrar usuario
            nombre = input("Ingrese el nombre del usuario: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == '4':  # Dar baja usuario
            id_usuario = input("Ingrese el ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == '5':  # Prestar libro
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            biblioteca.prestar_libro(isbn, id_usuario)

        elif opcion == '6':  # Devolver libro
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            biblioteca.devolver_libro(isbn, id_usuario)

        elif opcion == '7':  # Buscar libro
            termino = input("Ingrese el título, autor o categoría del libro a buscar: ")
            biblioteca.buscar_libro(termino)

        elif opcion == '8':  # Listar libros prestados
            id_usuario = input("Ingrese el ID del usuario para listar los libros prestados: ")
            biblioteca.listar_libros_prestados(id_usuario)

        elif opcion == '9':  # Salir
            print("Gracias por usar el sistema de gestión de biblioteca digital.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Ejecutar el sistema
ejecutar_sistema()
