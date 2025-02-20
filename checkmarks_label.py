import tkinter as tk
import config as cfg

class CheckmarksLabel(tk.Label):
    def __init__(self):
        super().__init__()

        self.checkmark_text = tk.StringVar()
        self.config(
            bg=cfg.YELLOW,
            fg=cfg.GREEN,
            font=cfg.CHECK_MARK_FONT,
            textvariable=self.checkmark_text
        )

    def add_checkmark(self):
        cur_text = self.checkmark_text.get()
        if len(cur_text) < cfg.MAX_CHECKMARKS_NUM:
            cur_text += cfg.CHECK_MARK
            self.checkmark_text.set(cur_text)

    def reset_text(self):
        self.checkmark_text.set("")
