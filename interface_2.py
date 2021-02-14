from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import filedialog

root = Tk()
root.geometry("750x135")
root.title("Find a record")

# Insert an explanatory field
path1 = Label(root, text = "Select a file where you want to find a record", width = 50, anchor = "w")
path1.grid(row = 0, column = 0)

# Insert an explanatory field
path2 = Label(root, text = "Select a folder where you want to save a file with a found record", width = 50, anchor = "w")
path2.grid(row = 1, column = 0)

# Insert a field where a value needed to be found will be input
value = Entry(root, width = 50, borderwidth = 5)
value.grid(row = 2, column = 0, padx = 1, pady = 1, sticky = "w")
value.insert(0, "Enter here a value you are looking for")

# Select a folder with old files
def file_path_func():
    global file_path
    root.filename = filedialog.askopenfilename(initialdir="", title = "Select a file", filetype = (("txt files", "*.txt"),("all files", "*.*")))
    file_path = root.filename
    file_path = Label(root, text = root.filename, width = 45, anchor = "w")
    file_path.grid(row = 0, column = 2)
    file_path = file_path.cget("text")
    return

button_dots_file = Button(root, text = "...", padx = 10, pady = 5, command = file_path_func)
button_dots_file.grid(row = 0, column = 1)

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

# Insert a find button
def myClick():
    global value
    value = value.get()
    return

button_find = Button(root, text = "Find", padx = 10, pady = 5, command = lambda: [myClick(), root.destroy()])
button_find.grid(row = 3)

root.mainloop()