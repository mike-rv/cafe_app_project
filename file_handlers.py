import csv


def is_csv_empty(csv_file):
    with open(csv_file) as csv_file_reader:
        reader = csv.reader(csv_file_reader)
        for row, _ in enumerate(reader):
            if row:
                return False
    return True


if is_csv_empty("products.csv"):
    products_list = []
else:
    with open("products.csv") as csv_file:
        products_list = [
            {k: v for k, v in row.items()} for row in csv.DictReader(csv_file)
        ]

if is_csv_empty("couriers.csv"):
    couriers_list = []
else:
    with open("couriers.csv") as csv_file:
        couriers_list = [
            {k: v for k, v in row.items()} for row in csv.DictReader(csv_file)
        ]

if is_csv_empty("orders.csv"):
    orders_list = []
else:
    with open("orders.csv") as csv_file:
        orders_list = [
            {k: v for k, v in row.items()} for row in csv.DictReader(csv_file)
        ]
