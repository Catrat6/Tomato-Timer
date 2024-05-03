import time
from tkinter import *
import math


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
checks = " "
timer = None

def reset_timer():
    global reps, checks, timer
    window.after_cancel(timer)
    reps = 0
    checks = " "
    title_label.config(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, 'bold'))
    check_marks.config(text=checks, bg=YELLOW, fg=GREEN, font=('Arial', 20, 'bold'))
    canvas.itemconfig(timer_text, text='00:00')

def start_timer():
    global reps, checks
    reps += 1

    work_time = 25 * 60
    short_break = 5 * 60
    long_break = 25 * 60

    if reps >= 9:
        title_label.config(text='Reset Timer', bg=YELLOW, fg=RED, font=(FONT_NAME, 50, 'bold'))

    print(reps)
    if reps == 8:
        count_down(long_break)
        title_label.config(text='Relax', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, 'bold'))
    elif reps % 2 == 0:
        count_down(short_break)
        title_label.config(text='Break', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, 'bold'))
    else:
        count_down(work_time)
        checks += '\u2713'
        title_label.config(text='Work', bg=YELLOW, fg=RED, font=(FONT_NAME, 50, 'bold'))
        check_marks.config(text=checks, bg=YELLOW, fg=GREEN, font=('Arial', 20, 'bold'))

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if int(count_sec) < 10:
        count_sec = f'0{count_sec}'


    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)


window = Tk()
window.title('Pomodoro Study Timer')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')

canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))

title_label = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, 'bold'))
title_label.grid(column=1, row=0)

start_button = Button(text='Start', bg=GREEN, font=(FONT_NAME, 12, 'bold'), command=start_timer)
start_button.grid(column=0, row=2)

check_marks = Label(text=checks, bg=YELLOW, fg=GREEN, font=('Arial', 20, 'bold'))
check_marks.grid(column=1, row=3)

reset_button = Button(text='Reset', bg=GREEN, font=('Arial', 12, 'bold'), command=reset_timer)
reset_button.grid(column=3, row=2)

canvas.grid(column=1, row=1)

window.mainloop()