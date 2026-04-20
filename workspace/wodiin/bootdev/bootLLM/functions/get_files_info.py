import os
import google.genai.types as types

def get_files_info(working_directory, directory="."):
    
    # Get the absolute path of the working directory
    abs_path = os.path.abspath(working_directory)

    # Normalize the target directory path and ensure it's within the working directory
    target_dir = os.path.normpath(os.path.join(abs_path, directory))

    # Check if the target directory is a subdirectory of the working directory
    valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path

    # If the target directory is not valid (i.e., it's outside the working directory), return an error message
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # Check if the target directory exists and is a directory
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory' 

   # Attempt to list the contents of the target directory and gather information about each item 
    try:
        filenames = os.listdir(target_dir)
        lines = []

        # Iterate through each item in the target directory and gather information
        for filename in filenames:
            item_path = os.path.join(target_dir, filename)
            item_size = os.path.getsize(item_path)
            is_item_directory = os.path.isdir(item_path)
            lines.append(f"- {filename}: file_size={item_size} bytes, is_dir={is_item_directory}")
        return "\n".join(lines)

    # Handle any exceptions that may occur during the process and return an error message
    except Exception as e:
            return f"Error: {str(e)}"


# Define the function schema for get_files_info to be used in the Gemini API
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
                ),
            },
        ),
    )
