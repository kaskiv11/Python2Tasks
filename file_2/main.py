import csv

with open('data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == "Banana":
            row[2] = 45.3


data = [
    ["Name", "Count", "Price"],
    ["Banana", 100, 59.5],
    ["Apple", 80, 40.3]
]

with open('data.csv', mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)


with open('data.csv', mode="r", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Name'], row['Count'], row['Price'])


data_new = [
    ["Kiwi", 90, 109.5],
    ["peach", 70, 87.3]
]

with open('data.csv', mode="a", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_new)

print("\n")
with open('data.csv', mode="r", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if float(row["Price"]) >= 85:
            print(row["Name"], row["Count"], row["Price"])


def change_price(file_name, name_product, new_price):
    with open(file_name, mode="r", newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"] == name_product:
                row["Price"] = new_price
            data_file.append(row)


def write_to_file_csv(file_name):
    with open(file_name, mode="w", newline='') as file:
        fieldnames = ["Name", "Count", "Price"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_file)


file = "data.csv"
name_product = input("Enter name of product: ")
new_price = input("Enter the new price")

data_file = []
change_price(file, name_product, new_price)
write_to_file_csv(file)
