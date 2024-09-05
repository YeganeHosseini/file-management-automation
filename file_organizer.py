import os
import shutil

# Dictionary to map file types to directories
FILE_TYPES = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.7z', '.tar'],
}

def organize_files(directory):
    """
    Organize files into folders based on their file type.
    
    :param directory: The path of the directory to organize
    """
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            
            # Find the appropriate folder for the file type
            for folder_name, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    folder_path = os.path.join(directory, folder_name)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)  # Create folder if it doesn't exist
                    
                    # Move the file into the appropriate folder
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    print(f"Moved: {filename} --> {folder_name}")
                    break
            else:
                # If file type doesn't match any in the list, move to 'Others'
                other_folder = os.path.join(directory, 'Others')
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"Moved: {filename} --> Others")

if __name__ == "__main__":
    folder_to_organize = input("Enter the directory path to organize: ")
    organize_files(folder_to_organize)

