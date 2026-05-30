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


def get_category(file_extension):
    for category, extensions in CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category

    return "Others"


def get_unique_path(destination_path):
    if not os.path.exists(destination_path):
        return destination_path

    folder = os.path.dirname(destination_path)
    file_name = os.path.basename(destination_path)
    name, extension = os.path.splitext(file_name)

    counter = 1

    while True:
        new_file_name = f"{name}_{counter}{extension}"
        new_path = os.path.join(folder, new_file_name)

        if not os.path.exists(new_path):
            return new_path

        counter += 1


def organize_files():
    print("File Organizer started!")

    files = os.listdir(TARGET_FOLDER)

    for file in files:
        file_path = os.path.join(TARGET_FOLDER, file)

        if os.path.isdir(file_path):
            continue

        file_name, file_extension = os.path.splitext(file)

        category_found = get_category(file_extension)

        category_folder = os.path.join(TARGET_FOLDER, category_found)

        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        destination_path = os.path.join(category_folder, file)
        destination_path = get_unique_path(destination_path)

        shutil.move(file_path, destination_path)

        print(f"Moved: {file} -> {category_found}")


if __name__ == "__main__":
    organize_files()