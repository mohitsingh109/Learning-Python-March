from sms_message_system import Sms
from email_message_system import Email
from slack_message_system import Slack

sms_message_system = Sms("835784738573")
email_message_system = Email("test@gmail.com")
slack_message_system = Slack("m123")

mohit_subscribed = [sms_message_system, email_message_system, slack_message_system]

for subscriber in mohit_subscribed:
    subscriber.sent_message("Hello Mohit we've meeting schedule today") # Run time ploy

