from functions.write_file import write_file

def test_write_file():
    result_test_1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result_test_1)
    result_test_2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result_test_2)
    result_test_3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result_test_3)

test_write_file()