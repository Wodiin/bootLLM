from functions.get_files_info import get_files_info

def test_get_files_info():
    result_test_1 = get_files_info("calculator", ".")
    print(f"Result for current directory:\n {result_test_1}")
    result_test_2 = get_files_info("calculator", "pkg")
    print(f"Result for 'pkg' directory:\n {result_test_2}")
    result_test_3 = get_files_info("calculator", "/bin")
    print(f"Result for '/bin' directory:\n {result_test_3}")
    result_test_4 = get_files_info("calculator", "../")
    print(f"Result for '../' directory:\n {result_test_4}")

test_get_files_info()