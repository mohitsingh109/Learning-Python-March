from message import MessageSystem

class Slack(MessageSystem):
    def __init__(self, username):
        self.__username = username

    def sent_message(self, text):
        print(f"Sending {text} message to {self.__username}")