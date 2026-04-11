# error if file not exist
# this mode overwrite the old data

def export_order(orders: list, file):
    for order in orders:
        file.write(order + "\n")

def main():
    with open('report.txt', 'w') as file:
        orders = [
            "Breed",
            "JAM",
            "Jean",
            "PAN",
            "Book",
        ]
        export_order(orders, file)

main()