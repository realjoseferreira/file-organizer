import os
import shutil
import argparse
from datetime import datetime

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Spreadsheets": [".xlsx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Audios": [".mp3", ".wav"],
    "Compressed": [".zip", ".rar", ".7z"],
}


def get_target_folder():
    parser = argparse.ArgumentParser(
        description="Organize files into folders based on their extensions."
    )

    parser.add_argument(
        "folder_path",
        help="Path to the folder you want to organize"
    )

    args = parser.parse_args()
    target_folder = args.folder_path

    if not os.path.exists(target_folder):
        print(f"Error: folder not found: {target_folder}")
        exit(1)

    if not os.path.isdir(target_folder):
        print(f"Error: path is not a folder: {target_folder}")
        exit(1)

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


def write_log(message):
    logs_folder = "logs"

    if not os.path.exists(logs_folder):
        os.makedirs(logs_folder)

    log_path = os.path.join(logs_folder, "organization_log.txt")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{current_time}] {message}\n")


def organize_files(target_folder):
    start_message = "File Organizer started!"
    print(start_message)
    write_log(start_message)

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

        message = f"Moved: {file} -> {category_found}"
        print(message)
        write_log(message)

    if moved_files == 0:
        message = "No files to organize."
        print(message)
        write_log(message)
    else:
        message = f"Done! {moved_files} file(s) organized."
        print(message)
        write_log(message)


if __name__ == "__main__":
    folder = get_target_folder()
    organize_files(folder)