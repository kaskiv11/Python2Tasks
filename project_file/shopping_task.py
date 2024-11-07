import time
from file_task import write_shopping_list


def add_product(shopping_list, file_path):
    product = input('Enter product name: ')
    quantity = int(input('Enter quantity: '))
    price = float(input('Enter price: '))
    shopping_list[product] = {'quantity': int(quantity), 'price': float(price)}
    print(f"Product {product} added to shopping")

    write_shopping_list(shopping_list, file_path)
    print(f"The product {product} has been added to file")


def view_shopping_list(shopping_list):
    count = 1
    for product, info in shopping_list.items():
        quantity = info['quantity']
        price = info['price']
        print(f"{count}. Product - {product}. Quantity - {quantity}. Price - {price}")
        count = count + 1


def update_product_name(shopping_list, file_path):
    old_name = input('Enter product name: ')
    if old_name in shopping_list:
        new_name = input('Enter new product name: ')
        shopping_list[new_name] = shopping_list.pop(old_name)
        write_shopping_list(shopping_list, file_path)
    else:
        print(f'Product {old_name} not found in shopping list')


def update_product_quantity(shopping_list, file_path):
    product = input('Enter product name: ')
    if product in shopping_list:
        new_quantity = int(input('Enter new quantity name: '))
        shopping_list[product]['quantity'] = new_quantity
        print("The product quantity has been updated")

        write_shopping_list(shopping_list, file_path)
    else:
        print(f'Product {product} not found in shopping list')


def update_product_price(shopping_list, file_path):
    product = input('Enter product name: ')
    if product in shopping_list:
        new_price = float(input('Enter new price: '))
        shopping_list[product]['price'] = new_price
        print("The product price has been updated")

        write_shopping_list(shopping_list, file_path)
    else:
        print(f'Product {product} not found in shopping list')


def edit_product(shopping_list, file_path):
    print("""       ----EDIT----
        1. Edit product name
        2. Edit product quantity
        3. Edit product price
    """)
    action = int(input('Select an option: '))
    if action == 1:
        update_product_name(shopping_list, file_path)
    elif action == 2:
        update_product_quantity(shopping_list, file_path)
    elif action == 3:
        update_product_price(shopping_list, file_path)
    else:
        print('Invalid an action')


def delete_product(shopping_list, file_path):
    product = input('Enter product name you want delete: ')
    if product in shopping_list:
        del shopping_list[product]
        print(f"The product {product} has been deleted")

        write_shopping_list(shopping_list, file_path)
    else:
        print(f'Product {product} not found in shopping list')


def select_option(shopping_list, file_path):
    while True:
        action = input('Do you want to add, view, edit, delete or exit? ')
        if action == 'add':
            add_product(shopping_list, file_path)
        elif action == 'view':
            view_shopping_list(shopping_list)
        elif action == 'edit':
            edit_product(shopping_list, file_path)
        elif action == 'delete':
            delete_product(shopping_list, file_path)
        elif action == 'exit':
            time.sleep(3)
            print('Goodbye!')
            break

