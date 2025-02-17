import os
import json

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = self.cargar_inventario()
    
    def cargar_inventario(self):
        """Carga los productos desde el archivo de inventario."""
        if not os.path.exists(self.archivo):
            return {}
        try:
            with open(self.archivo, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error al cargar el inventario: {e}")
            return {}
    
    def guardar_inventario(self):
        """Guarda los productos en el archivo de inventario."""
        try:
            with open(self.archivo, "w", encoding="utf-8") as file:
                json.dump(self.productos, file, indent=4)
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
    
    def agregar_producto(self, nombre, cantidad, precio):
        """Agrega un nuevo producto al inventario."""
        if nombre in self.productos:
            print("El producto ya existe. Use actualizar_producto para modificarlo.")
            return
        self.productos[nombre] = {"cantidad": cantidad, "precio": precio}
        self.guardar_inventario()
        print(f"Producto '{nombre}' agregado exitosamente.")
    
    def actualizar_producto(self, nombre, cantidad=None, precio=None):
        """Actualiza la cantidad y/o precio de un producto existente."""
        if nombre not in self.productos:
            print("El producto no existe en el inventario.")
            return
        if cantidad is not None:
            self.productos[nombre]["cantidad"] = cantidad
        if precio is not None:
            self.productos[nombre]["precio"] = precio
        self.guardar_inventario()
        print(f"Producto '{nombre}' actualizado correctamente.")
    
    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        if nombre not in self.productos:
            print("El producto no existe en el inventario.")
            return
        del self.productos[nombre]
        self.guardar_inventario()
        print(f"Producto '{nombre}' eliminado exitosamente.")
    
    def mostrar_inventario(self):
        """Muestra el inventario actual."""
        if not self.productos:
            print("El inventario está vacío.")
            return
        for nombre, info in self.productos.items():
            print(f"{nombre}: Cantidad: {info['cantidad']}, Precio: {info['precio']}")

# Ejemplo de uso
def main():
    inventario = Inventario()
    while True:
        print("\n1. Agregar producto\n2. Actualizar producto\n3. Eliminar producto\n4. Mostrar inventario\n5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(nombre, cantidad, precio)
        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(nombre, cantidad, precio)
        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == "4":
            inventario.mostrar_inventario()
        elif opcion == "5":
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
