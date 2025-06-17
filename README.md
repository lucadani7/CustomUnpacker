# CustomUnpacker
**Description:**  
This tool was created primarily for educational purposes — to better understand how custom archive formats work, including file headers, metadata, and binary I/O. It is not intended to replace existing solutions like `tar` or `zip`, but rather to explore the mechanics behind them. It supports creating archives, listing contents, and extracting specific or all files. Neither the zipFile library nor a third-party Python library have been used.

---

## ⚙️ Prerequisites

- **Python Version:** Ensure you have Python 3.10 or newer installed on your system. To check your Python version, open your terminal or command prompt and run:

  ```bash
  python --version
  ```
  OR

  ```bash
  python3 --version
  ```
- If the command returns a version number starting with 3.10 or higher (e.g., Python 3.10.4), you’re good to go. If not, you’ll need to install or update Python.

- Install Python 3.10 (if needed):

  - **Windows:** You can download and install Python 3.10 from the official Python website: [https://www.python.org/downloads/release/python-31015/](https://www.python.org/downloads/release/python-31015/). Alternatively, you can use the Windows Package Manager (winget) to install it:

    ```bash
    winget install -e --id Python.Python.3.10
    ```

    You can also use Chocolatey, if you have it installed on your system:

    ```bash
    choco install python310 -y
    ```
    
  - **macOS:** Download the latest Python 3.10 installer for macOS from the official Python website: [https://www.python.org/downloads/macos/](https://www.python.org/downloads/macos/). Alternatively, you can use Homebrew to install it:
 
    ```bash
    brew install python@3.10
    ```
 
  - **Linux:** On Linux, you can install Python 3.10 using your distribution's package manager. For example, on Ubuntu:

    ```bash
    sudo apt update && sudo apt install python3.10 -y
    ```

---

## 📦 Features

### 1. `create_archive(sources, archive_name)`
Creates an archive from the specified files or directories.

- **Parameters:**
  - `sources`: A directory or a list of files to include in the archive.
  - `archive_name`: The name of the archive to be created. For fewer problems, giving the archive's absolute path is recommended.

### 2. `list_content(archive_path)`
Lists all files within a specified archive.

- **Parameters:**
  - `archive_path`: The path to the archive whose contents you want to list. For fewer problems, giving the archive's absolute path is recommended.

### 3. `full_unpack(archive_path, destination_directory)`
Extracts all files from the specified archive to a destination directory.

- **Parameters:**
  - `archive_path`: The path to the archive to be extracted. For fewer problems, giving the archive's absolute path is recommended.
  - `destination_directory`: The directory where files will be extracted. For fewer problems, giving the destination directory's absolute path is recommended. If the destination directory does not exist, it will be created.

### 4. `unpack(archive_path, files_list, destination_directory)`
Extracts specified files from an archive to a destination directory.

- **Parameters:**
  - `archive_path`: The path to the archive to be extracted. For fewer problems, giving the archive's absolute path is recommended.
  - `files_list`: A list of files to extract.
  - `destination_directory`: The directory where files will be extracted. For fewer problems, giving the destination directory's absolute path is recommended. If the destination directory does not exist, it will be created. If a file does not exist in the list, it will be skipped. If a file exists in the list but not in the archive, the user will be warned.

---

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/lucadani7/CustomUnpacker.git
   cd CustomUnpacker
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 📟 Command-Line Usage

The project includes a main.py script that allows you to execute the functions from the CustomUnpacker class directly from the command line. For running the project, type in the command line `python3 main.py`, then press Enter key and then type the command you want to execute.

- **Available Commands:**
  -	create_archive: Create an archive with specified files.
  -	list_content: List the contents of an archive.
  -	full_unpack: Extract all files from an archive.
  -	unpack: Extract specified files from an archive.

- **Additional Commands:**
  -	help: Show this help message
  -	quit: Quit the program
 
- **Notes:**
  - The commands `help` and `quit` are handled internally and do not appear in the standard argparse usage block. However, when typing `help`, these additional commands will also be shown for clarity.
  - If you enter an unknown command (e.g., `hellokitty`), the tool will show the list of valid commands and remain active without quitting the program.
    
- **Examples:**
  -	Creating an archive:
    
    ```bash
   	create_archive -s file1.txt file2.txt -a archive_name
    ```
    
  -	Listing the contents of an archive:

    ```bash
    list_content -p archive_name
    ```
    
  -	Extracting all files from an archive:

    ```bash
    full_unpack -p archive_name -d ./output_dir
    ```
    
  -	Extracting specific files from an archive:
 
    ```bash
    unpack -p archive_name -f file1.txt file2.txt -d ./output_dir
    ```

---

## 🧩 Constants

**In the constants.py file, the following constants are defined:**
 -	HEADER_FORMAT: Specifies the format of the header for archived files. Defined as '256sI', meaning:
    -	256s: A string of exactly 256 bytes for storing the file name.
    -	I: An unsigned integer (4 bytes) for storing the file size.
 -	HEADER_SIZE: Dynamically computed size of the header using struct.calcsize(HEADER_FORMAT).

**These constants define the structure and size of each file header stored in the archive.**

---

## 📄 License

This project is licensed under the GPL-3.0 License.

---

## 📬 Contact & Feedback

If you have questions, suggestions, or would like to provide feedback about this project, feel free to reach out via email.

🔔 Important:
To ensure your message is read and not marked as spam, the email subject line must contain one of the following:
  -	 [CustomUnpacker] Questions – for inquiries about usage, issues, or technical help
  -	 [CustomUnpacker] Suggestions – for improvement ideas or feature requests
  -	 [CustomUnpacker] Feedback – for general impressions or thoughts on the project

❗ Emails without the correct subject line will be ignored and marked as spam.

📧 Email: lucaionescu1998@gmail.com
