"""
Kipland Melton 01/12/2021

Firstly, this program will scan a given directory for its files, skipping over
existing folders, and examine single files and their file types

Secondly, the program will create new directories corresponding to the file types
contained in the directory

Finally, the program will move single files into their corresponding "home" folders.

Twitter: @kiplandvaughn
"""

import os
from pathlib import Path


DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],

    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],

    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],

    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"],

    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],

    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],

    "PLAINTEXT": [".txt", ".in", ".out"],

    "PDF": [".pdf"],

    "PYTHON": [".py"],

    "XML": [".xml"],

    "EXE": [".exe"],

    "SHELL": [".sh"]

}

"""
  DONE Next goal for program functionality: Be able to view any custom directory

  DONE Next goal for program functionality: Print out each extension within a given
  directory

  DONE Next goal for program functionality, find a away to ignore other directories inside a given
  directory to only focus and raw files.


"""

def main():

  print("\n---Paste which directory you would like sorted---")
  chosenDirectory = raw_input("Enter directory: ")
  print("-------------------------------------------------\n")

  print("Is this directory valid?",os.path.isdir(chosenDirectory))

  directoryContents = os.listdir(chosenDirectory)

  # This is a 2D list that gets filled with lists that contain each files name denoted with [0]
  # and extension denoted with [1]
  fileTypes = []

  if os.path.isdir(chosenDirectory) == True:
    print("\n---Directory Contents---")
    #Where "entry" is a string, containing the name of a single folder or file
    #in a given directory
    for entry in directoryContents:
      #Prints a string of each file/folder within given directory
      print(entry)
      #Fills the fi leTypes list with lists that contain 2 elements, the name of the file
      #and the extension is applicable
      fileTypes.append(entry.split('.'))
    print("------------------------\n")
 
    print("---Files Within fileTypes---")
    # This loop displays each list (file) inside of the 2d fileTypes list.
    for x in range(len(fileTypes)):
      print(fileTypes[x])
    # This loop displays the file type of the first file in fileTypes list,
    # since the file type can be denoted as [1]

    print(len(fileTypes[0]))
    if len(fileTypes[0]) < 2:
      print("The first file in the given directories file type is: A Folder")
    else:
      print("The first file in the given directories file type is: ", fileTypes[0][1])
    print("----------------------------")


  else:
    print("Try a different directory or format.")
    print("Example: /Users/User/Documents/\n")

  


if __name__ == '__main__':
	main()