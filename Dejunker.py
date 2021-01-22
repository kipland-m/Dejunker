"""
Kipland Melton 01/12/2021

Firstly, this program will scan a given directory for its files, skipping over
existing folders, and examine single files and their file types

Secondly, the program will create new directories corresponding to the file types
contained in the directory

Finally, the program will move single files into their corresponding "home" folders.
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

Next goal for program functionality: Print out each extension within a given
directory, while skipping over folders.

"""

def main():

  print("\nPaste which directory you would like sorted")
  chosenDirectory = raw_input("Enter directory: ")

  print("Is this directory valid?",os.path.isdir(chosenDirectory))

  directoryContents = os.listdir(chosenDirectory)

  fileTypes = []

  if os.path.isdir(chosenDirectory) == True:
    print("\n---Directory Contents---")
    for entry in directoryContents:
      print(entry)
      file_type = entry.split(".")
      fileTypes.append(file_type[1])

    print("------------------------\n")
  else:
    print("Try a different directory or format.")
    print("Example: /Users/User/Documents/\n")

  


if __name__ == '__main__':
	main()