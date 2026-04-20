import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try: 
        # Get the absolute path of the working directory
        abs_path = os.path.abspath(working_directory)

        # Normalize the target file path and ensure it's within the working directory
        target_file = os.path.normpath(os.path.join(abs_path, file_path))

        # Check if the target file is a subdirectory of the working directory
        valid_target_file = os.path.commonpath([abs_path, target_file]) == abs_path

        # If the target file is not valid (i.e., it's outside the working directory), return an error message
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # Check if the target file exists and is a regular file
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        # Check if the target file is a Python file
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        # Run the Python file using subprocess
        command = ['python', target_file]

        # If additional arguments are provided, add them to the command
        if args:
             command.extend(args)
        
        # Run the command and capture the output
        completed_process = subprocess.run(command,cwd=abs_path, capture_output=True, text=True, timeout=30)

        # Prepare the result based on the process output
        result = ""
        if not completed_process.stdout and not completed_process.stderr:
            result += "No output produced"
        if completed_process.stdout:
            result += f"STDOUT: {completed_process.stdout}\n"
        if completed_process.stderr:
            result += f"STDERR: {completed_process.stderr}\n"
        if completed_process.returncode != 0:
            result += f"Process exited with code {completed_process.returncode}"
        return result
    
    except Exception as e:
        return f"Error: executing Python file: {str(e)}"