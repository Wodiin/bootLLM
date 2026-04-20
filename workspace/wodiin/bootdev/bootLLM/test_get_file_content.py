from functions.get_file_content import get_file_content

def test_get_file_content():
    
    result_test_alpha = get_file_content("calculator", "lorem.txt")
    print(f"Length: {len(result_test_alpha)}")
    print(f"End: ...{result_test_alpha[-100:]}")

    result_test_1 = get_file_content("calculator", "main.py")
    print(result_test_1)
    result_test_2 = get_file_content("calculator", "pkg/calculator.py")
    print(result_test_2)
    result_test_3 = get_file_content("calculator", "/bin/cat")
    print(result_test_3)
    result_test_4 = get_file_content("calculator", "does_not_exist.py")
    print(result_test_4)

test_get_file_content()