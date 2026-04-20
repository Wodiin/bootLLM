import os
import google.genai.types as types

def write_file(working_directory, file_path, content):
    try:
        # Get the absolute path of the working directory
        abs_path = os.path.abspath(working_directory)

        # Normalize the target file path and ensure it's within the working directory
        target_file = os.path.normpath(os.path.join(abs_path, file_path))

        # Check if the target file is a subdirectory of the working directory
        valid_target_file = os.path.commonpath([abs_path, target_file]) == abs_path

        # If the target file is not valid (i.e., it's outside the working directory), return an error message
        if not valid_target_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        # Check if the target file already exists and is a directory
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        # Ensure the target directory exists
        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        # Write the content to the target file
        with open(target_file, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


    except Exception as e:
        return f"Error: {str(e)}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path", "content"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write to, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            )
        }
    )
)
