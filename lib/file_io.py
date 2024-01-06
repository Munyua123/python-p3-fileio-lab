def write_file(file_name, file_content):
    file_name_with_extension = f'{file_name}.txt'
    try:
        with open(file_name_with_extension, 'w') as file:
            file.write(file_content)
    except Exception as e:
        print(f"Error writing to file: {e}")
        raise
    

def append_file(file_name, append_content):
    file_name_with_extension = f'{file_name}.txt'
    try:
        with open(file_name_with_extension, 'a') as file:
            file.write(append_content)
    except Exception as e:
        print(f"Error appending to file: {e}")
        raise

def read_file(file_name):
    file_name_with_extension = f'{file_name}.txt'
    try:
        with open(file_name_with_extension, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{file_name_with_extension}' not found.")
        raise  
    except Exception as e:
        print(f"Error reading from file: {e}")
        raise
