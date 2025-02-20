import tkinter as tk
from timer import Timer
import config as cfg
from pomodoro_canvas import PomodoroCanvas
from checkmarks_label import CheckmarksLabel

class MainWindow:
    def __init__(self):

        self.window = tk.Tk()
        self.setup_main_window()

        self.pomodoro_canvas = PomodoroCanvas()

        self.timer = Timer(self)

        self.timer_label = tk.Label(text=cfg.L_DEFAULT_TEXT, bg=cfg.YELLOW, fg=cfg.GREEN, font=cfg.L_FONT)
        self.start_button = tk.Button(text=cfg.B_START_TEXT, font=cfg.B_FONT, command=self.start_timer)
        self.reset_button = tk.Button(text=cfg.B_RESET_TEXT, font=cfg.B_FONT, command=self.reset_timer)

        self.checkmarks_label = CheckmarksLabel()

        self.pomodoro_canvas.grid(row=1, column=1)
        self.timer_label.grid(row=0, column=1)
        self.start_button.grid(row=2, column=0)
        self.reset_button.grid(row=2, column=2)
        self.checkmarks_label.grid(row=3, column=1)

        self.window.mainloop()

    def setup_main_window(self):
        self.window.title(cfg.W_TITLE)
        self.window.config(padx=cfg.W_PADX, pady=cfg.W_PADY, bg=cfg.YELLOW)

    def start_timer(self):
        self.start_button.config(state="disabled")
        self.timer.start_timer()

    def change_state(self, cur_time, reps):
        self.pomodoro_canvas.set_timer_text(cur_time)
        if cur_time == 0 and reps % 2 != 0:
            self.checkmarks_label.add_checkmark()

    def go_to_work(self):
        self.timer_label.config(text=cfg.L_WORK_TEXT, fg=cfg.GREEN)

    def go_to_break(self):
        self.timer_label.config(text=cfg.L_BREAK_TEXT, fg=cfg.PINK)

    def go_to_long_break(self):
        self.timer_label.config(text=cfg.L_BREAK_TEXT, fg=cfg.RED)

    def reset_timer(self):
        self.timer.stop_timer()
        self.timer_label.config(text=cfg.L_DEFAULT_TEXT, fg=cfg.GREEN)
        self.pomodoro_canvas.reset_text()
        self.checkmarks_label.reset_text()
        self.start_button.config(state="normal")

    def delay_action(self, delay_ms, action, *args):
        return self.window.after(delay_ms, action, *args)

    def cancel_action(self, action):
        self.window.after_cancel(action)
