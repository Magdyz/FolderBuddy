#!/usr/bin/python3

import os,sys
import tkinter as tk
# modern themed widgets
from tkinter import ttk
import time

##### change Subfolder names to the desired subfolders you want. You can add or remove just don't remove the " " 

myFolders = ["Project", "Music", "Footage", "Export", "Documents"]

##### change Path names to the desired folder

PATH = "/Users/magdy.gaber/Documents/ShufiMafi/"


def styling():
# window title
	mainWindow.title('Folder Buddy')
# Styling ??
  window_width = 400
	window_height = 300
# get the screen dimension
	screen_width = mainWindow.winfo_screenwidth()
	screen_height = mainWindow.winfo_screenheight()
# find the center point
	center_x = int(screen_width/2 - window_width / 2)
	center_y = int(screen_height/2 - window_height / 2)
# set the position of the window to the center of the screen
	mainWindow.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
	mainWindow.resizable(False, False)
	mainWindow.attributes('-alpha', 0.97)
	mainWindow.attributes('-topmost', 1)

def createProject():
	folderName = str(PATH+entry.get())
# create main folder to house subfolders
	os.mkdir(folderName)
	print( "++ " + folderName + ' is created!')
# create sub-folders
	for item in myFolders:
		os.mkdir(f"{folderName}/{item}")
		print( "++ " + folderName + "/" + item + ' is created!')   
# confirmation message
	print("Directory is created")
	label.config(text='Directory is created!')

# GUI tk start
mainWindow = tk.Tk()

# styling function
styling()

# foldername tkinter
entry = tk.StringVar()
entryFolderName = ttk.Entry(mainWindow, textvariable=entry, width=15,font=('arial',20))
entryFolderName.pack(expand=True)
entryFolderName.focus()

# label to trigger createProject
label = ttk.Label(mainWindow, text=' Type or paste folder name', padding= 5,font= ("Helvetica", 14)
)
label.pack()
btn = ttk.Button(mainWindow, text='Create Project', command= createProject, padding=10)
btn.pack(ipadx=10,ipady=10,expand=True)


mainWindow.mainloop()
