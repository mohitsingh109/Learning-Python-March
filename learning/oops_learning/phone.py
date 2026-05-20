# Inheritance
    # Polymorphism
        # Run time
        # Compile time

# Inheritance
# Phone:
# name, model, price, color, height, width, weight

# Inheritance
# 1. Single Inheritance (one parent - one child) XX
# 2. Multilevel Inheritance (P --> C ---> C) XX
# 3. Hierarchy Inheritance (P --> C1 --> C2) YY
# 4. Hybrid Inheritance (P ---> C --> (c1, c2) ) YY


# Parent class
class Phone:
    def __init__(self, name, model, price, color, height, width, weight, number_of_cameras):
        self.__name = name
        self.__model = model
        self.__price = price
        self.__color = color
        self.__height = height
        self.__width = width
        self.__weight = weight
        self._number_of_cameras = number_of_cameras # protected variable


    # Getter
    def get_name(self):
        return self.__name

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def get_color(self):
        return self.__color

    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__weight

    def _get_number_of_cameras(self):
        return self._number_of_cameras

    #setter
    def set_price(self, price):
        self.__price = price

    def display(self):
        print("Parent Class", self.__name)

    def click_image(self):
        print("Click Image using phone:", self.__name)

# Child class
class IPhone(Phone):
    def __init__(self, name, model, price, color, height, width, weight, number_of_cameras, face_id):
        super().__init__(name, model, price, color, height, width, weight, number_of_cameras)
        self.face_id = face_id

    def f1(self):
        print(self._number_of_cameras)


# Child class
class Samsung(Phone):
    def __init__(self, name, model, price, color, height, width, weight, number_of_cameras, galaxy_ai):
        super().__init__(name, model, price, color, height, width, weight, number_of_cameras)
        self.galaxy_ai = galaxy_ai

    #function overriding
    def click_image(self):
        print("Click image using galaxy ai:", self.galaxy_ai)

    def f1(self):
        print(self._number_of_cameras)

iphone17 = IPhone("IPhone 17", "Pro Max", 10, "black", 11, 22, 33, 3, "f_123")
#iphone17.click_image() # Run time polymorphism

samsung_s24 = Samsung("Samsung S24", "24", 10, "black", 11, 22, 33, 3, "ax_123")
#samsung_s24.click_image() # Run time polymorphism

phone = [iphone17, samsung_s24] # ....

for p in phone:
    p.display()
    p.click_image() # Run time polymorphism
    p.f1()