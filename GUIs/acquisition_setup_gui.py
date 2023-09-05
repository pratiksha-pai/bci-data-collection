#Imports the necessary packages
import tkinter as tk
from GUIs import main_menu_gui
from Custom_Packages import read_write

import sys
import os

# Add folder_b to sys.path
sys.path.append('/Users/jackmostyn/Lab Scripts/bci-data-collection/Custom_Packages')


# Stores all the properties of the windows in one place to make changes easier
def get_window_properties(prop):

    window_title = "Acquisition Setup"
    window_width = 500
    window_height = 500
    window_x = 200
    window_y = 200 
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

# Adds the GUI elements to the window
def add_gui_elements(root):
    # Gets the GUI element parameters
    px, py, btn_width, btn_height, ent_width, ent_height, window_height = get_window_properties("gui")

    # Creates the frame that stores the GUI elements
    frame = tk.Frame(root)
    frame.pack(pady=(window_height//4))

    # Creates the label and field asking for the participant ID
    partID_lbl = tk.Label(frame, text="Participant ID:")
    partID_lbl.grid(row=0, column=0, padx=px, pady=py, sticky="w")
    partID_ent = tk.Entry(frame, width=btn_width)
    partID_ent.grid(row=0, column=1, padx=px, pady=py)

    # Creates a dropdown menu to select the protocol for the experiment
    # Get the options for the dropdown menu
    options = get_dropdown_options()

    # Creates the label for the dropdown
    dropdown_label = tk.Label(frame, text="Select an Option:")
    dropdown_label.grid(row=6, column=0, padx=px, pady=py, sticky="w")  # positioned below the entry

    # Creates the dropdown menu (Combobox widget)
    dropdown = ttk.Combobox(frame, values=options, width=btn_width)
    dropdown.grid(row=6, column=1, padx=px, pady=py)
    dropdown.set(options[0])  # set the first option as the default value


    # Creates the button to cancel the setup and return to main menu
    def cancel(root):
        root.destroy()
        main_menu_gui.open()
    cancel_btn = tk.Button(frame, text="Cancel", command=lambda:cancel(root), width=btn_width, height=btn_height)
    cancel_btn.grid(row=5, column=0, padx=px, pady=py)
    return

# Opens the main menu -- called by other scripts
def open():
    
    # Creates the window
    root = create_window()

    # Adds GUI elements to the window
    add_gui_elements(root)

    # Start the main loop
    root.mainloop()



