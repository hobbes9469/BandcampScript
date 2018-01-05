import zipfile, os, shutil

SOURCE_DIR = 'C:\\Users\\Matthew Kang\\Documents\\SOURCE'
TARGET_DIR = 'C:\\Users\\Matthew Kang\\Documents\\TARGET'
DISCARD_DIR = 'C:\\Users\\Matthew Kang\\Documents\\SOURCE\\Finished'
FILES_TO_UNZIP = []
UNZIPPED_FILES = []


# All this does is change the directory to source directory
def goToSourceDir():
    try:
        os.chdir(SOURCE_DIR)
    except FileNotFoundError:
        print("ERROR: Source directory '" + SOURCE_DIR + "' could not be found.")
    except:
        print("ERROR: Unexpected error. (SOURCE)")

# Function to fill FILES_TO_UNZIP with names of zip files in directory
def idZipFiles():
    files = os.listdir(".")
    for file in files:
        if zipfile.is_zipfile(file):
            FILES_TO_UNZIP.append(file)

# Strips the '.zip' at the end of all files to get folder name, and adds it to array
# Also has the responsibility of creating the new folders for files to go into
def getFolderNames():
    for file in FILES_TO_UNZIP:
        folder = file.replace(".zip", "")
        UNZIPPED_FILES.append(folder)
    for newFolder in UNZIPPED_FILES:
        newFolderPath = TARGET_DIR + "\\" + newFolder
        try:
            os.makedirs(newFolderPath)
        except FileExistsError:
            print("ERROR: Directory at '" + newFolderPath +
                  "' could not be created because it already exists.")

# Function to extract all zip files into the target directory
def extractAllZips():
    for file in FILES_TO_UNZIP:
        print("Extracting '" + file + "' to '" + TARGET_DIR + "'")
        zFile = zipfile.ZipFile(file)
        folder = file.replace(".zip", "")
        zFile.extractall(TARGET_DIR + "\\" + folder)

# Moves zips into a folder for later removal (or checking)
def discardZips():
    for file in FILES_TO_UNZIP:
        zipPath = os.path.abspath(file)
        try:
            shutil.move(zipPath, DISCARD_DIR)
        except shutil.Error:
            print("ERROR: File '" + file + "' in discard folder already exists.")
            os.unlink(zipPath)

# Open new windows for all new directories
def openNewWindows():
    try:
        os.chdir(TARGET_DIR)
    except FileNotFoundError:
        print("ERROR: Target directory '" + TARGET_DIR + "' could not be found.")
    except:
        print("ERROR: Unexpected error. (TARGET)")
    for folder in UNZIPPED_FILES:
        try:
            fullPath = os.path.abspath(folder)
            os.startfile(fullPath)
        except FileNotFoundError:
            print("ERROR: Unable to find folder in path '" + fullPath + "'.")
        except:
            print("ERROR: Unexpected error with opening new windows.")



if __name__ == "__main__":
    goToSourceDir()         # Go to source
    idZipFiles()            # Get names of all zips
    getFolderNames()        # Get folder names of zips without '.zip'
    extractAllZips()        # Extract zip files to target
    discardZips()           # Moves all zip files in source to a discard folder
    openNewWindows()        # Use folder names to open separate windows
