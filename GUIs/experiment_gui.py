# Imports the necessary packages
import tkinter as tk
from GUIs import acquisition_setup_gui

# Stores all the properties of the windows in one place to make changes easier
def get_window_properties(prop):

    window_title = "Experiment"
    window_width = 500
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

# Adds the GUI elements to the window
def add_gui_elements(root):

    # Gets the GUI element parameters parameters
    px, py, btn_width, btn_height, window_height = get_window_properties("gui")

    # Creates the frame that stores the GUI elements
    frame = tk.Frame(root)
    frame.pack(pady=(window_height//4))

    # Creates the button to end data collection
    def end_acquisition(root):
        print("ending")
    exit_btn = tk.Button(frame, text="End Acquisition", command=lambda:end_acquisition(root), width=btn_width, height=btn_height)
    exit_btn.grid(row=4, column=0, padx=px, pady=py)
    return

# Opens the main menu -- called by other scripts
def open(partID, protocol):
    print(partID)
    print(protocol)
    # Creates the window
    root = create_window()

    # Adds GUI elements to the window
    add_gui_elements(root)

    # Start the main loop
    root.mainloop()



