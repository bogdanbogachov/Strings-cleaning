from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import filedialog

root = Tk()
root.geometry("550x110")
root.title("From comma to point")

# Insert an explanatory field
path1 = Label(root, text = "Select folder where files to be changed are located", width = 40)
path1.grid(row = 0, column = 0, sticky = "w")

# Insert an explanatory field
path2 = Label(root, text = "Select folder where you want to save changed files", width = 40)
path2.grid(row = 1, column = 0, sticky = "w")

# Select a folder with old files
def old_path_func():
    global old_path
    root.directory = filedialog.askdirectory(initialdir="", title = "Select a folder")
    old_path = root.directory
    old_path = Label(root, text = old_path, width = 45, anchor = "w")
    old_path.grid(row = 0, column = 2)
    old_path = old_path.cget("text")
    return

button_dots_old = Button(root, text = "...", padx = 10, pady = 5, command = old_path_func)
button_dots_old.grid(row = 0, column = 1)

# Select a folder for new files
def new_path_func():
    global new_path
    root.directory = filedialog.askdirectory(initialdir = "", title = "Select a folder")
    new_path = root.directory
    new_path = Label(root, text = new_path, width = 45, anchor = "w")
    new_path.grid(row = 1, column = 2)
    new_path = new_path.cget("text")
    return

button_dots_new = Button(root, text = "...", padx = 10, pady = 5, command = new_path_func)
button_dots_new.grid(row = 1, column = 1)

# Insert a convert button
button_submit = Button(root, text = "Convert", padx = 10, pady = 5, command = root.destroy)
button_submit.grid(row = 2)

root.mainloop()