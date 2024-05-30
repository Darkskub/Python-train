def write_text_to_file(text, file_name):
    with open(file_name, "a+") as file:
        file.write(text + "\n")


def print_even_lines(file_name):
    global i
    with open(file_name, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        if i % 2 != 0:
            print(lines[i].strip())


write_text_to_file("Some text", "3.txt")

print_even_lines("3.txt")
