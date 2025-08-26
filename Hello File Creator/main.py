"""
Version --> 1.0.0

This script is used to create 'n' number of empty TEXT files following the naming scheme (Eg:'file1.txt,file2.txt,...) provided by the user.

Step 1 : take input for the naming scheme to follow
Step 2 : take input for the number of files to create.
Step 3 : Create/files based on user input

"""
file_name = input("Enter file name for the file/files to be created : ")
file_type = input("Enter filetype for file 'txt/md' : ")
num_of_files = int(input("How many files should be created? "))

for num in range(1,num_of_files+1):
    file = open(f"{file_name}{num}.{file_type}","x")


