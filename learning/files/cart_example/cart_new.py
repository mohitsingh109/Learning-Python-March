"""
User Info (user.txt)
id
name
email
Example: 123,Mohit,mohit123@gmail.com
"""
from learning.oops_learning.person import User

# cache
"""
[User(u_id:112, name:Mohit, email:abc)])]
"""

# File read and return all the user
def load_user() -> list:
    user_list = []
    with open("users.txt", "r") as file:
        for line in file:
            user_id, name, email = line.split(",")
            user = User(user_id, name, email)
            user_list.append(user)
    return user_list

def find_user_by_id(user_id: str) -> User | None:
    if not users:
        print("[WARN] No users database found exit the code")
        exit(-1)
    for user in users:
        if user.u_id == user_id:
            return user
    print(f"[WARN] No user found with id {user_id}")
    return None

def find_user_by_name(name: str) -> User | None:
    if not users:
        print("[WARN] No users database found exit the code")
        exit(-1)
    for user in users:
        if user.name == name:
            return user
    print(f"[WARN] No user found with name {name}")
    return None

def find_user_by_email(email: str) -> User | None:
    if not users:
        print("[WARN] No users database found exit the code")
        exit(-1)
    for user in users:
        if user.email == email:
            return user
    print(f"[WARN] No user found with email {email}")
    return None

def save_user(user_id, name, email):
    if not users:
        print("[WARN] No users database found exit the code")
        exit(-1)

    if find_user_by_id(user_id):
        print(f"[WARN] User found with id {user_id} we can't save same user again")
        return
    user = User(user_id, name, email)
    with open("users.txt", "a") as file:
        file.write(user.txt_row() + "\n")

    # updating our users cache
    users.append(user)

def load_cart() -> dict:
    carts_data = {}

    for user in users:
        carts_data[user.u_id] = []

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
for user in users:
    user.display()
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