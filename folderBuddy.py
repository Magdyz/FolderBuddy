import os

# Folder name that will be inputed everytime as a question

folderName = input("Type folder name: \n")

# remove the # from the code below and add the Folder name if you prefer to have a constant name everytime without questions.
# If you choose to use the option below comment the first folderName above. You can only use one variable.

# folderName = "CHANGE THIS TEXT BETWEEN BRACKETS WITH FOLDER NAME"

subfolder1 = "CHANGE-SUBFOLDER-NAME1"
subfolder2 = "CHANGE-SUBFOLDER-NAME2"
subfolder3 = "CHANGE-SUBFOLDER-NAME3"
subfolder4 = "CHANGE-SUBFOLDER-NAME4"
subfolder5 = "CHANGE-SUBFOLDER-NAME5"
subfolder6 = "CHANGE-SUBFOLDER-NAME6"

# Add more if you want

# subfolder7 = "Images"
# subfolder6 = "Documents"


# The main function that includes all sub-folders.
# Nothing needs to be changed here 

def createProject():
	os.mkdir(folderName)
	print( "++ " + folderName + ' is created!')
	os.mkdir(f"{folderName}/{subfolder1}")
	print( "++ " + folderName + "/" + subfolder1 + ' is created!')   
	os.mkdir(f"{folderName}/{subfolder2}")
	print( "++ " + folderName + "/" + subfolder2 + ' is created!')   
	os.mkdir(f"{folderName}/{subfolder3}")
	print( "++ " + folderName + "/" + subfolder3 + ' is created!')   
	os.mkdir(f"{folderName}/{subfolder4}")
	print( "++ " + folderName + "/" + subfolder4 + ' is created!')   
	os.mkdir(f"{folderName}/{subfolder5}")
	print( "++ " + folderName + "/" + subfolder5 + ' is created!')   	
	os.mkdir(f"{folderName}/{subfolder6}")
	print( "++ " + folderName + "/" + subfolder6 + ' is created!')   
	
## To add more subfolders 
## Add subfolder7 = "CHANGE-SUBFOLDER-NAME7" like the example above
## then
## remove "#" and copy and paste the code below with the same spaces and change subfolder#number accordingly

#	os.mkdir(f"{folderName}/{subfolder7}")
#	print( "++ " + folderName + "/" + subfolder7 + ' is created!')   
#	os.mkdir(f"{folderName}/{subfolder8}")
#	print( "++ " + folderName + "/" + subfolder8 + ' is created!')   


createProject()
print("Directory is created")

