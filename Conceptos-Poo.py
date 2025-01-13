# Definición de una clase base (Vehiculo)
class Vehiculo:
    """
    Clase base que representa un vehículo genérico.
    Utiliza encapsulación para proteger el atributo 'modelo'.
    """
    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo público
        self._modelo = modelo  # Atributo protegido (encapsulación)

    def encender(self):
        """Método genérico para encender el vehículo."""
        return f"{self.marca} {self._modelo} está encendido."

    def obtener_modelo(self):
        """Método para acceder al atributo protegido '_modelo'."""
        return self._modelo

# Clase derivada (Automovil)
class Automovil(Vehiculo):
    """
    Clase derivada que representa un automóvil.
    Hereda de Vehiculo y añade un atributo específico 'puertas'.
    """
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas  # Atributo específico de Automovil

    def encender(self):
        """Sobrescribe el método 'encender' para especificar detalles de un automóvil."""
        return f"El automóvil {self.marca} {self._modelo} con {self.puertas} puertas está encendido."

# Clase derivada (Motocicleta)
class Motocicleta(Vehiculo):
    """
    Clase derivada que representa una motocicleta.
    Hereda de Vehiculo y añade un atributo específico 'tipo'.
    """
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo  # Atributo específico de Motocicleta

    def encender(self):
        """Sobrescribe el método 'encender' para especificar detalles de una motocicleta."""
        return f"La motocicleta {self.marca} {self._modelo} de tipo {self.tipo} está encendida."

# Clase con encapsulación de atributos
class Bicicleta:
    """
    Clase que representa una bicicleta.
    Utiliza atributos privados para proteger la información.
    """
    def __init__(self, marca, tipo):
        self.__marca = marca  # Atributo privado
        self.__tipo = tipo  # Atributo privado

    def obtener_info(self):
        """Método para obtener la información de la bicicleta."""
        return f"Bicicleta: {self.__marca}, Tipo: {self.__tipo}"

    def modificar_marca(self, marca):
        """Permite modificar el atributo privado '__marca'."""
        self.__marca = marca

    def modificar_atributos(self, marca, tipo):
        """Permite modificar ambos atributos privados '__marca' y '__tipo'."""
        self.__marca = marca
        self.__tipo = tipo

# Demostración de las clases
if __name__ == "__main__":
    # Instancia de la clase base Vehiculo
    vehiculo_generico = Vehiculo("Generico", "Modelo X")
    print(vehiculo_generico.encender())  # Demostración del método encender

    # Instancia de la clase derivada Automovil
    auto = Automovil("Toyota", "Corolla", 4)
    print(auto.encender())  # Demostración de sobrescritura de método

    # Instancia de la clase derivada Motocicleta
    moto = Motocicleta("Yamaha", "YZF-R3", "Deportiva")
    print(moto.encender())  # Demostración de sobrescritura de método

    # Instancia de la clase Bicicleta con encapsulación
    bici = Bicicleta("Trek", "Montaña")
    print(bici.obtener_info())  # Acceso a atributos privados a través de un método

    # Modificación de atributo privado
    bici.modificar_marca("Giant")
    print(bici.obtener_info())  # Confirmación del cambio de atributo privado

    # Modificación de ambos atributos privados
    bici.modificar_atributos("Specialized", "Carrera")
    print(bici.obtener_info())  # Confirmación del cambio de ambos atributos privados
