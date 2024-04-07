
import sys
import os
import glob
from pathlib import Path

# scan without sub-folder
def scan_files(folderPath, fileExtension):
    print("scan in: ", folderPath)
    dirList = os.listdir(folderPath) 
    for filename in dirList: 
        if filename.endswith(fileExtension): 
            print(os.path.join(folderPath, filename)) 
            

# scan with sub-folder
def scan_files_withsubfolder(folderPath, fileExtension):
    print("scan in: ", folderPath)
    for dirpath, dirs, files in os.walk(folderPath):
        for filename in files:
            if filename.endswith(fileExtension): 
                print(os.path.join(dirpath, filename)) 


if __name__ == '__main__':
    folderPath = os.getcwd()
    scan_files_withsubfolder(folderPath, ".bat")
    