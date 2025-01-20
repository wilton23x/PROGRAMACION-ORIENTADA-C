class Archivo:
    # Constructor (__init__) para inicializar el objeto
    def __init__(self, nombre_archivo):
        """
        Inicializa el objeto Archivo con el nombre del archivo proporcionado.
        Intenta abrir el archivo en modo de escritura.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = None
        try:
            self.archivo = open(self.nombre_archivo, 'w')  # Intentamos abrir el archivo en modo de escritura
            print(f"Archivo '{self.nombre_archivo}' abierto exitosamente.")
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")

    # Destructor (__del__) para cerrar el archivo si está abierto
    def __del__(self):
        """
        Destructor que se activa cuando el objeto Archivo es destruido.
        Cierra el archivo si está abierto.
        """
        if self.archivo:
            try:
                self.archivo.close()
                print(f"Archivo '{self.nombre_archivo}' cerrado exitosamente.")
            except Exception as e:
                print(f"Error al cerrar el archivo: {e}")
    
    # Método para escribir en el archivo
    def escribir(self, contenido):
        """
        Escribe el contenido proporcionado en el archivo abierto.
        """
        if self.archivo:
            try:
                self.archivo.write(contenido)
                print("Contenido escrito en el archivo.")
            except Exception as e:
                print(f"Error al escribir en el archivo: {e}")
        else:
            print("No se puede escribir, el archivo no está abierto.")

# Ejemplo de uso de la clase
def main():
    # Crear un objeto de la clase Archivo
    archivo = Archivo("ejemplo.txt")
    
    # Escribir contenido en el archivo
    archivo.escribir("Este es un ejemplo de archivo.")
    
    # El archivo se cerrará automáticamente cuando el objeto sea destruido
    del archivo  # Eliminamos el objeto explícitamente, lo que activa el destructor

# Llamamos a la función principal
if __name__ == "__main__":
    main()
