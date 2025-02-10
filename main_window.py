import tkinter as tk
from colors import YELLOW

W_TITLE = "Pomodoro"
W_PADX = 100
W_PADY = 50

C_WIDTH = 200
C_HEIGHT = 224

T_POSX = C_WIDTH / 2
T_POSY = C_HEIGHT / 2 + 18
T_TEXT = "00:00"
T_COLOR = "white"
T_FONT = ("Courier", 35, "bold")

def setup_main_window():
    main_window = tk.Tk()
    main_window.title(W_TITLE)
    main_window.config(padx=W_PADX, pady=W_PADY, bg=YELLOW)
    return main_window

def setup_main_canvas(bgr_image):
    main_canvas = tk.Canvas(width=C_WIDTH, height=C_HEIGHT, bg=YELLOW, highlightthickness=0)
    main_canvas.create_image(C_WIDTH / 2, C_HEIGHT / 2, image=bgr_image)
    return main_canvas

def setup_timer_text(canvas):
    return canvas.create_text(T_POSX, T_POSY, text=T_TEXT, fill=T_COLOR, font=T_FONT)
