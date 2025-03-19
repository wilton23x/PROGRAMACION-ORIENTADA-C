import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

def agregar_tarea():
    fecha = entry_fecha.get_date()  # Obtener la fecha seleccionada
    tarea = entry_tarea.get()  # Obtener la tarea escrita

    # Validar si ambos campos están llenos
    if fecha and tarea:
        # Insertar la tarea en la lista (Treeview)
        tree.insert('', 'end', values=(fecha, tarea))
        entry_tarea.delete(0, tk.END)  # Limpiar campo de tarea después de agregarla
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

def eliminar_tarea():
    seleccionado = tree.selection()  # Obtener la tarea seleccionada
    if seleccionado:
        # Confirmar eliminación de la tarea seleccionada
        if messagebox.askyesno("Confirmación", "¿Desea eliminar la tarea seleccionada?"):
            for item in seleccionado:
                tree.delete(item)
    else:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar")

def marcar_como_completada():
    seleccionado = tree.selection()  # Obtener la tarea seleccionada
    if seleccionado:
        for item in seleccionado:
            # Añadir texto indicando que la tarea ha sido completada
            tarea_actual = tree.item(item, 'values')[1]  # Obtener la tarea
            tree.item(item, values=(tree.item(item, 'values')[0], tarea_actual + " (Completada)"))
    else:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Tareas Pendientes")
root.geometry("500x400")

# Marco de entrada para fecha y tarea
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

# Etiqueta y campo para la fecha
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
entry_fecha = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta y campo para la tarea
tk.Label(frame_entrada, text="Tarea:").grid(row=1, column=0, padx=5, pady=5)
entry_tarea = tk.Entry(frame_entrada)
entry_tarea.grid(row=1, column=1, padx=5, pady=5)

# Botones para acciones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Agregar Tarea", command=agregar_tarea).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Eliminar Tarea Seleccionada", command=eliminar_tarea).grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="Marcar como Completada", command=marcar_como_completada).grid(row=0, column=2, padx=5)
tk.Button(frame_botones, text="Salir", command=root.quit).grid(row=0, column=3, padx=5)

# Marco para la lista de tareas
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

# Configuración de la lista de tareas (Treeview)
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Tarea"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Tarea", text="Tarea")
tree.pack()

# Ejecutar la interfaz gráfica
root.mainloop()