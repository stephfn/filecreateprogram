# Stephanie Nord
# 10.1

"""program that performs file processing activities will use the OS library
to validate that a directory exists before creating a file in that directory
Your program will prompt the user for the directory they would like 
to save the file in as well as the name of the file The program 
should then prompt the user for their name, address, and phone number
Your program will write this data to a comma separated line in a file 
and store the file in the directory specified by the user"""

""" Once the data has been written program should read the file you just wrote 
to the file system and display the file contents to the user for validation purposes"""

# import OS library as well as OS path
import os
import os.path

# locate file path, and set user input to file_Name
file_Path = 'C:\\Users\\Justin\\Desktop\\python_work'

# prompt the user for the directory
os.listdir('.')
file_Directory = input('Please enter the directory name where you would like to save your file:')

# prompt the user for the file they would like to save in
file_Name = input('Please file name to be created: ')

# define the complete path 
completePath = file_Directory+file_Name


# check to see if file path exists
if os.path.isdir(file_Directory):
 print('Directory Exists')
else:
	print("Directory does not exist")
 
# create a new file


 # check to see if the complete path exists
if os.path.exists(completePath):
 print('Complete path is ', completePath)
else:
	print("No pathway")

with open (completePath, "w") as f:
# ask user for their name, address, and phone number
	name =(input('Please enter your name:  \n'))
	address = (input('Please enter your address:  \n'))
	phone =(input('Please enter your phone number:  \n'))
# print input, with name format then write to file in path.
	print(name.capitalize())
	print(address)
	print(phone)
	f.write(name)
	f.write(address)
	f.write(phone)


# open same file for reading
with open(completePath, 'r') as fileHandle:
 data = fileHandle.read() #read data from the file
 
# need to separate answers by comma 

 data = fileHandle.close() # file close
 
