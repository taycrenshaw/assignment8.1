import json

def get_name_of_directory():
    """Prompt user for name of the directory they want to save the file to."""
    filename = 'directoryName.json'
    try:
        with open(filename) as f_obj:
            directoryName = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return directoryName

def file_name():
    """Prompt user for name of the file they want to save to the directory."""
    filename = 'fileName.json'
    try:
        with open(filename) as f_obj:
            fileName = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return fileName
