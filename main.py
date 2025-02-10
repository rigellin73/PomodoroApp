import tkinter as tk
from itertools import count

from main_window import setup_main_window, setup_main_canvas, setup_timer_text
from colors import YELLOW, GREEN

# Constants

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CD_TIMER = 300

BGR_IMAGE = "tomato.png"
L_FONT = ("Courier", 35, "bold")
B_FONT = ("Arial", 14, "normal")
CHECK_MARK = "✔"
CHECK_MARK_FONT = ("Courier", 18, "normal")

def start_timer():
    countdown(CD_TIMER)

def countdown(cur_time_sec):
    minutes = int(cur_time_sec / 60)
    if minutes < 10:
        minutes = f"0{minutes}"
    seconds = cur_time_sec % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    formatted_time = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=formatted_time)
    if cur_time_sec > 0:
        window.after(1000, countdown, cur_time_sec - 1)

window = setup_main_window()
bgr_image = tk.PhotoImage(file=BGR_IMAGE)

canvas = setup_main_canvas(bgr_image)
timer_text = setup_timer_text(canvas)

timer_label = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=L_FONT)
start_button = tk.Button(text="Start", font=B_FONT, command=start_timer)
reset_button = tk.Button(text="Reset", font=B_FONT)
checkmark_label = tk.Label(text=CHECK_MARK, bg=YELLOW, fg=GREEN, font=CHECK_MARK_FONT)

canvas.grid(row=1, column=1)
timer_label.grid(row=0, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
checkmark_label.grid(row=3, column=1)

window.mainloop()
