import tkinter as tk

def open():

    #Sets the properties of the window
    title = "Main Menu"
    width = 500
    height = 500
    x = 200
    y = 200 

    #Creates the window
    root = tk.Tk()

    #Changes the window's properties
    root.title(title) #Sets the window title
    root.geometry(f"{width}x{height}+{x}+{y}") #Sets the window's dimensions

    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    open()
