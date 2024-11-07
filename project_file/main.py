from shopping_task import select_option
from file_task import read_shopping_list


def main():
    file_path = "shopping_list.txt"

    select_option(read_shopping_list(file_path), file_path)


if __name__ == '__main__':
    main()
