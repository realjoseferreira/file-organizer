import os

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
    file_name, file_extension = os.path.splitext(file)

    category_found = "Others"

    for category, extensions in CATEGORIES.items():
        if file_extension.lower() in extensions:
            category_found = category

    print(f"File: {file} | Category: {category_found}")