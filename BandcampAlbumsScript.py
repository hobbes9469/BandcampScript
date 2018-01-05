import zipfile, os

SOURCE_DIR = ''
TARGET_DIR = ''
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

# Just strips the '.zip' at the end of all files to get folder name, and adds it to array
def getFolderNames():
    for file in FILES_TO_UNZIP:
        folder = file.replace(".zip", "")
        UNZIPPED_FILES.append(folder)

# Function to extract all zip files into the target directory
def extractAllZips():
    for file in FILES_TO_UNZIP:
        print("Extracting " + file + " to '" + TARGET_DIR + "'")
        zFile = zipfile.ZipFile(file)
        zFile.extractall(TARGET_DIR)

# Open new windows for all new directories
def openNewWindows():
    try:
        os.chdir(TARGET_DIR)
    except FileNotFoundError:
        print("ERROR: Target directory '" + TARGET_DIR + "' could not be found.")
    except:
        print("ERROR: Unexpected error. (TARGET)")
    for folder in UNZIPPED_FILES:
        fullPath = os.path.abspath(folder)
        os.startfile(fullPath)



if __name__ == "__main__":
    goToSourceDir()         # Go to source
    idZipFiles()            # Get names of all zips
    getFolderNames()        # Get folder names of zips without '.zip'
    extractAllZips()        # Extract zip files to target
    openNewWindows()        # Use folder names to open separate windows
