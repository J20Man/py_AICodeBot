def run_python_file(working_directory, file_path, args=[]):
    import os
    import subprocess

    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    target_dir = os.path.dirname(target_file)

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'
    if not target_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result_file = subprocess.run(
            ["python", target_file, *args],
            timeout=30,
            capture_output=True,
            text=True
        )

        if not result_file.returncode == 0:
            return f'Process exited with code {result_file.returncode}'
        if result_file.stderr == "" and result_file.stdout == "":
            return 'No output produced'

        return f'STDOUT:{result_file.stdout} STDERR:{result_file.stderr}'

    except Exception as e:
        return f'Error: executing Python file:  {str(e)}'
