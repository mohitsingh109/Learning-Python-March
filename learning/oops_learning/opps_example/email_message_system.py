from message import MessageSystem

class Email(MessageSystem):

    def __init__(self, email):
        self.__email = email
        
    def sent_message(self, text):
        print(f"Sending email to {self.__email} {text}")
