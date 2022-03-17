import os

# Folder name that will be inputed everytime as a question

folderName = input("Type folder name: \n")                                # Prompt user to add folder name 
# folderName = "CHANGE THIS TEXT BETWEEN BRACKETS WITH FOLDER NAME"       # uncomment if you want the same foldername all the time


# change Subfolder names to the desired subfolders you want. You can add or remove just don't remove the " " 

myFolders = ["subfolder1", "subfolder2", "subfolder3", "subfolder4", "subfolder5", "subfolder6"]


# The main function 
# Nothing needs to be changed here 

def createProject():
	os.mkdir(folderName)
	print( "++ " + folderName + ' is created!')

	for item in myFolders:
		os.mkdir(f"{folderName}/{item}")
		print( "++ " + folderName + "/" + item + ' is created!')   


createProject()
print("Mission Accomplished")

