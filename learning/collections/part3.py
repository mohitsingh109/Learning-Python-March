# List compression

squares = []

for i in range(1, 11):
    squares.append(i * i)

print(squares)

# # List compression
#         [expression loop]
squares = [i * i for i in range(1, 11)]
print(squares)

squares = (i * i for i in range(1, 11))
print(squares)

squares = {i * i for i in range(1, 11)}
print(squares)

users = [
    {"name": "Mohit", "age": 25},
    {"name": "Karan", "age": 25},
]

# list of name
names = []
for user in users:
    name = user["name"]
    names.append(name)

print(names)

names = [user["name"] for user in users]

orders = [100, 400, 200, 300]

labels = []

for order in orders:
    if order >= 250:
        labels.append("High")
    else:
        labels.append("Low")

print(labels)

# "High" if order >= 250 else "Low" ==> Ternary operator
labels = ["High" if order >= 250 else "Low" for order in orders]
print(labels)