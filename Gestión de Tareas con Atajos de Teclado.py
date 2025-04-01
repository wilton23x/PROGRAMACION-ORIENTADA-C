import tkinter as tk
from tkinter import messagebox

def agregar_tarea(event=None):
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

def marcar_completada(event=None):
    try:
        indice = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(indice)
        if not tarea.startswith("✔ "):
            lista_tareas.delete(indice)
            lista_tareas.insert(indice, "✔ " + tarea)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

def eliminar_tarea(event=None):
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

def cerrar_app(event=None):
    root.quit()

# Configuración de la ventana
root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("400x400")

# Campo de entrada y botón para agregar
entrada_tarea = tk.Entry(root, width=50)
entrada_tarea.pack(pady=10)
entrada_tarea.bind("<Return>", agregar_tarea)

btn_agregar = tk.Button(root, text="Agregar Tarea", command=agregar_tarea)
btn_agregar.pack()

# Lista de tareas
lista_tareas = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
lista_tareas.pack(pady=10)

# Botones para completar y eliminar tareas
btn_completar = tk.Button(root, text="Marcar Completada", command=marcar_completada)
btn_completar.pack()
btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack()

# Asociación de atajos de teclado
root.bind("<c>", marcar_completada)
root.bind("<C>", marcar_completada)
root.bind("<d>", eliminar_tarea)
root.bind("<D>", eliminar_tarea)
root.bind("<Delete>", eliminar_tarea)
root.bind("<Escape>", cerrar_app)

# Ejecutar la aplicación
root.mainloop()

root.mainloop()
