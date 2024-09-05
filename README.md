
# File Management Automation Script

This Python script automates the organization of files in a specified directory by categorizing files based on their extensions. The script moves files into corresponding subfolders (e.g., "Documents", "Images", "Music"). Unknown file types are moved into an "Others" folder.

## Features

- **Organize files by type**: Files are categorized into folders like `Documents`, `Images`, `Music`, etc.
- **Unknown file handling**: Files with unrecognized extensions are moved to an `Others` folder.
- **Folder creation**: If a folder for a file type does not exist, it is created automatically.
- **Logging**: The script logs all file movements and errors to a log file (`file_organizer.log`).
- **Command-line arguments**: The directory to organize is passed as a command-line argument for flexibility.
- **Scheduled execution**: The script can be scheduled to run periodically using Task Scheduler (Windows) or cron (Linux/macOS).

## Supported File Types

| Category   | Extensions                        |
|------------|------------------------------------|
| Documents  | `.pdf`, `.docx`, `.txt`, `.xlsx`   |
| Images     | `.jpg`, `.jpeg`, `.png`, `.gif`    |
| Videos     | `.mp4`, `.mov`, `.avi`             |
| Music      | `.mp3`, `.wav`, `.aac`             |
| Archives   | `.zip`, `.rar`, `.7z`, `.tar`      |

## Prerequisites

- **Python 3.x**: Ensure that Python 3.x is installed.
- **argparse**: Command-line arguments support is provided by the built-in argparse library.
- **Logging**: Built-in logging for tracking file movements.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YeganeHosseini/task-manager-api.git
   cd file-management-automation
   ```

2. **Set up a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   Since this script only uses built-in Python libraries, no additional packages are required. However, you can create a `requirements.txt` if needed for future use.

## Usage

### Run the Script with Command-Line Arguments

Run the script by passing the directory to be organized as a command-line argument:

```bash
python file_organizer.py /path/to/directory
```

For example:

```bash
python file_organizer.py C:\Users\yegan\Downloads
```

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

### Logging

All file movements and errors are logged in `file_organizer.log`. This log file records details about which files were moved and where, along with timestamps.

### Scheduling the Script

the script can be scheduled to run periodically.

#### Windows Task Scheduler

1. Create a `.bat` file to automate the execution:
   ```bat
   @echo off
   cd C:\path\to\your\project
   venv\Scripts\activate
   python file_organizer.py C:\path\to\directory
   ```

2. Open Task Scheduler, create a new task, and select the `.bat` file to run on your desired schedule (e.g., daily, weekly).

#### Linux/macOS cron

1. Open crontab to schedule the script:
   ```bash
   crontab -e
   ```

2. Add the following cron job to run the script every day at 2 AM:
   ```bash
   0 2 * * * /usr/bin/python3 /path/to/your/project/file_organizer.py /path/to/directory
   ```

### Optional Features

- **Command-line arguments**: Use argparse to pass the directory path as an argument.
- **Logging**: The script logs all file movements in a `.log` file.
- **Scheduled execution**: Use Task Scheduler (Windows) or cron (Linux/macOS) to run the script periodically.

## License

This project is licensed under the MIT License.