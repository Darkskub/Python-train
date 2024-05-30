import pytest


def merge_and_write(file1_path, file2_path, output_file_path):
    try:
        with open(file1_path, "r") as file1:
            data1 = file1.read().strip()

        with open(file2_path, "r") as file2:
            data2 = file2.read().strip()

        merged_data = data1 + " " + data2

        with open(output_file_path, "w") as output_file:
            output_file.write(merged_data)

        with open(output_file_path, "r") as output_file:
            data = output_file.read()
        return data
    except FileNotFoundError:
        return "Один из файлов не найден"


@pytest.fixture
def test_create_files(tmpdir):
    file1 = tmpdir.join("file1.txt")
    file2 = tmpdir.join("file2.txt")
    output_file = tmpdir.join("output.txt")

    file1.write("Some text 1")
    file2.write("Some text 2")

    return file1, file2, output_file


def test_merge_and_write(test_create_files):
    file1, file2, output_file = test_create_files
    expected_data = "Some text 1 Some text 2"

    result = merge_and_write(str(file1), str(file2), str(output_file))

    assert result == expected_data


def test_file_not_found():
    file1_path = "nonexistent_file1.txt"
    file2_path = "nonexistent_file2.txt"
    output_file_path = "output.txt"

    result = merge_and_write(file1_path, file2_path, output_file_path)

    assert result == "Один из файлов не найден"
