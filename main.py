from tkinter import *
import math
import os
from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

class PomodoroTimer:
    def __init__(self):
        self.reps = 0
        self.timer = None
        self.is_running = False
        self.paused = False
        self.remaining_time = 0
        
        self.window = Tk()
        self.window.title("Pomodoro")
        self.window.config(padx=100, pady=50, bg=YELLOW)
        
        self.setup_ui()
        
    def setup_ui(self):
        # Canvas setup
        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        try:
            self.tomate_img = PhotoImage(file="tomato.png")
            self.canvas.create_image(100, 112, image=self.tomate_img)
        except Exception as e:
            messagebox.showerror("Error", f"Could not load tomato image: {str(e)}")
            self.window.destroy()
            return
            
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
        self.canvas.grid(column=1, row=1)

        # Timer title
        self.timer_title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
        self.timer_title.grid(column=1, row=0)

        # Buttons
        self.start_button = Button(text="Start", highlightthickness=0, command=self.start_timer)
        self.start_button.grid(column=0, row=2)
        
        self.pause_button = Button(text="Pause", highlightthickness=0, command=self.pause_timer, state=DISABLED)
        self.pause_button.grid(column=1, row=2)
        
        self.reset_button = Button(text="Reset", highlightthickness=0, command=self.reset_timer)
        self.reset_button.grid(column=2, row=2)

        # Check marks
        self.check_mark = Label(bg=YELLOW, fg=GREEN)
        self.check_mark.grid(column=1, row=3)

    def reset_timer(self):
        if self.timer:
            self.window.after_cancel(self.timer)
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.timer_title.config(text="Timer")
        self.check_mark.config(text="")
        self.reps = 0
        self.is_running = False
        self.paused = False
        self.start_button.config(state=NORMAL)
        self.pause_button.config(state=DISABLED)

    def pause_timer(self):
        if self.is_running:
            if not self.paused:
                self.paused = True
                self.pause_button.config(text="Resume")
                if self.timer:
                    self.window.after_cancel(self.timer)
            else:
                self.paused = False
                self.pause_button.config(text="Pause")
                self.count_down(self.remaining_time)

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.config(state=DISABLED)
            self.pause_button.config(state=NORMAL)
            self.reps += 1

            work_sec = WORK_MIN * 60
            short_break_sec = SHORT_BREAK_MIN * 60
            long_break_sec = LONG_BREAK_MIN * 60

            if self.reps % 8 == 0:
                self.count_down(long_break_sec)
                self.timer_title.config(text="Break", fg=RED)
            elif self.reps % 2 == 0:
                self.count_down(short_break_sec)
                self.timer_title.config(text="Break", fg=PINK)
            else:
                self.count_down(work_sec)
                self.timer_title.config(text="Work", fg=GREEN)

    def count_down(self, count):
        if self.paused:
            self.remaining_time = count
            return
            
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_sec}")
        
        if count > 0:
            self.timer = self.window.after(1000, self.count_down, count - 1)
        else:
            self.is_running = False
            self.start_button.config(state=NORMAL)
            self.pause_button.config(state=DISABLED)
            self.start_timer()
            mark = ""
            for _ in range(math.floor(self.reps/2)):
                mark += "✔"
            self.check_mark.config(text=mark)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = PomodoroTimer()
    app.run()