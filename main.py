import tkinter as tk
from tkinter import ttk

from morse import *

WHITE = "#ffffff"
BLACK = "#000000"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
h_size = 200
w_size = 400


def call_conversor(text):
    morse_code = morse_converter(text)
    morse_output.config(text=morse_code)


def center_window():
    # get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # calculate position x and y coordinates
    x = (screen_width / 2) - (w_size / 2)
    y = (screen_height / 2) - h_size
    window.geometry('%dx%d+%d+%d' % (w_size, h_size, x, y))


#Create windows
window = tk.Tk()
window.title("Text to Morse Code Converter")
window.config(bg=YELLOW, height=h_size, width=w_size)
center_window()

#Create Canvas
canvas = tk.Canvas(window, height=h_size, width=w_size, highlightthickness=0)
canvas.pack()

#Background set
img = tk.PhotoImage(file="wallpaper.png")
canvas.create_image(w_size, h_size, image=img)

#Draw Tittle
i = canvas.create_text(w_size / 2, 50, text="Morse Converter", font=(FONT_NAME, 30, 'bold'), fill=BLACK)
r = canvas.create_rectangle(canvas.bbox(i), fill=GREEN)
canvas.tag_lower(r, i)

#Entry box
entry = ttk.Entry(justify=tk.LEFT, width=60)
entry.place(x=10, y=h_size / 2)

#Button
button = ttk.Button(text="Convert to Morse", command=lambda: call_conversor(entry.get()))
window.bind('<Return>', lambda event: call_conversor(entry.get()))
button.place(x=w_size / 3, y=(h_size - h_size / 3))

#Output
morse_output = tk.Label(text='', font=(FONT_NAME, 10, 'bold'))
morse_output.place(x=10, y=h_size - 25)

window.mainloop()
