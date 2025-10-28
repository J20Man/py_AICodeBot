from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                )
            }
        )
)

schema_get_file_content = types.FunctionDeclaration(
        name="get_file_content",
        description="Reads file content, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "filename": types.Schema(
                    type=types.Type.STRING,
                    description="The Contents of the file, contained within the working directory"
                )
            }
    )
    
)

schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description="Runs a python file, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "filename": types.Schema(
                    type=types.Type.STRING,
                    description="Runs the specified Python file only.",
                )
            }
        )
)

schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="Writes a file, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "filename": types.Schema(
                    type=types.Type.STRING,
                    description="Writes a specific file, contained within the working directory"
                ),
                "contents": types.Schema(
                    type=types.Type.STRING,
                    description="The contents to write to the file."
                )
                
            }
        )
)

