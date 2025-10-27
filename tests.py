from functions.write_file import write_file
from functions.run_python_file import run_python_file

def test():
    result = run_python_file("calculator", "main.py")
    print("Result for Calculators")
    print(result)

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Printing calc result")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print("this should be an error")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print("This should be an error")
    print(result)

    result = run_python_file("calculator", "lorem.txt")
    print("this should be an error")
    print(result)



if __name__ == "__main__":
    test()