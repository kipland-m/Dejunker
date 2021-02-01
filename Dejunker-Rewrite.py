import os, shutil

def main():

	# Will contain all directories of files that need to be sorted
	sortableFiles = []
	# Will contain all directories of folders that are within the directory to be sorted
	unsortableFiles = []

	chosenDirectory = raw_input("Enter directory: ")

	if os.path.isdir(chosenDirectory) == True:
		directoryContents = os.listdir(chosenDirectory)

		counter = 0

		for entry in directoryContents:
			if os.path.isdir(entry) == True:
				unsortableFiles.append(directoryContents[counter])
			
			else:
				sortableFiles.append(directoryContents[counter])
			
			counter += 1

	print(sortableFiles)
	print(unsortableFiles)

if __name__ == '__main__':
	main()
