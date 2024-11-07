words = ["hello", "world", "python"]

upper_words = list(map(lambda x: x.upper(), words))

print(upper_words)

numbers = [1, 2, -3, 4, 5, -6]

even_numbers = list(filter(lambda x: x > 0, numbers))
print(even_numbers)

count_words = list(map(lambda x: len(x), words))
print(count_words)

names = ["Greg", "Greg", "Chris", "Toby", "Fred", "David", "David"]

unique_names = list(filter(lambda x: names.count(x) == 1, names ))
print(unique_names)

full_names = list(map(lambda name: f"Pawliv {name}", unique_names))
print(full_names)

products = [
    {"name": "apple", "price": 5, "quantity": 20},
    {"name": "banana", "price": 10, "quantity": 25},
    {"name": "kiwi", "price": 21, "quantity": 17}
]


price_threshold = 8

filtered_products = list(filter(lambda product: product["price"] >= price_threshold, products))

print(filtered_products)

transform_product = list(map(lambda product: {"name": product["name"], "quantity": product["quantity"]}, filtered_products))

print(transform_product)