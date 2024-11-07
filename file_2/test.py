import math


def power(a, b):
    return math.pow(a, b)


print(power(2, 5))

file = "my_file.txt"
with open(file, "r", encoding="utf-8") as f:
    print(f.read())


with open(file, "w", encoding="UTF-8") as f:
    f.write("Я займаюсь на ментоській годині")

with open(file, "a", encoding="UTF-8") as f:
    f.write("\nЯ спати")


sum = lambda a, b: a+b


print(sum(10, 30))


numbers = input("Enter numbers through space: ").split()
numbers = [int(number) for number in numbers]

squared = list(map(lambda x: x ** 2, numbers))
print(squared)

div_3 = list(filter(lambda x: x%3 == 0, numbers))
print(div_3)

products = [
    {"name": "apple", "price": 10, "quantity": 20},
    {"name": "mango", "price": 43, "quantity": 30},
    {"name": "banana", "price": 37, "quantity": 50}
]
min_price = 15
max_price = 40

filtered_products = list(filter(lambda product: product["price"] > min_price and product["price"] < max_price, products))
print(filtered_products)