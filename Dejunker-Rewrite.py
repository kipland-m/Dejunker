import os, shutil

def main():

	# Will contain all directories of files that need to be sorted
	sortableFiles = []
	# Will contain all directories of folders that are within the directory to be sorted
	unsortableFiles = []
	# Will be populated with filepaths of all the items inside a given directory
	directoryPaths = []
	# Will be populated with lists pulled from directoryContents
	fileTypes = []
	


	chosenDirectory = raw_input("Enter directory: ")


	if os.path.isdir(chosenDirectory) == True:
		directoryContents = os.listdir(chosenDirectory)

	for x in range(len(directoryContents)):
		directoryPaths.append(os.path.join(chosenDirectory, directoryContents[x]))


	# This for loop looks into directoryContents, splits the entry by a 
	for entry in directoryContents:
		fileTypes.append(entry.split('.'))




	# This for loop views into directoryPaths, which is populated
	# with all the filepaths found in the given directory.
	# It then checks every filepath, and determines if they are files or folders
	counter = 0
	for entry in directoryPaths:
		if os.path.isdir(entry) == True:
			unsortableFiles.append(directoryPaths[counter])
		
		elif os.path.isfile(entry) == True:
			sortableFiles.append(directoryPaths[counter])
		


		counter += 1

	print("Sortable")
	for entry in sortableFiles:
		print(entry)
	print("Unsortable")
	for entry in unsortableFiles:
		print(entry)

if __name__ == '__main__':
	main()
