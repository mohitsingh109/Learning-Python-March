# Indentation syntax
# Control ===> if else, if elif else, if
# name = input("Enter your name: ")

# Other language like java/ c++ follow this
# if (name == "hacker") {
# print("Hacker are not allowed")
# print("Sorry you can't login")
# }

# # if, if else
# if name == "hacker":
#     print("Hacker are not allowed")
#     print("Sorry you can't login")
# else:
#     print("Login success")

# if elif else

report = "ABC"

if report == "VM":
    print("Trigger VM report")
elif report == "TV":
    print("Trigger TV report")
elif report == "Assert":
    print("Trigger asset report")
else:
    print("Trigger all type of report")

marks = 95

if marks >= 90:
    print("A")
elif marks >= 70:
    print("B")
else:
    print("C")

# Below is wrong you should always make sure the order if else if correct
# if marks >= 70:
#     print("B")
# elif marks >= 90:
#     print("A")
# else:
#     print("C")
