# Imports the necessary packages
import tkinter as tk
import datetime
import os
import multiprocessing
import csv
from GUIs import main_menu_gui

# Stores all the properties of the windows in one place to make changes easier
def get_window_properties(prop):

    window_title = "Experiment"
    window_width = 1000
    window_height = 800
    window_x = 200
    window_y = 200 
    padx = 5
    pady = 5
    btn_width = 20
    btn_height = 2

    if prop == "window":
        return window_title, window_width, window_height, window_x, window_y
    if prop == "gui":
        return padx, pady, btn_width, btn_height, window_height

# Creates the window
def create_window():

    # Creates the window
    root = tk.Tk()

    # Sets the properties of the window
    title, width, height, x, y = get_window_properties("window")

    # Changes the window's properties
    root.title(title) # Sets the window title
    root.geometry(f"{width}x{height}+{x}+{y}") # Sets the window's dimensions
    return root

# Creates the folder for storing data
def create_storage(partID, protocol):
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime('%Y%m%d%H%M%S')
    folderID = protocol + "_" + formatted_date + "_" + partID
    base_path = "/Users/jackmostyn/Lab Scripts/bci-data-collection/Data"
    folder_path = base_path + "/" + folderID
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

# Gets the instructions for data collection
def get_instructions():
    protocol_path = "/Users/jackmostyn/Lab Scripts/bci-data-collection/Protocols/Main"
    instructions_path = protocol_path + "/Instructions.csv"
    parameters_path = protocol_path + "/Parameters.csv"
    instructions = []
    with open(instructions_path, 'r') as file1:
        reader1 = csv.reader(file1)
        for rowa in reader1:
            instructions.append(rowa)
    instructions.pop(0)
    parameters = []
    with open(parameters_path, 'r') as file2:
        reader2 = csv.reader(file2)
        for rowb in reader2:
            parameters.append(rowb)
    return instructions, parameters   

# Collects the body camera data
def collect_bodycam(queue):
    data = [1, 2, 3, 4, 5]
    queue.put(data)

# Collects the dart camera data
def collect_dart(queue):
    data = [1, 2, 3, 4, 5]
    queue.put(data)

# Collects the glove data
def collect_gloves(queue):
    data = [1, 2, 3, 4, 5]
    queue.put(data)

# Collects the glasses data
def collect_glasses(queue):
    data = [1, 2, 3, 4, 5]
    queue.put(data)

# Collects the EEG data
def collect_eeg(queue):
    data = [1, 2, 3, 4, 5]
    queue.put(data)

# Collects the EMG data
def collect_emg(queue):
    data = [1, 2, 3, 4, 5]
    queue.put(data)

