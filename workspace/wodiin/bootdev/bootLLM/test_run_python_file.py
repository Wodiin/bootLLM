from functions.run_python_file import run_python_file

def test_run_python_file():

    result_test_1 = run_python_file("calculator", "main.py")
    print(result_test_1)
    result_test_2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result_test_2)
    result_test_3 = run_python_file("calculator", "tests.py")
    print(result_test_3)
    result_test_4 = run_python_file("calculator", "../main.py")
    print(result_test_4)
    result_test_5 = run_python_file("calculator", "nonexistent.py")
    print(result_test_5)
    result_test_6 = run_python_file("calculator", "lorem.txt")
    print(result_test_6)

test_run_python_file()