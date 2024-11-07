import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("¡Hola Mundo!")

# Crear el widget de etiqueta
label = tk.Label(root, text="¡Hola Mundo!", font=("Arial", 24))
label.pack(pady=20)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
