# Data structure/Collection
# List -- Array  []
# Tuple -- Immutable Array ()
# Set --> Unique list {}
# Dict  ---> Key Value {}

# Slice in list

# List
# Order (it maintain the insertion order)
# Mutable (add/edit/delete)
# Allow duplicate
# we can access element via a Index
# Index start from 0
# Negative use --> if you want the last

# Empty array/list
# cart1 = [] # most prefer
# cart2 = list() # type cast (tuple ==> list, set ===> list)
#         #  0           1         2
#         # -3           -2          -1
# cart3 = ["laptop", "mouse", "mouse", "keyboard"]
#
# print(cart3)
# cart3.append("headphone")
# print(cart3)
# cart3.remove("mouse")
# print(cart3)
# print(cart3[0])
# print(cart3[1])
# print(cart3[-1])
# print(cart3) # ['laptop', 'keyboard', 'headphone']
#
# cart3[1] = "Keyboard" # edit operation
# print(cart3)

# Real world list is a complex object like list of employee
# Multi line comment
"""
[
{"user":"Mohit", "email":"mohit@123"}, 
{"user":"Karan", "email":"karan@123"}
]
"""
         #build
builds = ["SUCCESS", "FAILED", "SKIP", "SUCCESS", "SUCCESS", "FAILED"]

# i want to know how much build succeeded

def extract_build_status(build_list, status):
    filtered_build = []
    for build in build_list:
        if build == status:
            filtered_build.append(build)

    return filtered_build

# [0-SUCCESS, 3-SUCCESS, 4-SUCCESS]
def extract_build_status_with_index_range(build_list, status):
    filtered_build_index = []
    for index in range(len(build_list)): # (0, 6]
        if build_list[index] == status:
            output = f"{index}-{build_list[index]}" # 0-SUCCESS
            # output = str(index) + "-" + build_list[index] f function solve this problem
            filtered_build_index.append(output)

    return filtered_build_index

def extract_build_status_with_index_enumerate(build_list, status):
    filtered_build_index = []
    for index, build in enumerate(build_list):
        if build == status:
            output = f"{index}-{build}"
            filtered_build_index.append(output)

    return filtered_build_index


# for build in builds:
#     print(build)
# print(len(extract_build_status(builds, "SUCCESS")))
# print(len(extract_build_status(builds, "FAILED")))
# print(extract_build_status_with_index_range(builds, "SUCCESS"))
# print(extract_build_status_with_index_range(builds, "FAILED"))
# print(extract_build_status_with_index_range(builds, "BLABLA"))
#print(extract_build_status_with_index_enumerate(builds, "FAILED"))

# Tuple
# Same as list, but they are immutable
# pulling data from DB
# Gender, WeekDays, Months

# week_days = ("MON", "TUE", "WED")
# for day in week_days:
#     print(day)

# week_days[0] = "ABC" error in tuple

builds_tuple = ("SUCCESS", "FAILED", "SKIP", "SUCCESS", "SUCCESS", "FAILED")

# print(extract_build_status_with_index_enumerate(builds_tuple, "FAILED"))

# Set (Fast) (Hash Table) (Hashing) ==> O(1)
# Unordered
# Unique value
# Mutable
# No index
# Fast to check duplicate
# look up operation fast based on some set of record
# List can also do this but in O(N)

# JAVA
# Filtered List ==> ["CRIMINAL", "TOYS", ...]
# Filtered set ==> {"CRIMINAL", "TOYS", ...}

# List of duplicate ==> List of Unique with same order
# Set + List
# Set ==> List
# list loop lookup in Set

import random
import time

build_number1 = {}
build_number2 = set()

build_array = [] # len == 1_000_000

for i in range(1_000_000):
    build_array.append(random.randint(1, 5000))

