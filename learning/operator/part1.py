# print("Welcome to python learning")
#
# print("Welcome to python learning", "How are you?")
#
# # f stand for f function
# print(f"Welcome to python learning How are you?")

# Variables -> Dynamic variable
# String, Int, Float, Boolean, Char
product_name = "Laptop"
print(product_name, type(product_name))

product_name = 10
print(product_name, type(product_name))

is_valid_user = True
print(is_valid_user, type(is_valid_user))

# Type Conversion int(), str(), bool(), float()
price = "100" # int but represent as string
print(price, type(price))
# str --> int
price = int(price)
print(price, type(price))

# # ValueError will throw
# invalid_price = "abc"
# invalid_price = int(invalid_price)
# print(invalid_price, type(invalid_price))

amount = 10.44
amount_int = int(amount)
print(amount_int, type(amount_int))

amount_str = str(amount)
print(amount_str, type(amount_str))

# Input & Output
# input return type is string
name = input("Enter your name?")
age = int(input("Enter your age?"))

#print("Hi", name, "Your age is", age)
print(f"Hi {name} Your age is {age}")








