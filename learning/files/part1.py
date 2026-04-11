# Open file


# r ==> read mode
# dangling pointer
# file = open("stocks.txt", mode="r") # file connection
# data = file.read() # reading data from file
# print(data)
# # logic crash
# file.close() # closing file connection

# best practice is with "with"

# with open("stocks.txt", mode="r") as file:
#     data = file.read()
#     print(data)

def parse_stock_data(stocks_data: list, headers: list) -> dict:
    stock_dict = {}
    for idx in range(len(headers)):
        key = headers[idx]
        value = stocks_data[idx]
        stock_dict[key] = value
    return stock_dict


with open("stocks.txt", mode="r") as file:
    headers = None
    stock_live_data = []
    for line in file:
        if headers is None:
            headers = line.strip().split("|")
        else:
            stocks_data = line.strip().split("|")
            data_dict = parse_stock_data(stocks_data, headers)
            stock_live_data.append(data_dict)

# print(stock_live_data)
# for data in stock_live_data:
#     print(data)

