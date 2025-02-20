import tkinter as tk
import config as cfg

class PomodoroCanvas(tk.Canvas):
    def __init__(self):
        super().__init__()

        self.config(width=cfg.C_WIDTH, height=cfg.C_HEIGHT, bg=cfg.YELLOW, highlightthickness=0)
        self.bgr_image = tk.PhotoImage(file=cfg.BGR_IMAGE)
        self.create_image(cfg.C_WIDTH / 2, cfg.C_HEIGHT / 2, image=self.bgr_image)
        self.timer_text = self.create_text(
            cfg.T_POSX,
            cfg.T_POSY,
            text=cfg.T_DEFAULT_TEXT,
            fill=cfg.T_COLOR,
            font=cfg.T_FONT
        )

    def set_timer_text(self, cur_time):
        self.itemconfig(self.timer_text, text=self.format_time(cur_time))

    def reset_text(self):
        self.itemconfig(self.timer_text, text=cfg.T_DEFAULT_TEXT)

    def format_time(self, time_in_sec):
        minutes = int(time_in_sec / 60)
        if minutes < 10:
            minutes = f"0{minutes}"
        seconds = time_in_sec % 60
        if seconds < 10:
            seconds = f"0{seconds}"
        formatted_time = f"{minutes}:{seconds}"
        return formatted_time
