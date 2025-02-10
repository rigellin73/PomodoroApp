import tkinter as tk
from timer import Timer

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

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

BGR_IMAGE = "tomato.png"
L_FONT = ("Courier", 35, "bold")
B_FONT = ("Arial", 14, "normal")
CHECK_MARK = "✔"
CHECK_MARK_FONT = ("Courier", 18, "normal")

class MainWindow:
    def __init__(self):

        self.window = tk.Tk()
        self.setup_main_window()
        self.bgr_image = tk.PhotoImage(file=BGR_IMAGE)

        self.canvas = tk.Canvas(width=C_WIDTH, height=C_HEIGHT, bg=YELLOW, highlightthickness=0)
        self.setup_main_canvas()
        self.timer_text = self.canvas.create_text(T_POSX, T_POSY, text=T_TEXT, fill=T_COLOR, font=T_FONT)

        self.timer = Timer()

        self.timer_label = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=L_FONT)
        self.start_button = tk.Button(text="Start", font=B_FONT, command=self.start_timer)
        self.reset_button = tk.Button(text="Reset", font=B_FONT)
        self.checkmark_label = tk.Label(text=CHECK_MARK, bg=YELLOW, fg=GREEN, font=CHECK_MARK_FONT)

        self.canvas.grid(row=1, column=1)
        self.timer_label.grid(row=0, column=1)
        self.start_button.grid(row=2, column=0)
        self.reset_button.grid(row=2, column=2)
        self.checkmark_label.grid(row=3, column=1)

    def setup_main_window(self):
        self.window.title(W_TITLE)
        self.window.config(padx=W_PADX, pady=W_PADY, bg=YELLOW)

    def setup_main_canvas(self):
        self.canvas.create_image(C_WIDTH / 2, C_HEIGHT / 2, image=self.bgr_image)

    def start_timer(self):
        self.timer.start_timer(self)

    def change_timer_text(self, text):
        self.canvas.itemconfig(self.timer_text, text=text)
