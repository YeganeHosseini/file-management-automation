import os
import shutil
import argparse

FILE_TYPES = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.7z', '.tar'],
}

def organize_files(directory):
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()

            for folder_name, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    folder_path = os.path.join(directory, folder_name)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    print(f"Moved: {filename} --> {folder_name}")
                    break
            else:
                other_folder = os.path.join(directory, 'Others')
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"Moved: {filename} --> Others")

if __name__ == "__main__":
    # Set up argparse for command-line arguments
    parser = argparse.ArgumentParser(description="Organize files in a directory by their file type.")
    parser.add_argument('directory', type=str, help="The path to the directory to organize")
    args = parser.parse_args()

    # Call the function to organize the files
    organize_files(args.directory)
