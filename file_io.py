# This program will import pathlib and shutil modules
# Create a path object that shows the current working directory
# Print the current path
# Reference the CWD create a new path obj that will be used to create a new folder called folder_week11
# Create a new directory using the previous path created
# Using the path created make a folder week 11 directory and create a path that will be used to create a text file named week11.txt
# Use the method touch to create the week11.txt as a blank file
# Print file contents using read() method to confirm text written
# Make a new path in the folder week 11 directory called file backups
# Make a new directory referecing the new path in the prior step
# Using the shutil module make a copy of week11.txt file called week11 backup.txt and save it withint he file backups directory
# Navigate back to folder 11 directory
# From folder week 11 use rglob() method to printo out only the txt files that have been created in this directory and subdirectories

# import pathlib and shutil
import pathlib
import shutil

# Get the current working directory
path = pathlib.Path.cwd()
print("This is the current working directory: ", path)

# Create a folder named folder_week11
folder_path = path / "folder_week11"
folder_path.mkdir(exist_ok=True)

# Define the path for week11.txt inside the new folder
week11_file = folder_path / "week11.txt"

# Create an empty text file
week11_file.touch()

# Write a test message to the file
file = week11_file.open(mode='a', encoding='utf-8')
lines = ["Test: Writing to file.\n"]
file.writelines(lines)
file.close()

# Read and print the file's contents
file = week11_file.open(mode='r', encoding='utf-8')
print(file.read())
file.close()

# Create a subdirectory named file_backups for the backup file
backup_dir = folder_path / "file_backups"
backup_dir.mkdir(exist_ok=True)

# Copy the file as week11_backup.txt into the backup directory
backup_file = backup_dir / "week11_backup.txt"
shutil.copy(week11_file, backup_file)

# Search for and print all .txt files inside folder_week11 and its subdirectories
print("These are all the found text files within the directories:")
for txt_file in folder_path.rglob("*.txt"):
    print(txt_file)
