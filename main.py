import tkinter as tk
from tkinter import ttk
from morse.py import Morse_Converter
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
h_size = 200
w_size = 400


def center_window():
    # get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # calculate position x and y coordinates
    x = (screen_width / 2) - (w_size / 2)
    y = (screen_height / 2) - (h_size)
    window.geometry('%dx%d+%d+%d' % (w_size, h_size, x, y))


window = tk.Tk()
window.title("Text to Morse Code Converter")
window.config(bg=YELLOW, height=h_size, width=w_size)
window.resizable(width=False, height=False)
center_window()

# text_label = tk.Label(window, text='Text to Convert', font=(FONT_NAME, 10, 'bold'))
# text_label.grid(row=0, column=0)

# Create Canvas
canvas = tk.Canvas(window, height=h_size, width=w_size, highlightthickness=0)
canvas.pack()

# Background set
img = tk.PhotoImage(file="wallpaper.png")
canvas.create_image(400, 300, image=img)

# draw text
i = canvas.create_text(w_size / 2, 50, text="Morse Converter", font=(FONT_NAME, 30, 'bold'), fill="black")
r = canvas.create_rectangle(canvas.bbox(i), fill="gray")
canvas.tag_lower(r, i)

# Crear caja de texto.
entry = ttk.Entry()
entry = ttk.Entry(justify=tk.LEFT , width= 60)
# Posicionarla en la ventana.
entry.place(x=10, y=h_size/2)
button = ttk.Button(text="Convert to Morse", command=lambda: print(entry.get()))
button.place(x= w_size / 3, y=(h_size-h_size/3))




window.mainloop()
