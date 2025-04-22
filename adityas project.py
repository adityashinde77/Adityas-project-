import tkinter as tk
import time

def start_timer():
    try:
        t = int(entry.get())
    except ValueError:
        label.config(text="Please enter a valid number!")
        return

    while t >= 0:
        mins, secs = divmod(t, 60)
        timer_format = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=timer_format)
        root.update()
        time.sleep(1)
        t -= 1

    label.config(text="Time's Up!")

# Create window
root = tk.Tk()
root.title("Aditya's Project - Timer")
root.geometry("300x200")
root.configure(bg="lightblue")

# Title Label
title = tk.Label(root, text="Aditya's Timer", font=("Arial", 20, "bold"), bg="lightblue")
title.pack(pady=10)

# Time entry
entry = tk.Entry(root, font=("Arial", 16), justify="center")
entry.pack(pady=10)

# Start button
start_button = tk.Button(root, text="Start Timer", command=start_timer, font=("Arial", 14))
start_button.pack(pady=10)

# Timer display
label = tk.Label(root, text="00:00", font=("Arial", 30), bg="lightblue")
label.pack(pady=10)

root.mainloop()