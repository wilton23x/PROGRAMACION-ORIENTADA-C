class Archivo:
    def __init__(self, nombre):
        """
        Constructor de la clase Archivo.
        Este método se ejecuta automáticamente al crear una instancia de la clase.
        Inicializa el nombre del archivo y abre el archivo en modo de escritura.
        :param nombre: Nombre del archivo a manejar.
        """
        self.nombre = nombre
        try:
            self.archivo = open(self.nombre, 'w')
            print(f"[INFO] Archivo '{self.nombre}' abierto correctamente.")
        except OSError as e:
            self.archivo = None
            print(f"[ERROR] No se pudo abrir el archivo: {e}")

    def escribir(self, texto):
        """
        Escribe texto en el archivo si está abierto.
        :param texto: Texto a escribir en el archivo.
        """
        if self.archivo and not self.archivo.closed:
            self.archivo.write(texto + '\n')
            print(f"[INFO] Texto escrito en el archivo: {texto}")
        else:
            print(f"[ERROR] No se puede escribir en el archivo '{self.nombre}'.")

    def cerrar(self):
        """
        Cierra el archivo si está abierto.
        Este método debe llamarse cuando ya no se necesite usar el archivo.
        """
        if self.archivo and not self.archivo.closed:
            self.archivo.close()
            print(f"[INFO] Archivo '{self.nombre}' cerrado correctamente.")

    def __del__(self):
        """
        Destructor de la clase Archivo.
        Este método se ejecuta automáticamente cuando el objeto es eliminado o el programa termina.
        Garantiza que el archivo esté cerrado al eliminar el objeto.
        """
        self.cerrar()

# Demostración de la clase Archivo
if __name__ == "__main__":
    print("[INFO] Creando instancia de la clase Archivo.")
    archivo = Archivo("mi_archivo.txt")  # Constructor __init__

    if archivo.archivo:  # Verifica que el archivo se haya abierto correctamente
        archivo.escribir("Primera línea del archivo.")  # Escribe una línea en el archivo
        archivo.escribir("Segunda línea del archivo.")  # Escribe otra línea en el archivo

        archivo.cerrar()  # Cierra el archivo de manera explícita

    print("[INFO] Fin del programa. Al finalizar, el destructor (__del__) se asegura de liberar recursos automáticamente.")
