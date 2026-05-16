# Class & Object
# Encapsulation
class Customer:
    # Constructor: to init the object
    def __init__(self, c_id, c_name, c_email):
        # data members, instance variable, object variable
        self.__id = c_id # private
        self.name = c_name # public
        self.__email = c_email # private

    def display(self):
        print(f"Customer id: {self.__id}, name: {self.name}, email: {self.__email}")

    # getter
    def get_id(self):
        return self.__id

    def get_email(self):
        return self.__email

    # setter
    def set_email(self, new_email):
        if new_email != self.__email:
            self.__email = new_email
        else:
            print("Email already set")


# create an object
# we are calling the __init__
c1 = Customer("123", "Mohit", "m@gamil.com")
print(c1.get_id(), c1.name, c1.get_email())

c2 = Customer("456", "Karan", "k@gamil.com")
print(c2.get_id(), c2.name, c2.get_email())

c1.display()
c2.display()

