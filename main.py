import tkinter as tk

from main_window import setup_main_window, setup_main_canvas

# Constants

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

BGR_IMAGE = "tomato.png"

window = setup_main_window()
bgr_image = tk.PhotoImage(file=BGR_IMAGE)

canvas = setup_main_canvas(bgr_image)
canvas.pack()

window.mainloop()
