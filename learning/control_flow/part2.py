# For loop (99%)

# list, set, tuple, dict, range

# range
# 0 -- < 10 step up by 1
# for i in range(10):
#     print(i)
#
# print("===========")
# # 1 -- < 10 step up by 1
# for i in range(1, 10):
#     print(i)
#
# print("===========")
#
# # 1 -- < 10 step up by 2
# for i in range(1, 10, 2):
#     print(i)
#
# print("===========")

# 10 -- < -1  step down by 1
# for i in range(10, -1, -1):
#     print(i)
#
# print("===========")
#
# for retry in range(3):
#     print(f"Perform retry: {retry}")


# While (1 %)

# is_active = True


# while is_active:
#     print("PLaying game")
#     continue_playing = input("Continue? ")
#     if continue_playing == "n":
#         is_active = False

#
# while has_data_in_db:
#     fetch it
#     do processing
#

# attempts = 0
#
# while attempts < 3:
#     print("Try saving the user record")
#     attempts += 1


# for row_number in range(10):
#     if row_number == 5:
#         print("Found the record that match x, y value")
#         break # stop the loop
#     print(f"Row Number: {row_number}")
#
# while True:
#     user_input  = input("Do you want to continue?")
#     if user_input == "y":
#         print("Let's play the game")
#     else:
#         break

# for row_number in range(10):
#     if row_number == 5:
#         print("Found the record that match x, y value")
#         continue # it returns back to  the loop
#     print(f"Process Row Number: {row_number}")


# for message in kafka:
#     if message already in db:
#         continue

# Table print based on user input
# input()
# int
# loop with range from 1 to 10 increase by 1
# if it's negative number I don't want to process
while True:
    number = input(f" {"=" * 5} Enter the number {"=" * 5}: ")
    number = int(number)

    if number <= 0:
        print("Invalid number to print the table")
        exit(-1) # No use in real life

    for i in range(1, 11, 1):
        cal = number * i
        print(f"{number} X {i} = {cal}")

    still_continue = input("Do you want to continue (y/n)?")
    # N, n, No, NO, no ===> n, no
    still_continue = still_continue.lower()
    if still_continue == "n" or still_continue == "no":
        print(f" {"🥳" * 10} Thank u {"🥳" * 10}")
        break