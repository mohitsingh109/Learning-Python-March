"""
{
    "name": "BBQ",
    "email": "bbq@gmail.com",
    "address": "Panchkula sec 20"
}
"""
# Class is a blueprint
# Encapsulation --> [your data member should not be accessible directly from outside if required access it has to be done via function]
class Restaurant:
    # Contractor - to init the object
    # Self refer to current object who call the function
    def __init__(self, name, email, address, menu = []):
        self.name = name # data member
        self.email = email  # data member
        self.__address = address  # data member
        self.__menu = menu  # data member

    def display_info(self):
        print(f"Name: {self.name} Menu: {self.__menu} Email: {self.email} Address: {self.__address}")

    # Getter & Setter
    def get_address(self):
        return self.__address

    def set_address(self, new_address):
        # Send OPT
        # Verify OPT
        self.__address = new_address

    def change_restaurant_name(self, name):
        if name is None:
            print("Please enter a valid restaurant name")
            return
        if name == self.name:
            print("Name is same so no need to change")
            return
        self.name = name
        self.display_info()



# Object
rest1 = Restaurant("BBQ", "BBQ@gmail.com", "Bla Bla") # == this auto call the __init__
rest2 = Restaurant("MC", "MC@gmail.com", "Bla Bla")
rest3 = Restaurant("KFC", "kfc@gmail.com", "Bla Bla")
rest4 = Restaurant(email="BBQ@gmail.com", name="BBQ", address="Sec 20", menu=["Pizza", "Juice"])

print(rest3.name)
rest1.display_info()
rest2.display_info()
rest4.display_info()
rest3.change_restaurant_name("KFC Super")
rest3.name = "Hacker"
rest3.display_info()
print(rest1.get_address())
