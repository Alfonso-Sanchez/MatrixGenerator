import tkinter as tk

# Tamaño de la matriz
MATRIX_SIZE = 8

# Función para inicializar la matriz (todos los valores en 0x00)
def initialize_matrix():
    return [[0x00 for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]

# Función para actualizar la matriz visual cuando se hace clic
def update_visual_matrix(event):
    x = event.x // CELL_SIZE
    y = event.y // CELL_SIZE
    if 0 <= x < MATRIX_SIZE and 0 <= y < MATRIX_SIZE:
        # Cambiar el valor de la celda (0x00 -> 0xFF o 0xFF -> 0x00)
        matrix[y][x] = 0xFF if matrix[y][x] == 0x00 else 0x00
        # Actualizar la ventana visual
        update_visual_window()
        # Actualizar la ventana de texto
        update_text_window()

# Función para actualizar la ventana visual
def update_visual_window():
    for y in range(MATRIX_SIZE):
        for x in range(MATRIX_SIZE):
            color = "white" if matrix[y][x] == 0xFF else "black"
            canvas.create_rectangle(
                x * CELL_SIZE, y * CELL_SIZE,
                (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                fill=color, outline="gray"
            )

# Función para actualizar la ventana de texto
def update_text_window():
    text_matrix.delete(1.0, tk.END)
    for row in matrix:
        hex_row = ", ".join(f"0x{cell:02X}" for cell in row)
        text_matrix.insert(tk.END, hex_row + "\n")

# Función para copiar la matriz al portapapeles
def copy_matrix():
    root.clipboard_clear()
    hex_matrix = ",\n".join(", ".join(f"0x{cell:02X}" for cell in row) for row in matrix)
    root.clipboard_append("{" + hex_matrix + "}")

# Función para pegar una matriz desde el portapapeles
def paste_matrix():
    try:
        clipboard_data = root.clipboard_get().strip()
        clipboard_data = clipboard_data.replace("{", "").replace("}", "").replace("\n", "").replace(" ", "")
        rows = clipboard_data.split(",")
        for y in range(MATRIX_SIZE):
            for x in range(MATRIX_SIZE):
                value = rows[y * MATRIX_SIZE + x].strip()
                matrix[y][x] = int(value, 16)
        update_visual_window()
        update_text_window()
    except Exception as e:
        print("Error al pegar la matriz:", e)

# Inicializar la matriz
matrix = initialize_matrix()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Editor de Matriz 8x8")

# Tamaño de cada celda en la ventana visual
CELL_SIZE = 40

# Ventana 1: Matriz en formato hexadecimal
frame_text = tk.Frame(root)
frame_text.pack(side=tk.LEFT, padx=10, pady=10)

label_text = tk.Label(frame_text, text="Matriz Hexadecimal")
label_text.pack()

text_matrix = tk.Text(frame_text, width=30, height=10)
text_matrix.pack()

button_copy = tk.Button(frame_text, text="Copiar Matriz", command=copy_matrix)
button_copy.pack(pady=5)

button_paste = tk.Button(frame_text, text="Pegar Matriz", command=paste_matrix)
button_paste.pack(pady=5)

# Ventana 2: Matriz visual
frame_visual = tk.Frame(root)
frame_visual.pack(side=tk.LEFT, padx=10, pady=10)

label_visual = tk.Label(frame_visual, text="Matriz Visual")
label_visual.pack()

canvas = tk.Canvas(frame_visual, width=CELL_SIZE * MATRIX_SIZE, height=CELL_SIZE * MATRIX_SIZE)
canvas.pack()
canvas.bind("<Button-1>", update_visual_matrix)

# Inicializar las ventanas
update_visual_window()
update_text_window()

# Ejecutar la aplicación
root.mainloop()