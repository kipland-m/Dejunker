import os, shutil

def main():

	# Will contain all directories of files that need to be sorted
	sortableFiles = []
	# Will contain all directories of folders that are within the directory to be sorted
	unsortableFiles = []
	# Will be populated with filepaths of all the items inside a given directory
	directoryPaths = []
	# Will be populated with all file types within given directory
	fileTypes = []
	# Will be populated with all generated directories to create new "sorted" directories
	directoryToCreate = []
	# Will be populated with all the file types that there are only one of
	singularFiles = []


	###### PROGRAM START
	chosenDirectory = raw_input("Enter directory: ")


	if os.path.isdir(chosenDirectory) == True:
		directoryContents = os.listdir(chosenDirectory)

	for x in range(len(directoryContents)):
		directoryPaths.append(os.path.join(chosenDirectory, directoryContents[x]))


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


	# Create list of all file extensions that need to have a new directory created
	for x in range(len(sortableFiles)):
		fileName, fileExtension = os.path.splitext(sortableFiles[x])
		fileExtension = fileExtension.replace('.','')
		fileTypes.append(fileExtension)

	# Populates the directoryToCreate list that will contain every, well, directory to create
	for x in range(len(fileTypes)):
		directoryToCreate.append(os.path.join(chosenDirectory, fileTypes[x]))


	### FILE MANIPULATION STARTS HERE
	# This create all the folders that the sortableFiles will be place in
	for x in range(len(fileTypes)):
		try:
			os.mkdir(directoryToCreate[x])
		except OSError:
			continue

	# This for loop will move all the files in sortableFiles
	# to their new "homes" that were created in the for loop above.
	for x in range(len(fileTypes)):
			try:
				shutil.move(sortableFiles[x],directoryToCreate[x])
			except shutil.Error:
				continue


	##### Development runtime infao
	print("\nQueued Directories")
	for entry in directoryToCreate:
		print(entry)

	print("\nFile Types")
	for entry in fileTypes:
		print(entry)

	print("\nSortable")
	for entry in sortableFiles:
		print(entry)
	
	print("\nThere are only one of these file types therefore they will not be moved")
	for entry in singularFiles:
		print(entry)

	print("\nUnsortable")
	for entry in unsortableFiles:
		print(entry)

	print("\nSuccessfully sorted "+str(len(fileTypes))+" files!")


	###### SUCCESSFUL PROGRAM FINISH
  


if __name__ == '__main__':
	main()
