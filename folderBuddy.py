import os

folderName = input("Type folder name: \n")

def createProject():
	os.mkdir(folderName)
	print( "++ " + folderName + ' is created!')
	os.mkdir(f"{folderName}/project")
	print( "++ " + folderName + "/project" + ' is created!')
	os.mkdir(f"{folderName}/Music")
	print( "++ " + folderName + "/Music" + ' is created!')
	os.mkdir(f"{folderName}/Footage")
	print( "++ " + folderName + "/Footage" + ' is created!')
	os.mkdir(f"{folderName}/Export")
	print( "++ " + folderName + "/Export" + ' is created!')
	os.mkdir(f"{folderName}/Documents")
	print( "++ " + folderName + "/Documents" + ' is created!')

createProject()
print("Directory is created")

