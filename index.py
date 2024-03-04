from tkinter import*
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN =24*60
SHORT_BREAK_MIN = 4*60
LONG_BREAK_MIN = 19*60
reps= 0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec=WORK_MIN+60
    short_break_sec=SHORT_BREAK_MIN*60 
    long_break_sec =LONG_BREAK_MIN*60      
 
    count_down(work_sec)     #1,3,5,7 reps
    if reps % 8==0:
       
       count_down(long_break_sec)  #8th round
       title_label.config(text="Break",fg=PINK)

    elif reps %2==0:

       count_down(short_break_sec)  #2 round
       title_label.config(text="Break",fg="green")

    else:
        count_down(work_sec)
        title_label.config(text="Task Time",fg="blue")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
        
def count_down(count):
    count_min=math.floor(count/60)
    count_second=count%60

    if count_second<=10:
      count_second=f"0{count_second}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_second}")
    print(count)
    if count>0:
       global timer
    
       timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            mark +="✔"
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()

window.title("pomodoro")
window.config(padx=100,pady=50,bg=GREEN)


title_label=Label(text="Timer",fg="red",bg=GREEN,font=(FONT_NAME,35,"bold"))
title_label.grid(column=1,row=1)


canvas=Canvas(width=200,height=224,bg=GREEN,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(103,130,text="00:00",fill="black",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=0)


start_button=Button(text="start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)


reset_button=Button(text="reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)


check_marks=Label(fg="blue")
check_marks.grid(column=1,row=3)

window.mainloop()
