import tkinter as tk
from timer import Timer

# Colors
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# Window settings
W_TITLE = "Pomodoro"
W_PADX = 100
W_PADY = 50

# Canvas settings
C_WIDTH = 200
C_HEIGHT = 224

# Timer text settings
T_POSX = C_WIDTH / 2
T_POSY = C_HEIGHT / 2 + 18
T_TEXT = "00:00"
T_COLOR = "white"
T_FONT = ("Courier", 35, "bold")

# Bgr image path
BGR_IMAGE = "tomato.png"

# Timer label settings
L_FONT = ("Courier", 35, "bold")
L_START_TEXT = "Timer"
L_WORK_TEXT = "Work"
L_BREAK_TEXT = "Break"

# Buttons settings
B_FONT = ("Arial", 14, "normal")
B_START_TEXT = "Start"
B_RESET_TEXT = "Reset"

# Check mark settings
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

        self.timer = Timer(self)

        self.timer_label = tk.Label(text=L_START_TEXT, bg=YELLOW, fg=GREEN, font=L_FONT)
        self.start_button = tk.Button(text=B_START_TEXT, font=B_FONT, command=self.start_timer)
        self.reset_button = tk.Button(text=B_RESET_TEXT, font=B_FONT, command=self.reset_timer)
        self.checkmark_text = tk.StringVar()
        self.checkmark_label = tk.Label(bg=YELLOW, fg=GREEN, font=CHECK_MARK_FONT, textvariable=self.checkmark_text)

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
        self.timer.start_timer()

    def change_timer_text(self, text):
        self.canvas.itemconfig(self.timer_text, text=text)

    def go_to_work(self):
        self.timer_label.config(text=L_WORK_TEXT, fg=GREEN)

    def go_to_break(self):
        self.timer_label.config(text=L_BREAK_TEXT, fg=PINK)

    def go_to_long_break(self):
        self.timer_label.config(text=L_BREAK_TEXT, fg=RED)

    def add_checkmark(self):
        cur_text = self.checkmark_text.get()
        cur_text += CHECK_MARK
        self.checkmark_text.set(cur_text)

    def reset_timer(self):
        self.timer.stop_timer()
        self.timer_label.config(text=L_START_TEXT, fg=GREEN)
        self.change_timer_text(T_TEXT)
        self.checkmark_text.set("")

    def delay_action(self, delay_ms, action, *args):
        return self.window.after(delay_ms, action, *args)

    def cancel_action(self, action):
        self.window.after_cancel(action)
