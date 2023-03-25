import os

# Set the paths to the two folders
folder1_path = './downloaded_latest_chrome'
folder2_path = './extracted_latest_chrome'

# List the files in each folder
folder1_files = set(os.listdir(folder1_path))
folder2_files = set(os.listdir(folder2_path))

# Find files with the same name in both folders
common_files = folder1_files.intersection(folder2_files)

count = 0
# Delete files with the same name from folder1
for file in common_files:
    count += 1
    file_path = os.path.join(folder1_path, file)
    try:
        os.remove(file_path)
        print(f"Deleted file: {file_path}")
    except Exception as e:
        print(f"Error deleting file: {file_path} - {e}")

print("Completed deleting files with the same name.")
print(count)