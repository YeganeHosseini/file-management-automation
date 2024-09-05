
# File Management Automation Script

This Python script automates the process of organizing files in a specified directory. It categorizes files by their extensions and moves them into corresponding subfolders (e.g., "Documents", "Images", "Music"). If a file's type is unrecognized, it is moved to an "Others" folder.

## Features

- **Organize files by type**: Files are categorized and moved into folders like `Documents`, `Images`, `Videos`, etc.
- **Unknown file handling**: Files with unknown extensions are moved into an `Others` folder.
- **Folder creation**: If a folder for a file type does not exist, it is created automatically.

## Supported File Types

| Category   | Extensions                        |
|------------|------------------------------------|
| Documents  | `.pdf`, `.docx`, `.txt`, `.xlsx`   |
| Images     | `.jpg`, `.jpeg`, `.png`, `.gif`    |
| Videos     | `.mp4`, `.mov`, `.avi`             |
| Music      | `.mp3`, `.wav`, `.aac`             |
| Archives   | `.zip`, `.rar`, `.7z`, `.tar`      |

## Prerequisites

- Python 3.x
- (Optional) `argparse` for command-line argument support (included in `requirements.txt`).

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YeganeHosseini/file-management-automation.git
   cd file-management-automation
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script in your terminal:
   ```bash
   python file_organizer.py
   ```

2. Enter the full directory path that you want to organize when prompted:
   ```bash
   Enter the directory path to organize: C:\path\to\your\directory
   ```

3. The script will automatically move files into categorized folders.

### Example

If you have files like `document.pdf`, `picture.jpg`, and `song.mp3` in your Downloads folder, after running the script:

```
Downloads/
├── Documents/
│   └── document.pdf
├── Images/
│   └── picture.jpg
├── Music/
│   └── song.mp3
```

### Future work


- **Command-line arguments**: Use the `argparse` library to pass the directory as a command-line argument.
- **Logging**: Record the actions taken by the script (i.e., which files were moved) into a `.log` file.
- **Scheduled Execution**: Set up the script to run periodically using task schedulers like `cron` (Unix) or Task Scheduler (Windows).

## License

This project is licensed under the MIT License.

