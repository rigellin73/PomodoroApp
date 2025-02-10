import tkinter as tk

from main_window import setup_main_window, setup_main_canvas

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

BGR_IMAGE = "tomato.png"

window = setup_main_window()
bgr_image = tk.PhotoImage(file=BGR_IMAGE)

canvas = setup_main_canvas(bgr_image)
canvas.pack()

window.mainloop()
