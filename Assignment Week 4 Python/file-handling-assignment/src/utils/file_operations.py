def read_file(filename):
    """Reads the content of a file and returns it."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except IOError:
        print(f"Error: The file '{filename}' cannot be read.")
        return None

def write_file(filename, content):
    """Writes content to a specified file."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
    except IOError:
        print(f"Error: The file '{filename}' cannot be written.")