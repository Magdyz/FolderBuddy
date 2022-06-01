# FolderBuddy

# A simple tool to create folders quickly

As a video editor I need to create the same folders everytime with a different project. I have created this simple code to ask me to change the project name then automatically create subfolders. It's best suited for project that need many subfolders without any copying and pasting.

Download the Zip file and extract it where you want new projects to be created. 

Before you start go ahead and open the file in any text editor. Change the names of the sub-folder that will need to be created. 

-----------------------------------------------------------------------------------------

## Edit the simple code

All you need to do is change names for "sub-folders" as clear in the instructions

The code asks for the main folder name everytime as this could change but if you prefer to have the same folder name everytime and change subfolders use this code

```folderName = "CHANGE THIS TEXT BETWEEN BRACKETS WITH FOLDER NAME"```

instead of 

```folderName = input("Type folder name: \n")```

## Folder name as an argument

You could add the folder name as an argument when running the script. Uncomment the following code for `foldername`

```
import sys                                    # uncomment if you want the foldername to be inputed as an argument 
folderName = " ".join(sys.argv[1:])           # uncomment if you want the foldername to be inputed as an argument 

```

This will make the script and foldername run in one command. 

```
python3 folderBuddy.py test folder num 1

```
or

```
python folderBuddy.py test folder num 1

```
-----------------------------------------------------------------------------------------
## Chnage/add sub-folders


To change sub-folders, add name between brackets

``` 
myFolders = ["subfolder1", "subfolder2", "subfolder3", "subfolder4", "subfolder5", "My NEW SUBFOLDER"]

```

To add more or remove subfolders

```
myFolders = ["subfolder1", "subfolder2", "subfolder3", "subfolder4", "subfolder5", "My NEW SUBFOLDER", "My NEW SUBFOLDER2"]

```

-----------------------------------------------------------------------------------------

## Run the program

```
python3 folderBuddy.py
```
or
```
python folderBuddy.py
```

## Run the program by double clicking it on Mac

I have found this to be very tricky on Mac but the best solution was by doing the following

- changing file name to `folderBuddy.command` or `folderBuddy.tool` instead of the normal `.py`
- inputing the following code in the terminal to change permission to excute code `chmod +x folderBuddy.command`

### Troubleshooting

This will work but I have found the the program will create the new folder/Sub-folders in the main directory not in the current folder. Maybe it was only my case but if this happens. Add the following code to the top of you script:

```
PATH = "/Users/Jim/Desktop/projects/" # copy the path for your folder or where you want your new folder to be
folderName = PATH+input("Type folder name: \n")     
```

Best of luck,
MG
