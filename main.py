import os

TARGET_FOLDER = "test_folder"

print("File Organizer started!")

files = os.listdir(TARGET_FOLDER)

for file in files:
    file_name, file_extension = os.path.splitext(file)

    print(f"File {file_name} | Extension: {file_extension}")