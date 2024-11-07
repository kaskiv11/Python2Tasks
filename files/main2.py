


list_programing = ["Python", "C++", "JavaScript", "Java", "PHP"]


with open('file.txt', 'w', encoding='utf-8') as file:
    file.write(", ".join(list_programing))


with open('file.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print(data)


with open('file2.txt', 'w', encoding='utf-8') as file:
    file.write(data)


def read_my_file(file):
    with open(file, 'r', encoding='utf-8') as file:
        print(file.read())


read_my_file("main.py")
read_my_file("file2")

