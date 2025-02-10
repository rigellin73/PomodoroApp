# Prod values
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
# SECONDS_MULTIPLIER = 60
# NUMBER_OF_CYCLES = 8

# Test values
WORK_MIN = 5
SHORT_BREAK_MIN = 3
LONG_BREAK_MIN = 10
SECONDS_MULTIPLIER = 1
NUMBER_OF_CYCLES = 4

class Timer:
    def __init__(self, main_window):
        self.window = main_window
        self.reps = 0
        self.timer = None

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
        if self.reps % NUMBER_OF_CYCLES == 0:
            self.window.go_to_long_break()
            self.countdown(LONG_BREAK_MIN * SECONDS_MULTIPLIER)
        elif self.reps % 2 == 0:
            self.window.go_to_break()
            self.countdown(SHORT_BREAK_MIN * SECONDS_MULTIPLIER)
        else:
            self.window.go_to_work()
            self.countdown(WORK_MIN * SECONDS_MULTIPLIER)

    def countdown(self, cur_time_sec):
        self.window.change_timer_text(self.format_time(cur_time_sec))
        if cur_time_sec > 0:
            self.timer = self.window.delay_action(1000, self.countdown, cur_time_sec - 1)
        else:
            if self.reps % 2 != 0:
                self.window.add_checkmark()
            self.start_timer()

    def stop_timer(self):
        self.window.cancel_action(self.timer)
        self.reps = 0
