import os
import config

def get_file_content(working_directory, file_path):
    try:
        # Get the absolute path of the working directory
        abs_path = os.path.abspath(working_directory)

        # Normalize the target file path and ensure it's within the working directory
        target_file = os.path.normpath(os.path.join(abs_path, file_path))

        # Check if the target file is a subdirectory of the working directory
        valid_target_file = os.path.commonpath([abs_path, target_file]) == abs_path

        # If the target file is not valid (i.e., it's outside the working directory), return an error message
        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_file, 'r') as f:
            content = f.read(config.MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {config.MAX_CHARS} characters]'
        return content
    except Exception as e:
        return f"Error: {str(e)}"