import os

# Specify the directory path
directory_path = "/"  # Change this to your directory

# Get the list of entries in the directory
try:
    contents = os.listdir(directory_path)
    print("Contents of the directory:", contents)
except FileNotFoundError:
    print(f"The directory {directory_path} does not exist.")
except PermissionError:
    print(f"Permission denied to access {directory_path}.")
