import pickle

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
    
class Inventario:
    def __init__(self):
        self.productos = {}
    
    def agregar_producto(self, producto):
        self.productos[producto.id_producto] = producto
    
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")
    
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")
    
    def buscar_producto(self, nombre):
        encontrados = [p.__dict__ for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        return encontrados if encontrados else "Producto no encontrado."
    
    def mostrar_productos(self):
        return [p.__dict__ for p in self.productos.values()]
    
    def guardar_en_archivo(self, archivo):
        with open(archivo, 'wb') as f:
            pickle.dump(self.productos, f)
    
    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'rb') as f:
                self.productos = pickle.load(f)
        except (FileNotFoundError, EOFError):
            print("Archivo no encontrado o vacío, iniciando inventario vacío.")

def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo("inventario.pkl")
    while True:
        print("\nMenú de Inventario:")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Guardar y salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deje vacío para no cambiar): ")
            precio = input("Nuevo precio (deje vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            print(inventario.buscar_producto(nombre))
        elif opcion == "5":
            print(inventario.mostrar_productos())
        elif opcion == "6":
            inventario.guardar_en_archivo("inventario.pkl")
            print("Inventario guardado. Saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
