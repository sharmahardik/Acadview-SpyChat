from datetime import datetime

spy_name = "Hardik"
spy_salutation = "Mr."
spy_age = 20
spy_rating = 4.5
spy_is_online = False

Friends = []

class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me