import pathlib
import shutil

# Get the current working directory
path = pathlib.Path.cwd()
print("This is the current working directory: ", path)

# Create a folder named 'folder_week11'
folder_path = path / "folder_week11"
folder_path.mkdir(exist_ok=True)

# Define the path for 'week11.txt' inside the new folder
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

# Create a subdirectory named 'file_backups' for the backup file
backup_dir = folder_path / "file_backups"
backup_dir.mkdir(exist_ok=True)

# Copy the file as 'week11_backup.txt' into the backup directory
backup_file = backup_dir / "week11_backup.txt"
shutil.copy(week11_file, backup_file)

# Search for and print all .txt files inside folder_week11 and its subdirectories
print("These are all the found text files within the directories:")
for txt_file in folder_path.rglob("*.txt"):
    print(txt_file)
