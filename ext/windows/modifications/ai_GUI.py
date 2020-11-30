from tkinter import messagebox as mb
from functools import partial
import tkinter.font as font
from tkinter import *
import tkinter as tk 
import webbrowser
import ctypes
import os

# add whitespace between UI's images, labels, or buttons
def addWhitespace(amount):
    whitespaceFont = font.Font(family='Helvetica', size=5)
    for i in range(amount):
        Label(root, text=' ', font=whitespaceFont).pack(fill=tk.BOTH)

# open project's GitHub web page
def openREADME():
    webbrowser.open('https://en.wikipedia.org/wiki/Kinect') # TODO, link main project repo when made public

# open "Moving Pose" research paper web page
def openPaper():
    webbrowser.open('https://openaccess.thecvf.com/content_iccv_2013/papers/Zanfir_The_Moving_Pose_2013_ICCV_paper.pdf')

# Link: https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except
# check if a string is an int or not
def is_int(value):
    try: 
        int(value)
        return True
    except ValueError:
        return False

# print list indexes line by line
def printList(data):
    for i in data:
        print(i)

# read textfile into a list
def readTextFile(name):
    with open(name) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

# set textfile to stop C++ code from recording to a text file
def reset():
    file = open("record_frame_count.txt", "w+")
    file.write("DONE")
    results.config(text = "...")

# create prediction with moving pose
def prediction():
    print("TODO - Do the AI Part!")
    results.config(text = "YOU ARE RUNNING")

# comminucate between python and C++ code
def process_frame_count(frame_count):
    global filePath
    if(is_int(frame_count.get()) == True):
        state = readTextFile(filePath)
        state = str(state[0])
        if(state == "DONE"):
            file = open(filePath, "w+")
            file.write(str(frame_count.get()))
            results.config(text = "LOADING")
        elif(state == "DONE-RECORDING"):
            #mb.showinfo("Result", "Running!")
            results.config(text = "Processing...")
            reset()
            prediction()
        else:
            mb.showerror("Error", "Currently Recording, Please Wait!")
    else:
        mb.showerror("Error", "Please enter frame count as an int! Try Again!")

# clean UI's resolution for higher resolution monitors (Windows 10 only)
# ctypes.windll.shcore.SetProcessDpiAwareness(2)

# setup tkinter object
root = Tk() 

# setup text fonts in UI
defaultOptionsFont = font.Font(family='Helvetica', size=20)
defaultLabelFont = font.Font(family='Helvetica', size=20)
defaultButtonFont = font.Font(family='Helvetica', size=15)
resultsFont = font.Font(family='Helvetica', size=18)

# setup UI colors
bgColor = "white"
bgButton = "ghost white"

# setup UI dimension
dimensions = "550x1230"

# setup "results" label
#   - this will be used to display predictions from moving pose
results = Label(root, text="...", font=resultsFont)
filePath = "record_frame_count.txt"

### GUI Windows Setups

# setup UI shape
root.title('SRC-20')
root.configure(background=bgColor)
root.resizable(width=False, height=False)
root.geometry(dimensions)

# menu setup for README & MovingPose
menu = Menu(root) 
root.config(menu=menu)
filemenu = Menu(menu) 
menu.add_cascade(label='README', command=openREADME)
menu.add_cascade(label='MovingPose', command=openPaper) 

# UI's top image icon
photoIcon = PhotoImage(file = r"GUI_Icon.png") 
Button(root, image = photoIcon, highlightbackground=bgColor).pack(side = TOP) 

# setup MODE label
Label(root, text='Modes', font=defaultLabelFont, bg='gold').pack(fill=tk.BOTH)
addWhitespace(1)
Label(root, text='Moving Pose', font=font.Font(family='Helvetica', size=16, slant='italic')).pack(fill=tk.BOTH)
addWhitespace(1)

# setup FRAME COUNT label
Label(root, text='Frame Count', font=defaultLabelFont, bg='lightgreen').pack(fill=tk.BOTH)
addWhitespace(1)

# setup UI's FRAME text input
frame_count = StringVar()
Entry(root, textvariable=frame_count, font=defaultLabelFont).pack(fill=tk.BOTH)
process_frame_count = partial(process_frame_count, frame_count)
addWhitespace(1)

# setup UI's RECORD/PROCESS button
tk.Button(root, text='Record/Process', width=350, command=process_frame_count, highlightbackground=bgColor, font=defaultButtonFont, bg=bgButton).pack()
addWhitespace(1)

# setup UI's RESULTS label
resultsLabelColor = 'light blue'
Label(root, text='Results', font=defaultLabelFont, bg=resultsLabelColor).pack(fill=tk.BOTH)
addWhitespace(1)

# setup UI's result label
results.pack(fill=tk.BOTH)
addWhitespace(2)

# setup UI's RESET label 
resetLabelColor = 'orange red'
Label(root, text='RESET', font=defaultLabelFont, bg=resetLabelColor).pack(fill=tk.BOTH)
addWhitespace(1)

# setup UI's RESET button
tk.Button(root, text='<*_*>', width=350, command=reset, highlightbackground="red", font=defaultButtonFont, bg=bgButton).pack()
addWhitespace(2)

# main tkinter loop
root.mainloop()

