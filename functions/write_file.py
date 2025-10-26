def write_file(working_directory, file_path, content):
    import os

    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    target_dir = os.path.dirname(target_file)

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        if not os.path.exists(target_dir):
            os.makedirs(target_dir, exist_ok=True)

        with open(target_file, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
   
    except Exception as e:
        return f'Error reading file: {str(e)}'


