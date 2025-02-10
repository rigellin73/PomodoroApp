import tkinter as tk

W_TITLE = "Pomodoro"
C_WIDTH = 200
C_HEIGHT = 224

def setup_main_window():
    main_window = tk.Tk()
    main_window.title(W_TITLE)
    return main_window

def setup_main_canvas(bgr_image):
    main_canvas = tk.Canvas(width=C_WIDTH, height=C_HEIGHT)
    main_canvas.create_image(C_WIDTH / 2, C_HEIGHT / 2, image=bgr_image)
    return main_canvas
