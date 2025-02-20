import config as cfg

class Timer:
    def __init__(self, main_window):
        self.window = main_window
        self.reps = 0
        self.timer_action = None
        self.start_timer_action = None

    def format_time(self, time_in_sec):
        minutes = int(time_in_sec / 60)
        if minutes < 10:
            minutes = f"0{minutes}"
        seconds = time_in_sec % 60
        if seconds < 10:
            seconds = f"0{seconds}"
        formatted_time = f"{minutes}:{seconds}"
        return formatted_time

    def start_timer(self):
        self.reps += 1
        if self.reps % cfg.NUMBER_OF_CYCLES == 0:
            self.window.go_to_long_break()
            self.countdown(cfg.LONG_BREAK_MIN * cfg.SECONDS_MULTIPLIER)
        elif self.reps % 2 == 0:
            self.window.go_to_break()
            self.countdown(cfg.SHORT_BREAK_MIN * cfg.SECONDS_MULTIPLIER)
        else:
            self.window.go_to_work()
            self.countdown(cfg.WORK_MIN * cfg.SECONDS_MULTIPLIER)

    def countdown(self, cur_time_sec):
        self.window.change_timer_text(self.format_time(cur_time_sec))
        if cur_time_sec > 0:
            self.timer_action = self.window.delay_action(1000, self.countdown, cur_time_sec - 1)
        else:
            if self.reps % 2 != 0:
                self.window.add_checkmark()
            self.start_timer_action = self.window.delay_action(1000, self.start_timer)

    def stop_timer(self):
        if self.timer_action:
            self.window.cancel_action(self.timer_action)
        if self.start_timer_action:
            self.window.cancel_action(self.start_timer_action)
        self.reps = 0
