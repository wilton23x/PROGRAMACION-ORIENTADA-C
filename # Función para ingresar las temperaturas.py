# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for dia in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
        temperaturas.append(temperatura)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    print("Bienvenido al programa de cálculo del promedio semanal del clima.")
    temperaturas = ingresar_temperaturas()  # Ingresar las temperaturas de la semana
    promedio = calcular_promedio(temperaturas)  # Calcular el promedio
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")

# Llamar a la función principal
if __name__ == "__main__":
    main()
