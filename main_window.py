import tkinter as tk
from timer import Timer
import config as cfg

class MainWindow:
    def __init__(self):

        self.window = tk.Tk()
        self.setup_main_window()
        self.bgr_image = tk.PhotoImage(file=cfg.BGR_IMAGE)

        self.canvas = tk.Canvas(width=cfg.C_WIDTH, height=cfg.C_HEIGHT, bg=cfg.YELLOW, highlightthickness=0)
        self.setup_canvas()
        self.timer_text = self.canvas.create_text(cfg.T_POSX, cfg.T_POSY, text=cfg.T_DEFAULT_TEXT, fill=cfg.T_COLOR, font=cfg.T_FONT)

        self.timer = Timer(self)

        self.timer_label = tk.Label(text=cfg.L_DEFAULT_TEXT, bg=cfg.YELLOW, fg=cfg.GREEN, font=cfg.L_FONT)
        self.start_button = tk.Button(text=cfg.B_START_TEXT, font=cfg.B_FONT, command=self.start_timer)
        self.reset_button = tk.Button(text=cfg.B_RESET_TEXT, font=cfg.B_FONT, command=self.reset_timer)
        self.checkmark_text = tk.StringVar()
        self.checkmark_label = tk.Label(bg=cfg.YELLOW, fg=cfg.GREEN, font=cfg.CHECK_MARK_FONT, textvariable=self.checkmark_text)

        self.canvas.grid(row=1, column=1)
        self.timer_label.grid(row=0, column=1)
        self.start_button.grid(row=2, column=0)
        self.reset_button.grid(row=2, column=2)
        self.checkmark_label.grid(row=3, column=1)

        self.window.mainloop()

    def setup_main_window(self):
        self.window.title(cfg.W_TITLE)
        self.window.config(padx=cfg.W_PADX, pady=cfg.W_PADY, bg=cfg.YELLOW)

    def setup_canvas(self):
        self.canvas.create_image(cfg.C_WIDTH / 2, cfg.C_HEIGHT / 2, image=self.bgr_image)

    def start_timer(self):
        self.start_button.config(state="disabled")
        self.timer.start_timer()

    def change_timer_text(self, text):
        self.canvas.itemconfig(self.timer_text, text=text)

    def go_to_work(self):
        self.timer_label.config(text=cfg.L_WORK_TEXT, fg=cfg.GREEN)

    def go_to_break(self):
        self.timer_label.config(text=cfg.L_BREAK_TEXT, fg=cfg.PINK)

    def go_to_long_break(self):
        self.timer_label.config(text=cfg.L_BREAK_TEXT, fg=cfg.RED)

    def add_checkmark(self):
        cur_text = self.checkmark_text.get()
        cur_text += cfg.CHECK_MARK
        self.checkmark_text.set(cur_text)

    def reset_timer(self):
        self.timer.stop_timer()
        self.timer_label.config(text=cfg.L_DEFAULT_TEXT, fg=cfg.GREEN)
        self.change_timer_text(cfg.T_DEFAULT_TEXT)
        self.checkmark_text.set("")
        self.start_button.config(state="normal")

    def delay_action(self, delay_ms, action, *args):
        return self.window.after(delay_ms, action, *args)

    def cancel_action(self, action):
        self.window.after_cancel(action)
