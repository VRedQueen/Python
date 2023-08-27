import tkinter as tk

window = tk.Tk()
window.geometry("600x500")
window.title("Timer")
window.configure(background="black")

canvas = tk.Canvas(window, width=220, height=220, bg="black", highlightthickness=0)
canvas.pack(padx=10, pady=(50, 20), anchor="n")  # Using the anchor to center the Canvas vertically

circle = canvas.create_oval(20, 20, 200, 200, outline="gray78", width=3)

value_label = canvas.create_text(110, 110, text="0.00", font=("Arial", 35), fill="white")

def update_timer():
    global paused, time
    if not paused:
        time += 0.05
        canvas.itemconfig(value_label, text=f"{time:.2f}")
    window.after(30, update_timer)

paused = False
time = 0.00

def start_timer():
    global paused
    paused = False
    update_timer()

def pause_timer():
    global paused
    paused = True
     
def stop_timer():
    global paused, time
    paused = True
    time = 0.00
    canvas.itemconfig(value_label, text="0.00")

start_button = tk.Button(window, text="Start", command=start_timer, font=("Arial", 15))
pause_button = tk.Button(window, text="Pause", command=pause_timer, font=("Arial", 15))
stop_button = tk.Button(window, text="Stop", command=stop_timer, font=("Arial", 15))

# Horizontally center the buttons at the bottom
start_button.pack(side="left", padx=(190,10), pady=(0, 10))
pause_button.pack(side="left", padx=(5,10), pady=(0, 10))
stop_button.pack(side="right", padx=(0,190), pady=(0, 10))


window.mainloop()
