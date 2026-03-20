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
cart1 = [] # most prefer
cart2 = list() # type cast (tuple ==> list, set ===> list)
        #  0           1         2
        # -3           -2          -1
cart3 = ["laptop", "mouse", "mouse", "keyboard"]

print(cart3)
cart3.append("headphone")
print(cart3)
cart3.remove("mouse")
print(cart3)
print(cart3[0])
print(cart3[1])
print(cart3[-1])
print(cart3) # ['laptop', 'keyboard', 'headphone']

cart3[1] = "Keyboard" # edit operation
print(cart3)

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

week_days = ("MON", "TUE", "WED")
for day in week_days:
    print(day)

# week_days[0] = "ABC" error in tuple

builds_tuple = ("SUCCESS", "FAILED", "SKIP", "SUCCESS", "SUCCESS", "FAILED")

print(extract_build_status_with_index_enumerate(builds_tuple, "FAILED"))

# Set (Fast) (Hash Table)
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