"""

NOTE: If your file or folder is in current directory then use relative path or use absolute path. 

File handling in Python allows you to read, write, and manipulate files on the filesystem. Python provides built-in functions and libraries to work with files

1. Opening a File
To work with a file, you first need to open it using Python's open() function. 
The basic syntax is:
file_object = open('filename', 'mode')

Here, 'filename' is the name of the file you want to open, and 'mode' specifies the operation you want to perform on the file. The different modes are:
'r' - Read (default mode). Opens the file for reading.
'w' - Write. Opens the file for writing (creates a new file if not exists or truncates(empty) an existing file).
'a' - Append. Opens the file for appending (creates the file if it doesn't exist).
#optional('b' & 'x')
'b' - Binary mode. For reading or writing binary files (e.g., images).
'x' - Exclusive creation. Creates a new file, but fails if the file already exists.

Example:
file = open('example.txt', 'r')  # Open the file in read mode


2. Reading from a File
After opening a file in the read mode, you can read its contents using various methods:
read() or read(size) or read(numOfCharecter) - Reads the entire file or up to the specified number of bytes or read the specified number of charecter.
readline() - Reads the next line of the file.
readlines() - Reads all lines in a file and returns them as a list.

Example:
file = open('example.txt', 'r')

# Read the entire file
content = file.read()
print(content)

# Read one line at a time
line = file.readline()
print(line)

# Read all lines into a list
lines = file.readlines()
print(lines)

file.close()

NOTE: you should always close a file after opening by using file.close() method.

3. Writing to a File

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

4. Delete a File
To delete a file, you must import the OS module, and run its os.remove() function:
eg:-
import os
os.remove("demofile.txt")

To avoid getting an error, you might want to check if the file exists before you try to delete it:
eg:-
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

To delete an entire folder, use the os.rmdir() method:
eg:-
import os
os.rmdir("myfolder")


**BONUS: To get the current directory using os module use os.getcwd()
Example:
import os
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

"""
