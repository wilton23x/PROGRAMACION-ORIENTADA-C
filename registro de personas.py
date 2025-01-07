   # Programa para gestionar un registro de personas con nombre, edad y si son estudiantes.
# Utiliza tipos de datos como strings, enteros y booleanos.

def agregar_persona(nombre, edad, es_estudiante):
    """Función para agregar una persona al registro."""
    persona = {
        "nombre": nombre,
        "edad": edad,
        "es_estudiante": es_estudiante
    }
    return persona

def mostrar_persona(persona):
    """Función para mostrar los detalles de una persona."""
    print(f"Nombre: {persona['nombre']}")
    print(f"Edad: {persona['edad']}")
    print(f"Es estudiante: {'Sí' if persona['es_estudiante'] else 'No'}")

def main():
    """Función principal para interactuar con el usuario y gestionar el registro."""
    print("Bienvenido al registro de personas")

    # Solicitar los datos al usuario
    nombre = input("Ingresa el nombre de la persona: ")
    edad = int(input("Ingresa la edad de la persona: "))
    es_estudiante = input("¿Es estudiante? (sí/no): ").lower() == "sí"

    # Agregar persona al registro
    persona = agregar_persona(nombre, edad, es_estudiante)

    # Mostrar la información de la persona registrada
    print("\nPersona registrada:")
    mostrar_persona(persona)

if __name__ == "__main__":
    main()
