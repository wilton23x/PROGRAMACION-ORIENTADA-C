# Ejemplo de un sistema de gestión de tienda utilizando POO

class Producto:
    """Clase que representa un producto en la tienda."""
    
    def __init__(self, nombre, precio, cantidad_en_stock):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_en_stock = cantidad_en_stock

    def __str__(self):
        return f"{self.nombre} - ${self.precio} (Stock: {self.cantidad_en_stock})"

    def actualizar_stock(self, cantidad_vendida):
        """Actualiza la cantidad en stock del producto."""
        if cantidad_vendida <= self.cantidad_en_stock:
            self.cantidad_en_stock -= cantidad_vendida
        else:
            print(f"No hay suficiente stock de {self.nombre}.")

class Carrito:
    """Clase que representa el carrito de compras de un cliente."""
    
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        """Agrega un producto al carrito."""
        if cantidad <= producto.cantidad_en_stock:
            self.productos.append({"producto": producto, "cantidad": cantidad})
            producto.actualizar_stock(cantidad)
        else:
            print(f"No se puede agregar {cantidad} unidades de {producto.nombre}. Stock insuficiente.")

    def calcular_total(self):
        """Calcula el total de la compra."""
        total = sum(item["producto"].precio * item["cantidad"] for item in self.productos)
        return total

    def mostrar_contenido(self):
        """Muestra el contenido del carrito."""
        for item in self.productos:
            print(f"{item['producto'].nombre}: {item['cantidad']} x ${item['producto'].precio}")

class Cliente:
    """Clase que representa un cliente de la tienda."""
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = Carrito()

    def realizar_compra(self):
        """Muestra el total de la compra del cliente."""
        total = self.carrito.calcular_total()
        print(f"\n{self.nombre} ha comprado los siguientes productos:")
        self.carrito.mostrar_contenido()
        print(f"Total a pagar: ${total:.2f}")

class Tienda:
    """Clase que representa la tienda y sus productos."""
    
    def __init__(self):
        self.productos_disponibles = []

    def agregar_producto(self, producto):
        """Agrega un producto a la tienda."""
        self.productos_disponibles.append(producto)

    def mostrar_productos(self):
        """Muestra todos los productos disponibles en la tienda."""
        print("Productos disponibles en la tienda:")
        for producto in self.productos_disponibles:
            print(producto)

# Crear una tienda y algunos productos
tienda = Tienda()
producto1 = Producto("Camiseta", 20.0, 50)
producto2 = Producto("Jeans", 35.0, 30)
producto3 = Producto("Zapatos", 50.0, 20)

# Agregar productos a la tienda
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)

# Mostrar los productos disponibles
tienda.mostrar_productos()

# Crear un cliente y realizar una compra
cliente = Cliente("Wilton Salazar")
cliente.carrito.agregar_producto(producto1, 2)  # Comprar 2 camisetas
cliente.carrito.agregar_producto(producto2, 1)  # Comprar 1 jeans
cliente.realizar_compra()
