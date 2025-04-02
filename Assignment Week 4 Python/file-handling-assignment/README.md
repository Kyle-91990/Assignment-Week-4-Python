# File Handling Assignment

## Overview
This project is designed to enhance your skills in file handling and error management in Python. It includes a program that reads a file, modifies its content, and writes the modified content to a new file. The project also emphasizes robust error handling to gracefully manage issues such as non-existent files or read/write permissions.

## Project Structure
```
file-handling-assignment
├── src
│   ├── main.py
│   └── utils
│       └── file_operations.py
├── tests
│   └── test_file_operations.py
├── requirements.txt
└── README.md
```

## Instructions
1. **Clone the repository** to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies listed in `requirements.txt` using:
   ```
   pip install -r requirements.txt
   ```
4. Run the application by executing the `main.py` file:
   ```
   python src/main.py
   ```

## Error Handling
The application includes comprehensive error handling to manage various file-related issues:
- If the specified file does not exist, the program will notify the user and prompt for a new filename.
- If the file cannot be read due to permission issues, an appropriate error message will be displayed.
- The program ensures that any errors encountered during file operations are handled gracefully, allowing for a smooth user experience.

