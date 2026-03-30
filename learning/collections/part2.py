"""
Data: {
    "symbol": "AAPL",
    "date": "2018-09-21",
    "open": 23.5,
    "high": 23.5,
    "low": 23.5,
    "close": 23.5
}
"""
"""
HDFC --> list of record [ {"date": "2018-09-21",  "open": 23.5,...}, ]
"""
# Symbol --> date, open, high, low, close
stock_data = {
    "AAPL": [ {"date": "2018-09-21",  "open": 23.5, "high": 23.5, "low": 23.5, "close": 23.5}, {"date": "2018-09-22",  "open": 63.5, "high": 93.5, "low": 23.5, "close": 23.5} ],
    "HDFC": [ {"date": "2018-11-21",  "open": 13.5, "high": 43.5, "low": 63.5, "close": 63.5} ]
}

def get_stock_input():
    symbol = input("Enter a symbol: ")
    date = input("Enter a date: ")
    open_price = float(input("Enter a opening price: "))
    high_price = float(input("Enter a high price: "))
    low_price = float(input("Enter a low price: "))
    close_price = float(input("Enter a close price: "))
    return symbol, date, open_price, high_price, low_price, close_price

def add_candle_stick_data():
    symbol, date, open_price, high_price, low_price, close_price = get_stock_input()
    value = {
        "date": date,
        "open": open_price,
        "high": high_price,
        "low": low_price,
        "close": close_price
    }

    if symbol not in stock_data:
        stock_data[symbol] = []

    stock_data[symbol].append(value)

def show_stocks_name():
    stocks = list(stock_data.keys())
    print(stocks)

def view_all_stocks():
    for stock, values in stock_data.items():
        print(f"Show info for {stock} ======>>>>")
        for value in values:
            print(f"{value["date"]} -> {value['open']} -> {value['close']}")

def search_by_stock_and_date(symbol, date):
    if symbol not in stock_data:
        print(f"Stock: {symbol} not found")
        return # exit the function

    data_found = False
    for value in stock_data[symbol]:
        if value["date"] == date:
            print(f"{value['date']} -> open: {value['open']}, high: {value['high']}, low: {value['low']}, close: {value['close']}")
            data_found = True
            break
    if not data_found:
        print(f"Stock: {symbol} data not found for date: {date}")

def main():
    while True:
        prompt = """
        Enter a number to select option:
            1. To add a candle data
            2. View all available stocks name
            3. View all stock data
            4. View stock data for a given symbol & date
            5. View all stock data for a give symbol and open & close price range
            6. Give the max open value for a given symbol
            7. Show all stock data by a date
            8. Show all stock data and show only [open, close, low, high, date]
        """
        print(prompt)
        option = input("Enter a number: ")
        if option == "1":
            add_candle_stick_data()
        elif option == "2":
            show_stocks_name()
        elif option == "3":
            view_all_stocks()
        elif option == "4":
            symbol = input("Enter a symbol: ")
            date = input("Enter a date: ")
            search_by_stock_and_date(symbol, date)

main()