"""
User Info (user.txt)
id
name
email
Example: 123,Mohit,mohit123@gmail.com
"""
# cache
"""
[{"user_id": 123,"name": "Mohit","email": "mohit123@gmail.com"}]
"""

# File read and return all the user
def load_user() -> list:
    user_list = []
    with open("users.txt", "r") as file:
        for line in file:
            user_id, name, email = line.split(",") # [123, Mohit, mohit123@gmail.com]
            user = {
                "user_id": user_id,
                "name": name,
                "email": email
            }
            user_list.append(user)
    return user_list

def find_user_by_id(user_id: str) -> dict:
    if not users:
        print("[WARN] No users database found exit the code")
        exit(-1)
    for user in users:
        if user["user_id"] == user_id:
            return user # {"user_id": 123,"name": "Mohit","email": "mohit123@gmail.com"}
    print(f"[WARN] No user found with id {user_id}")
    return {}

def find_user_by_name(name: str) -> dict:
    if not users:
        print("[WARN] No users database found exit the code")
        exit(-1)
    for user in users:
        if user["name"] == name:
            return user  # {"user_id": 123,"name": "Mohit","email": "mohit123@gmail.com"}
    print(f"[WARN] No user found with name {name}")
    return {}

def find_user_by_email(email: str) -> dict:
    if not users:
        print("[WARN] No users database found exit the code")
        exit(-1)
    for user in users:
        if user["name"] == email:
            return user  # {"user_id": 123,"name": "Mohit","email": "mohit123@gmail.com"}
    print(f"[WARN] No user found with email {email}")
    return {}

def save_user(user_id, name, email):
    if not users:
        print("[WARN] No users database found exit the code")
        exit(-1)

    if find_user_by_id(user_id):
        print(f"[WARN] User found with id {user_id} we can't save same user again")
        return

    user_row = f"{user_id},{name},{email}" # 123,Mohit,mohit123@gmail.com
    with open("users.txt", "a") as file:
        file.write(user_row + "\n")

    # updating our users cache
    user = {
        "user_id": user_id,
        "name": name,
        "email": email
    }

    users.append(user)

def load_cart() -> dict:
    carts_data = {}

    for user in users:
        carts_data[user["user_id"]] = []

    with open("carts.txt", "r") as file:
        for line in file:
            cart_id, user_id, product_id, product_name, price, quantity = line.split(",")
            cart_product = {
                "product_id": product_id,
                "product_name": product_name,
                "price": price,
                "quantity": quantity
            }
            carts_data[user_id].append(cart_product)
    return carts_data

users = load_user()
# print(users)
# save_user("2244", "Aman", "aman123@gmail.com")
# save_user("2245", "Karan", "karan@gmail.com")
# print(users)



# carts = {
#     "2244": [
#         {"product_id": "22", "product_name": "Iphone17", "price": 500, "quantity": 1},
#         {"product_id": "23", "product_name": "Car Toy", "price": 30, "quantity": 2}
#     ],
#     "2245": []
# }
carts = load_cart()
for key, value in carts.items():
    print(f"{key} ===>  {value}")


"""
carts.txt
cart_id, user_id, product_id, product_name, price, quantity
1,2244,22,Iphone 17,500,1
1,2245,22,Iphone 17,500,1
1,2244,23,Car Toy,30,2
"""
# show_summary_for_user(user_id)
"""
user id, user name, email, list of cart product
"""