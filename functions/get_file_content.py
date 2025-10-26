def get_file_content(working_directory, file_path):
    import os
    from config import MAX_CHARS

    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory.'
    if not os.path.isfile(target_dir):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        TRUNCATION_TEXT = f'[...File "{file_path}" truncated at 10000 characters]'

        with open(target_dir, "r") as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += TRUNCATION_TEXT
        return content
    except Exception as e:
        return f'Error reading file: {str(e)}'

