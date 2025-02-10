WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

CD_TIMER = 300

class Timer:
    def __init__(self):
        reps = 0

    def format_time(self, time_in_sec):
        minutes = int(time_in_sec / 60)
        if minutes < 10:
            minutes = f"0{minutes}"
        seconds = time_in_sec % 60
        if seconds < 10:
            seconds = f"0{seconds}"
        formatted_time = f"{minutes}:{seconds}"
        return formatted_time

    def start_timer(self, main_window):
        self.countdown(main_window, CD_TIMER)

    def countdown(self, main_window, cur_time_sec):
        main_window.change_timer_text(self.format_time(cur_time_sec))
        if cur_time_sec > 0:
            main_window.window.after(1000, self.countdown, main_window, cur_time_sec - 1)
