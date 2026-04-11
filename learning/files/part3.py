# error if file not exist
# this mode overwrite the old data

def save_user_activity(user_activity: list, file):
    for activity in user_activity:
        file.write(activity + "\n")

def main():
    with open('log.txt', 'a') as file:
        user_activity = [
           "User searching iphone 14",
        ]
        save_user_activity(user_activity, file)

main()

# log.txt
# user action monitor
# customer_id-user_id.log
# customer dell ==> user ==> dell employee