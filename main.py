import os
import shutil
import sys

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Spreadsheets": [".xlsx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Audios": [".mp3", ".wav"],
    "Compressed": [".zip", ".rar", ".7z"],
}


def get_target_folder():
    if len(sys.argv) < 2:
        print("Usage: py main.py <folder_path>")
        sys.exit(1)

    target_folder = sys.argv[1]

    if not os.path.exists(target_folder):
        print(f"Error: folder not found: {target_folder}")
        sys.exit(1)

    if not os.path.isdir(target_folder):
        print(f"Error: path is not a folder: {target_folder}")
        sys.exit(1)

    return target_folder


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


def organize_files(target_folder):
    print("File Organizer started!")

    files = os.listdir(target_folder)
    moved_files = 0

    for file in files:
        file_path = os.path.join(target_folder, file)

        if os.path.isdir(file_path):
            continue

        file_name, file_extension = os.path.splitext(file)

        category_found = get_category(file_extension)

        category_folder = os.path.join(target_folder, category_found)

        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        destination_path = os.path.join(category_folder, file)
        destination_path = get_unique_path(destination_path)

        shutil.move(file_path, destination_path)

        moved_files += 1

        print(f"Moved: {file} -> {category_found}")

    if moved_files == 0:
        print("No files to organize.")
    else:
        print(f"Done! {moved_files} file(s) organized.")


if __name__ == "__main__":
    folder = get_target_folder()
    organize_files(folder)