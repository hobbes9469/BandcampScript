import os, zipfile


DISCARD_DIR = 'C:\\Users\\Matthew Kang\\Documents\\SOURCE\\DISCARD'
TARGET_DIR = 'C:\\Users\\Matthew Kang\\Documents\\TARGET'
FOLDERS_TO_OPEN = []


# Goes to the discard directory
def goToDir(directory):
    try:
        os.chdir(directory)
    except FileNotFoundError:
        print("ERROR: Discard directory '" + directory + "' could not be found.")
    except:
        print("ERROR: Unexpected error finding discard directory.")


# Gets the name of the folders based on the zip files in discard folder
def getFolderNames():
    files = os.listdir(".")
    for file in files:
        if zipfile.is_zipfile(file):
            folderName = file.replace(".zip", "")
            FOLDERS_TO_OPEN.append(folderName)


# Opens a new window for each folder specified under FOLDERS_TO_OPEN
def openFolders():
    for folder in FOLDERS_TO_OPEN:
        fullPath = os.path.abspath(folder)
        try:
            os.startfile(fullPath)
        except FileNotFoundError:
            print("ERROR: Unable to find folder in path '" + fullPath + "'.")
        except:
            print("ERROR: Unexpected error with opening new windows.")


if __name__ == "__main__":
    goToDir(DISCARD_DIR)        # Go to discard directory
    getFolderNames()            # Get the names of the folders to open in target directory
    goToDir(TARGET_DIR)         # Go to target directory
    openFolders()               # Open the folders
