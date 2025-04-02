# File Read & Write Challenge

import os
from utils.file_operations import read_file, write_file

def main():
    # Prompt user for the filenameDes
    input_filename = input("Please enter the filename to read: ")
    
    try:
        # Read the content of the file
        content = read_file(input_filename)
        
        # Modify the content (for example, converting to uppercase)
        modified_content = content.upper()
        
        # Define the output filename
        output_filename = f"modified_{os.path.basename(input_filename)}"
        
        # Write the modified content to a new file
        write_file(output_filename, modified_content)
        
        print(f"Modified content has been written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' cannot be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()