def dedup_builds(builds_duplicate):
    unique_build = []
    start = time.time()
    for build in builds_duplicate:
        if build not in unique_build: # O(N)
            unique_build.append(build)
    end = time.time()
    print(f"Total Time:{end - start}, Start: {start}, End: {end}")
    # Total Time:13.391114950180054, Start: 1774073943.56054, End: 1774073956.951655
    return unique_build

def dedup_builds_set(builds_duplicate):
    unique_build = []
    unique_build_set = set()
    start = time.time()
    for build in builds_duplicate:
        if build not in unique_build_set: # O(1)
            unique_build.append(build)
            unique_build_set.add(build)

    end = time.time()
    print(f"Total Time:{end - start}, Start: {start}, End: {end}")
    # Total Time:0.017790794372558594, Start: 1774074072.3517141, End: 1774074072.369505
    return unique_build

# print(dedup_builds_set(build_array))

# name_set = {"Mohit", "Karan", "Arjun", "Mohit", "Bla Bla", "Kuku"}
# print(name_set)

# Dict ==> Hash Map (Key : Value) (Hashing Tech)
# No Index
# Unordered
# Unique Key
# Duplicate Values
# Fast to search

# student_list = [
#     (1001, "Mohit", 44.5), # 0 <=== student
#     (1002, "Arjun", 94.5), # 1
#     (1003, "Aman", 55.5), # 2
#     (1004, "Karan", 64.5) # 3
# ]
#
# def search_student_by_id(students, stu_id, stu_name):
#     grades = []
#     for student in students:
#         if student[0] == stu_id or student[1] == stu_name:
#             print(student)
#             grades.append(student[2])
#     return grades
#
# print(search_student_by_id(student_list, 1003, "Arjun"))

# student_dict = {
#     1007: 66.7,
#     1003: 77.8,
#     1009: 45,
#     1004: 45
# }
# print(student_dict[1003]) # O(1)
# # Add / Update
# student_dict[1005] = 90
# student_dict[1004] = 40
# print(student_dict)
# #print(student_dict[9999]) # Key error
# print(student_dict.get(9999)) # None
#
# # Soft delete (XXXX)
# student_dict[1004] = None
# print(student_dict.get(1004)) # None
# print(student_dict)
#
# # Hard delete
# student_dict.pop(1004)
# print(student_dict)
#
# # Hard delete (Recommended)
# del student_dict[1005]
# print(student_dict)
#
# for s_id in student_dict.keys():
#     print(s_id)
#
# for s_value in student_dict.values():
#     print(s_value)
#
# for key, value in student_dict.items():
#     print(f"{key} ===> {value}")


student_database = {
    "1001": {
        "name": "Mohit",
        "class": "1",
        "age": 25,
        "marks": [100, 99, 67,50],
        "email": "test@yahoo.com"
    },
    "1002": {
        "name": "Karan",
        "class": "5",
        "age": 40,
        "marks": [56, 88, 67,50],
        "email": "karan@gmail.com"
    },
    "1003": {
        "name": "Arjun",
        "class": "5",
        "age": 32,
        "marks": [77, 23, 64, 88],
        "email": "arjun@hotmail.com"
    },
    "1004": {
        "name": "Aryan",
        "class": "2",
        "age": 32,
        "marks": [77, 23, 64, 88],
        "email": None
    }
}

# print(student_database["1001"])
#
# student_database["1001"]["email"] = "mohit@gmail.com"
#
# print(student_database["1001"])

def fetch_all_student_email(students_record):
    emails = []
    for student in students_record.values():
        if "email" in student and student["email"] is not None: # email is not None
            emails.append(student["email"])

    return emails


print(fetch_all_student_email(student_database))

def fetch_all_student_marks_with_there_id(students_record):
    pass

def find_by_student_id(students_record, s_id):
    pass

def find_by_student_email(students_record, s_email):
    pass

def find_all_student_by_class(students_record, s_class):
    pass

def find_all_student_contains_email_or_name(students_record, s_email, s_name):
    pass

# find_all_student_contains_email_or_name(student_database, "@gamil.com", "a")