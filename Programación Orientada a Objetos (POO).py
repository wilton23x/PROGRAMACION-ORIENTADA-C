# Clase para representar la información del clima diario
class ClimaDiario:
    def __init__(self):
        self.temperaturas = []  # Lista para almacenar las temperaturas

    # Método para ingresar las temperaturas de la semana
    def ingresar_temperaturas(self):
        for dia in range(7):
            temperatura = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
            self.temperaturas.append(temperatura)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Función principal
def main():
    print("Bienvenido al programa de cálculo del promedio semanal del clima.")
    clima = ClimaDiario()  # Crear una instancia de la clase ClimaDiario
    clima.ingresar_temperaturas()  # Ingresar las temperaturas de la semana
    promedio = clima.calcular_promedio()  # Calcular el promedio semanal
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")

# Llamar a la función principal
if __name__ == "__main__":
    main()
