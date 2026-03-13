# Arithmetic operator -, +, /, %, *, //

total_price = 513
quantity = 5
# // we use this if we don't need the decimal values
print(total_price // quantity)

# % to get the remainder

value = 18
print(value % 2)

# 4 ^ 4
print("4 ^ 4", 4 ** 4)

# BODMAS
total = (10 - 5) + 4 - 6 * 5/2
print(total)

# Relational Operator (result is always bool)
# >, <, >=, <=, !=, == Note (!=, ==) is used by all the data type

# name = input("Enter name")
# print(name == "Mohit")

print(10 > 5)
print(10 < 5)
print(5 <= 5)
print(5 >= 5)
print(5 == 5)
print(5 != 6)

# Logical operator  (left or right both should be bool)
# and, not, or

# User info
is_logged_in = True
is_admin = False

# is it a valid user
print(is_logged_in or is_admin)
print(5 >= 5 or 10 != 11)

# Short circuit
result = is_logged_in or is_admin
print("is_logged_in or is_admin", result)

result = is_admin and is_logged_in
print("is_admin and is_logged_in", result)

# not ===> true --> false or vice versa

print("not is_admin", not is_admin)

# Bitwise Operator ( >>, <<, ^, ~, &, |)
# binary number (fast math calculation)
#111 1000
#1111
#print(7 ^ 8)

# Assignment Operator
# =, +=, -=, /=, %=, //=

value = 25
# value = value + 5
value += 5
print(value)