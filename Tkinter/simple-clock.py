from tkinter import *
from time import strftime

def update_timer():
    time= strftime("%H:%M:%S %p")
    label_watch.config(text=time)
    label_watch.after(1000, update_timer)
    
window=Tk()
window.title("Digital watch")

label_watch= Label(window, font=("Arial",40,"bold"), bg= "gray10", fg="lime green")
label_watch.pack(anchor="center")

update_timer()
window.mainloop()    
