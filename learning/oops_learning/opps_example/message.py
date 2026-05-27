# Message system
# Message via an SMS, Email, Slack, Teams, WhatsApp,...

# MessageSystem
# sent_message(text) XXX

from abc import ABC, abstractmethod

class MessageSystem(ABC):

    @abstractmethod
    def sent_message(self, text):
        pass