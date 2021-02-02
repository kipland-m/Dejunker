import os, shutil

def main():

	# Will contain all directories of files that need to be sorted
	sortableFiles = []
	# Will contain all directories of folders that are within the directory to be sorted
	unsortableFiles = []
	# Will be populated with filepaths of all the items inside a given directory
	directoryPaths = []

	chosenDirectory = raw_input("Enter directory: ")


	if os.path.isdir(chosenDirectory) == True:
		directoryContents = os.listdir(chosenDirectory)

	for x in range(len(directoryContents)):
		directoryPaths.append(os.path.join(chosenDirectory, directoryContents[x]))



	print("Sortable")
	for entry in sortableFiles:
		print(entry)
	print("Unsortable")
	for entry in unsortableFiles:
		print(entry)

if __name__ == '__main__':
	main()
