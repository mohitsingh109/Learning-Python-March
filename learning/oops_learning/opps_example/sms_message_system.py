from message import MessageSystem

class Sms(MessageSystem):

    def __init__(self, phone_number):
        self.__phone_number = phone_number

    def sent_message(self, text):
        print(f"Sending SMS to {self.__phone_number}  with text: {text}")