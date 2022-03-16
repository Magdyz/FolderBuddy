# FolderBuddy

# A simple tool to create folders quickly

As a video editor I need to create the same folders everytime with a different project. I have created this simple code to ask me to change the project name then automatically create subfolders. It's best suited for project that need many subfolders without any copying and pasting.

Download the Zip file and extract it where you want new projects to be created. 

Before you start go ahead and open the file in any text editor. Change the names of the sub-folder that will need to be created. 

## Edit the simple code

All you need to do is change names for sub-folders as clear in the instructions

The code asks for the main folder name everytime as this could change but if you prefer to have the same folder name everytime and change subfolders use this code

```folderName = "CHANGE THIS TEXT BETWEEN BRACKETS WITH FOLDER NAME"```

instead of 

```folderName = input("Type folder name: \n")```

To change sub-folders, add name between brackets

``` 
subfolder1 = "CHANGE-SUBFOLDER-NAME1"
subfolder2 = "raw pictures"
subfolder3 = "Archives"

```

To add more subfolders, add this on top with the other subfolder variables

```
subfolder16 = "brand new sub-folder"
```

and add these two lines under the other lines in the function starting def. Don't change the spacing. And replace `subfolder` number with your new `subfolder16`

```
#	os.mkdir(f"{folderName}/{subfolder16}")
#	print( "++ " + folderName + "/" + subfolder16 + ' is created!')   
```


## Run the program

```
python3 folderBuddy.py
```
or
```
python folderBuddy.py
```

