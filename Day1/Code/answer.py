# You need to get a list of the files in the directory "files"
# You then need to compare it against a list generated from the "Files.txt" file.
# Every pair of students has a unique set of files!
# You will need a library to list the files in the directory


# Here, import a library to list the files:
import

# Open the file containing the list of patients and read it into a list, one line at a time

expectedFiles = []  # Start with an empty list

# This is a handy way to make sure the file is closed when you're done with it.
# For reference, the open command takes two arguments, a file name and an 'open mode' which may be 'r', 'w' or 'a'
# Thise mean 'r'ead, 'w'rite and 'a'ppend
with open("Files.txt", 'r') as fileList:
# You fill in this bit


# Now you have a list of files read from the file, you just need to work out which ones are missing.
# First of all, get a list of files in the directory (using a library function)

actualFiles =  # Simple function goes here!

# Now you have two lists, you can compare them to find which files are not in the directory