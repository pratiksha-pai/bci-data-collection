#Imports the necessary packages
import tkinter as tk
from GUIs import main_menu_gui
from GUIs import experiment_gui
from tkinter import ttk
from Custom_Packages import read_write

# Stores all the properties of the windows in one place to make changes easier
def get_window_properties(prop):

    window_title = "Acquisition Setup"
    window_width = 1000
    window_height = 1000
    window_x = 50
    window_y = 50 
    padx = 5
    pady = 5
    btn_width = 20
    btn_height = 2
    ent_width = 20
    ent_height = 2

    if prop == "window":
        return window_title, window_width, window_height, window_x, window_y
    if prop == "gui":
        return padx, pady, btn_width, btn_height, ent_width, ent_height, window_height

# Gets the list of protocols
def get_protocols():
    protocols = ["one", "two", "three"]
    return protocols

# Gets the setup status of the equipment
def get_equipment_status():
    eeg = "good"
    emg = "good"
    glasses = "good"
    body = "good"
    dart = "good"
    gloves = "good"
    statuses = eeg, emg, glasses, body, dart, gloves
    return statuses

# Creates the window
def create_window():
    root = tk.Tk() # Creates the window
    title, width, height, x, y = get_window_properties("window") # Sets the properties of the window
    root.title(title) # Sets the window title
    root.geometry(f"{width}x{height}+{x}+{y}") # Sets the window's dimensions
    return root

