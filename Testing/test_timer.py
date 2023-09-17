import tkinter as tk
from datetime import datetime, timedelta

def update_timer_display():
    if running.get():
        delta = datetime.now() - last_update_time[0]
        time_passed[0] += delta
        last_update_time[0] = datetime.now()

    # Compute total seconds
    total_seconds = time_passed[0].seconds + time_passed[0].microseconds / 1e6
    minutes, remainder = divmod(total_seconds, 60)
    seconds = int(remainder)
    milliseconds = int((remainder - seconds) * 1000)

    # Update the display
    timer_label.config(text="{}:{:02}:{:03}".format(minutes, seconds, milliseconds))
    
    # Schedule the function to be called after 50ms for more frequent updates
    root.after(50, update_timer_display)

def start_timer():
    if not running.get():
        running.set(True)
        last_update_time[0] = datetime.now()

def pause_timer():
    if running.get():
        running.set(False)
        delta = datetime.now() - last_update_time[0]
        time_passed[0] += delta

def print_timer():
    # Calculate the total time in seconds (including the fraction of a second)
    total_seconds = time_passed[0].seconds + time_passed[0].microseconds / 1e6
    print(total_seconds)

root = tk.Tk()
root.title("Timer App")

time_passed = [timedelta(0)]  # Use a list to make it mutable
last_update_time = [None]
running = tk.BooleanVar(root, False)

# Label to show the timer
timer_label = tk.Label(root, text="0:00:000", font=("Arial", 24))
timer_label.pack(pady=20)

# Buttons
play_button = tk.Button(root, text="Play", command=start_timer)
play_button.pack(side="left", padx=10)

pause_button = tk.Button(root, text="Pause", command=pause_timer)
pause_button.pack(side="left", padx=10)

print_button = tk.Button(root, text="Print", command=print_timer)
print_button.pack(side="right", padx=10)

update_timer_display()

root.mainloop()
