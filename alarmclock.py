from tkinter import *
import datetime
import time
import winsound
from threading import *
root = Tk()
root.geometry("400x200")
def Threading():
	t1=Thread(target=alarm)
	t1.start()

def alarm():
	while True:
		set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
		time.sleep(1)
		current_time = datetime.datetime.now().strftime("%H:%M:%S")
		print(current_time,set_alarm_time)
		if current_time == set_alarm_time:
			print("Time to Wake up")
			winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
Label(root,text="Set Time",font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()
hour = StringVar(root)

hours = list(range(0,25))
hourszf=[]
for n in hours:
    hourszf.append((str(n).zfill(2)))
hours = tuple(hourszf)

hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = list(range(0,61))
minuteszf=[]
for m in minutes:
    minuteszf.append((str(m).zfill(2)))
minutes = tuple(minuteszf)
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = list(range(0,61))
secondszf=[]
for m in seconds:
    secondszf.append((str(m).zfill(2)))
seconds = tuple(secondszf)
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=20)
root.mainloop()