# Adds the GUI elements to the window
def add_gui_elements(root):
    px, py, btn_width, btn_height, ent_width, ent_height, window_height = get_window_properties("gui") # Gets the GUI element parameters

    def create_frame2(root, partID, protocol):
        frame2 = tk.Frame(root) # Creates the frame that stores the GUI elements
        frame2.pack(pady=(window_height//4)) # Sets the size of the pady property of the frame
        statuses = get_equipment_status() # Gets the setup status of the equipment
        
        # Creates the eeg options
        eeg_lbl = tk.Label(frame2, text="EEG:")
        eeg_lbl.grid(row=0, column=0, padx=px, pady=py, sticky="w")
        eeg_status_lbl = tk.Label(frame2, text=statuses[0])
        eeg_status_lbl.grid(row=0, column=1, padx=px, pady=py, sticky="w")
        def setup_eeg(): # Function called to setup the eeg
            print("setting up EEG")
        eeg_btn = tk.Button(frame2, text="Setup", command=lambda:setup_eeg(), width=btn_width, height=btn_height) # Creates the button
        eeg_btn.grid(row=0, column=2, padx=px, pady=py) # Places the button

        # Creates the emg options
        emg_lbl = tk.Label(frame2, text="EMG:")
        emg_lbl.grid(row=1, column=0, padx=px, pady=py, sticky="w")
        emg_status_lbl = tk.Label(frame2, text=statuses[1])
        emg_status_lbl.grid(row=1, column=1, padx=px, pady=py, sticky="w")
        def setup_emg(): # Function called to setup the emg
            print("setting up EMG")
        emg_btn = tk.Button(frame2, text="Setup", command=lambda:setup_emg(), width=btn_width, height=btn_height) # Creates the button
        emg_btn.grid(row=1, column=2, padx=px, pady=py) # Places the button

        # Creates the glasses options
        glasses_lbl = tk.Label(frame2, text="Glasses:")
        glasses_lbl.grid(row=2, column=0, padx=px, pady=py, sticky="w")
        glasses_status_lbl = tk.Label(frame2, text=statuses[2])
        glasses_status_lbl.grid(row=2, column=1, padx=px, pady=py, sticky="w")
        def setup_glasses(): # Function called to setup the glasses
            print("setting up glasses")
        glasses_btn = tk.Button(frame2, text="Setup", command=lambda:setup_glasses(), width=btn_width, height=btn_height) # Creates the button
        glasses_btn.grid(row=2, column=2, padx=px, pady=py) # Places the button

        # Creates the body tracking options
        body_lbl = tk.Label(frame2, text="Body Tracking:")
        body_lbl.grid(row=3, column=0, padx=px, pady=py, sticky="w")
        body_status_lbl = tk.Label(frame2, text=statuses[3])
        body_status_lbl.grid(row=3, column=1, padx=px, pady=py, sticky="w")
        def setup_body(): # Function called to setup the body tracking
            print("setting up body tracking")
        body_btn = tk.Button(frame2, text="Setup", command=lambda:setup_body(), width=btn_width, height=btn_height) # Creates the button
        body_btn.grid(row=3, column=2, padx=px, pady=py) # Places the button

        # Creates the dart camera options
        dart_lbl = tk.Label(frame2, text="Dart Camera:")
        dart_lbl.grid(row=4, column=0, padx=px, pady=py, sticky="w")
        dart_status_lbl = tk.Label(frame2, text=statuses[4])
        dart_status_lbl.grid(row=4, column=1, padx=px, pady=py, sticky="w")
        def setup_dart(): # Function called to setup the dart camera
            print("setting up dart camera")
        dart_btn = tk.Button(frame2, text="Setup", command=lambda:setup_dart(), width=btn_width, height=btn_height) # Creates the button
        dart_btn.grid(row=4, column=2, padx=px, pady=py) # Places the button

        # Creates the gloves options
        gloves_lbl = tk.Label(frame2, text="Gloves:")
        gloves_lbl.grid(row=5, column=0, padx=px, pady=py, sticky="w")
        gloves_status_lbl = tk.Label(frame2, text=statuses[5])
        gloves_status_lbl.grid(row=5, column=1, padx=px, pady=py, sticky="w")
        def setup_gloves(): # Function called to setup the gloves
            print("setting up gloves")
        gloves_btn = tk.Button(frame2, text="Setup", command=lambda:setup_gloves(), width=btn_width, height=btn_height) # Creates the button
        gloves_btn.grid(row=5, column=2, padx=px, pady=py) # Places the button

        # Creates the button to cancel the setup and return to main menu
        def cancel(root): # Function called to cancel the setup
            root.destroy() # Destroys the current window
            main_menu_gui.open() # Opens the new window
        cancel_btn = tk.Button(frame2, text="Cancel", command=lambda:cancel(root), width=btn_width, height=btn_height) # Creates the button
        cancel_btn.grid(row=6, column=0, padx=px, pady=py) # Places the button

        # Creates the button to finish the setup and open the experiment window
        def finish_setup(root): # Function called to finish the setup
            root.destroy()
            experiment_gui.open(partID, protocol)
        finish_btn = tk.Button(frame2, text="Finish Setup", command=lambda:finish_setup(root), width=btn_width, height=btn_height) # Creates the button
        finish_btn.grid(row=6, column=1, padx=px, pady=py) # Places the button
        return

    def create_frame1(root):
        frame1 = tk.Frame(root) # Creates the frame that stores the GUI elements
        frame1.pack(pady=(window_height//4)) # Sets the size of the pady property of the frame

        # Creates the label and field asking for the participant ID
        partID_lbl = tk.Label(frame1, text="Participant ID:")
        partID_lbl.grid(row=0, column=0, padx=px, pady=py, sticky="w")
        partID_ent = tk.Entry(frame1, width=btn_width)
        partID_ent.grid(row=0, column=1, padx=px, pady=py)

        # Creates a dropdown menu to select the protocol for the experiment
        options = get_protocols() # Get the options for the dropdown menu
        dropdown_label = tk.Label(frame1, text="Select an Option:") # Creates the label for the dropdown
        dropdown_label.grid(row=1, column=0, padx=px, pady=py, sticky="w")  # Places the label
        dropdown = ttk.Combobox(frame1, values=options, width=ent_width) # Creates the dropdown menu
        dropdown.grid(row=1, column=1, padx=px, pady=py) # Places the dropdown
        dropdown.set(options[0])  # Sets the first option as default

        # Creates the button to cancel the setup and return to main menu
        def cancel(root): # Function called to cancel the setup
            root.destroy() # Destroys the current window
            main_menu_gui.open() # Opens the new window
        cancel_btn = tk.Button(frame1, text="Cancel", command=lambda:cancel(root), width=btn_width, height=btn_height) # Creates the button
        cancel_btn.grid(row=6, column=0, padx=px, pady=py) # Places the button

        # Creates the button to continue the setup and move to equipment setup
        def continue_setup(): # Function called to continue the setup
            partID = partID_ent.get()
            protocol = dropdown.get()
            frame1.destroy()
            create_frame2(root, partID, protocol)
        continue_btn = tk.Button(frame1, text="Continue Setup", command=lambda:continue_setup(), width=btn_width, height=btn_height) # Creates the button
        continue_btn.grid(row=6, column=1, padx=px, pady=py) # Places the button
        return

    create_frame1(root)
    return

# Opens the main menu -- called by other scripts
def open():
    root = create_window() # Creates the window
    add_gui_elements(root) # Adds GUI elements to the window
    root.mainloop() # Start the main loop