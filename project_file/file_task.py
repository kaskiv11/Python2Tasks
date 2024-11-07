def read_shopping_list(file_path):
    shopping_list = {}
    with open(file_path, 'r') as f:
        for line in f:
            product, quantity, price = line.strip().split(',')
            shopping_list[product] = {'quantity': int(quantity), 'price': float(price)}
        return shopping_list


def write_shopping_list(shopping_list, file_path):
    with open(file_path, 'w') as f:
        for product, info in shopping_list.items():
            quantity = info['quantity']
            price = info['price']
            f.write(f"{product},{quantity},{price}\n")