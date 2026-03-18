# # function with no argument
# def greet():
#     print("Hello1")
#     print("Hello2")
#
# print(greet()) # None
# print("Hello3")
#
# # function with argument
# def print_name(name):
#     print(f"Hello {name} How are you?")
#
# # call
# print_name("Mohit Singh")
#
# # function with multiple argument and return
# def calculate_total(price, quantity):
#     total = price * quantity
#     return total
#
# print(calculate_total(100, 5))

# function with multiple argument & default value and return
# def calculate_total(price, quantity=1, tax = 0.5):
#     total = price * quantity + tax
#     return total
#
# print(calculate_total(100, 5))
# print(calculate_total(100))
# print(calculate_total(tax=0.4, price=100)) # named argument
#
# def user_account_info(user_id):
#     # DB
#     # API
#     # username, email_id, phone_number
#     return "Mohit", "test@gmail.com", 7888770222
#
# user_name, email, phone_number = user_account_info(123)
# print(user_name)
# print(email)
# print(phone_number)
#
# _, _, phone_number = user_account_info(123) # error ==> tuple
# print(phone_number)
#
# _, email, _ = user_account_info(123)
# print(email)

def f1(arg1):
    print(f"f1({arg1})")
#
# def f2(arg1, arg2):
#     f1(arg1) # f2 is calling f1
#     print(f"f2({arg2})")
#
# f2("Mohit", "ABC")
#
# def validate_should_contains_numeric(pwd):
#     pass # if we don't have impl we can add pass
#
# def validate_should_contains_special_char(pwd):
#     pass
