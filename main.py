import os
import shutil

TARGET_FOLDER = "test_folder"

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Spreadsheets": [".xlsx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Audios": [".mp3", ".wav"],
    "Compressed": [".zip", ".rar", ".7z"],
}

print("File Organizer started!")

files = os.listdir(TARGET_FOLDER)

for file in files:
    file_path = os.path.join(TARGET_FOLDER, file)

    if os.path.isdir(file_path):
        continue

    file_name, file_extension = os.path.splitext(file)

    category_found = "Others"

    for category, extensions in CATEGORIES.items():
        if file_extension.lower() in extensions:
            category_found = category

    category_folder = os.path.join(TARGET_FOLDER, category_found)

    if not os.path.exists(category_folder):
        os.makedirs(category_folder)

    destination_path = os.path.join(category_folder, file)

    shutil.move(file_path, destination_path)

    print(f"Moved: {file} -> {category_found}")