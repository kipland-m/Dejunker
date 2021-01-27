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

  DONE Next goal for program functionality: form algorithm to sort over and create a list of all
  files that are ready to be sorted

  DONE Next goal for program functionality: Create a list of all file types within a given directory, 

Next goal for program functionaliy: Create a new directory for each unique entry 
in the list of file types "rawfileTypes   "


Be aware of the inevitable problem where a file contains more than one "." in its name.

"""

def main():

  print("\n---Paste which directory you would like sorted---")
  chosenDirectory = raw_input("Enter directory: ")
  print("-------------------------------------------------\n")

  print("Is this directory valid?",os.path.isdir(chosenDirectory))
  

  # This is a 2D list that gets filled with lists that contain each files name denoted with [0]
  # and extension denoted with [1]
  fileTypes = []

  rawfileTypes = []

  if os.path.isdir(chosenDirectory) == True:
    # directoryContents is a self explanitory list that gets filled
    # with seperate entities that each are names of files in a given directory.
    directoryContents = os.listdir(chosenDirectory)

    print("\n---Directory Contents---")

    #counter = iterates over the items within fileTypes
    #unsortable = tracks folders (in theory)
    #sortable = tracks raw files (in theory)

    counter = 0
    unsortable = 0
    sortable = 0


    #Where "entry" is a string, containing the name of a single folder or file
    #in a given directory
    for entry in directoryContents:
      #Prints a string of each file/folder within given directory
      print(entry)

      #Fills the fileTypes list with lists that contain 2 elements, the name of the file
      #and the extension is applicable
      fileTypes.append(entry.split('.'))


      # tests the length of a file inside a directory, if finding it has no extension
      # i.e. a length of 1, add one to unsortable
      if len(fileTypes[counter]) < 2:
        unsortable += 1
        #counter iterates to have each element inside fileTypes list
        #checked to see if it is unsortable
        counter += 1
      else:
        sortable += 1
    print("unsortable objects:",unsortable)
    print("sortable objects:",sortable)
    print("------------------------\n")
 
    print("---Files Within fileTypes---")


    # This loop displays each list (file) inside of the 2d fileTypes list.
    for x in range(len(fileTypes)):
      print(fileTypes[x])

      if len(fileTypes[x]) < 2:
        print("this is a folder, will not be added to rawfileTypes\n")
        continue

      elif len(fileTypes[x]) > 1 & len(fileTypes) < 3:
        rawfileTypes.append(fileTypes[x][1])
  
    print("\nthe variety of file types within the given directory are as follows:")  
    print(rawfileTypes)

    #To implement a procedure to create new directories you must specifify a path to create the new
    #directories in, and you may use os.path.join in order to 
    #concatenate a path and generated folder names

    directoryToCreate = []

    for x in range(len(rawfileTypes)):
      directoryToCreate.append(os.path.join(chosenDirectory, rawfileTypes[x]))
    

    for x in range(len(rawfileTypes)):
      try:
        os.mkdir(directoryToCreate[x])
      except OSError:
        continue



    for entry in directoryToCreate:
      print(entry)

    print("----------------------------")


  else:
    print("\n---Couldnt find that directory---")
    print("Try a different directory or format.")
    print("Example: /Users/User/Documents/")
    print("---------------------------------\n")
  


if __name__ == '__main__':
	main()