def run_experiment(root, save_path, instructions, parameters):
    # Gets the GUI element parameters parameters
    px, py, btn_width, btn_height, window_height = get_window_properties("gui")

    # Stores whether the experiment is running
    running = tk.BooleanVar(root, False)
    started = tk.BooleanVar(root, False)
    collecting = tk.BooleanVar(root, False)
    instruction_index = tk.IntVar(root, 0)
    last_update_time = [None]
    time_passed = [datetime.timedelta(0)]

    # Creates the frame that stores the GUI elements
    frame = tk.Frame(root)
    frame.pack(pady=(window_height//4))

    # Creates the label that displays the time
    timer_lbl = tk.Label(frame, text="0:00:000")
    timer_lbl.grid(row=0, column=0, padx=px, pady=py)

    # Creates the label that displays the instruction
    instruction_lbl = tk.Label(frame, text=instructions[0][5])
    instruction_lbl.grid(row=0, column=1, padx=px, pady=py)

    # Creates the data collection queues
    queue_bodycam = multiprocessing.Queue()
    queue_dart = multiprocessing.Queue()
    queue_gloves = multiprocessing.Queue()
    queue_glasses = multiprocessing.Queue()
    queue_eeg = multiprocessing.Queue()
    queue_emg = multiprocessing.Queue()


    # Creates the data collection threads
    proc_bodycam = multiprocessing.Process(target=collect_bodycam, args=(queue_bodycam,))
    proc_dart = multiprocessing.Process(target=collect_dart, args=(queue_dart,))
    proc_gloves = multiprocessing.Process(target=collect_gloves, args=(queue_gloves,))
    proc_glasses = multiprocessing.Process(target=collect_glasses, args=(queue_glasses,))
    proc_eeg = multiprocessing.Process(target=collect_eeg, args=(queue_eeg,))
    proc_emg = multiprocessing.Process(target=collect_emg, args=(queue_emg,))


    def update_timer_display():
        if running.get():
            delta = datetime.datetime.now() - last_update_time[0]
            time_passed[0] += delta
            last_update_time[0] = datetime.datetime.now()

        # Compute total seconds
        total_seconds = time_passed[0].seconds + time_passed[0].microseconds / 1e6
        minutes, remainder = divmod(total_seconds, 60)
        seconds = int(remainder)
        milliseconds = int((remainder - seconds) * 1000)

        # Checks if a timestamp has been crossed
        if instruction_index.get() < len(instructions):
            if total_seconds >= float(instructions[instruction_index.get()][1]):
                instruction_index.set(instruction_index.get() + 1)
                instruction_lbl.config(text=instructions[instruction_index.get()][5])
                state = instructions[instruction_index.get()][6]
                if state == "Add " and not collecting.get():
                    # proc_bodycam.start()
                    # proc_dart.start()
                    # proc_gloves.start()
                    # proc_glasses.start()
                    # proc_eeg.start()
                    # proc_emg.start()
                    collecting.set(True)
                elif state == "Save " and collecting.get():
                    # proc_bodycam.join()
                    # proc_dart.join()
                    # proc_gloves.join()
                    # proc_glasses.join()
                    # proc_eeg.join()
                    # proc_emg.join()
                    # bodycam_data = queue_bodycam.get()
                    # dart_data = queue_dart.get()
                    # gloves_data = queue_gloves.get()
                    # glasses_data = queue_glasses.get()
                    # eeg_data = queue_eeg.get()
                    # emg_data = queue_emg.get()
                    # print(dart_data)
                    collecting.set(False)
                elif state == "End ":
                    running.set(False)
        else:
            instruction_lbl.config(text="experiment finished")
        # Update the display
        timer_lbl.config(text="{:02}:{:02}:{:03}".format(minutes, seconds, milliseconds))
            
        # Schedule the function to be called after 50ms for more frequent updates
        root.after(10, update_timer_display)

    # Creates the button to start data collection
    def start_acquisition():
        if not running.get() and not started.get():
            running.set(True)
            started.set(True)
            last_update_time[0] = datetime.datetime.now()
            update_timer_display()
    start_btn = tk.Button(frame, text="Start", command=lambda:start_acquisition(), width=btn_width, height=btn_height)
    start_btn.grid(row=4, column=0, padx=px, pady=py)

    # Creates the button to pause data collection
    def pause():
        if running.get():
            running.set(False)
            delta = datetime.datetime.now() - last_update_time[0]
            time_passed[0] += delta
    pause_btn = tk.Button(frame, text="Pause", command=lambda:pause(), width=btn_width, height=btn_height)
    pause_btn.grid(row=4, column=1, padx=px, pady=py)

    # Creates the button to resume data collection
    def resume():
        if not running.get():
            running.set(True)
            last_update_time[0] = datetime.datetime.now()
    resume_btn = tk.Button(frame, text="Resume", command=lambda:resume(), width=btn_width, height=btn_height)
    resume_btn.grid(row=4, column=2, padx=px, pady=py)

    # Creates the button to end data collection
    def end_acquisition(root):
        root.destroy()
        main_menu_gui.open()
    end_btn = tk.Button(frame, text="End", command=lambda:end_acquisition(root), width=btn_width, height=btn_height)
    end_btn.grid(row=4, column=3, padx=px, pady=py)
    return


# Opens the main menu -- called by other scripts
def open_window(partID, protocol):
    root = create_window()
    save_path = create_storage(partID, protocol)
    instructions, parameters = get_instructions()
    run_experiment(root, save_path, instructions, parameters)
    root.mainloop()




