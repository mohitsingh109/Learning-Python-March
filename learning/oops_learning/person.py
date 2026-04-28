# Class & Object
# class Person
# Encapsulation
class User:
    # self ==> self refer to current/calling object
    def __init__(self, u_id, name, email): # constructor
        self.u_id = u_id
        self.name = name
        self.email = email

    def display(self): # class function
        print(f"User id: {self.u_id}, name: {self.name}, email: {self.email}")

    def txt_row(self):
        return f"{self.u_id},{self.name},{self.email}"

"""
2231,Mohit Singh,mohit123@gmail.com
2244,Aman,aman123@gmail.com
2245,Karan,karan@gmail.com
"""

# users = {
#     "123": {
#         "name": "Mohit",
#         "email": "mohit@gmail.com",
#         "address": "abc"
#     },
#     "456": {
#         "Name": "Karan",
#         "email_address": "karan@gmail.com",
#         "phone": "123"
#     }
# }

# # object
# user_1 = User(2231, "Mohit Singh", "mohit123@gmail.com", "ad1")
# user_2 = User(2244, "Aman", "aman123@gmail.com", "ad2")
# user_3 = User(2245, "Karan", "karan@gmail.com", "ad3")
#
# user_list = [user_1, user_2, user_3]
#
# for user in user_list:
#     user.display()
#
# abc = 123
# abc = str(abc)