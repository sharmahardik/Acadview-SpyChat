from select_friend import select_friend
from spy_details import ChatMessage, Friends

def send_message_help():
    friends_choice = select_friend()

    text = "Bro. I'm coming to save you. Don't worry. "

    new_chat = ChatMessage(text, True)

    Friends[friends_choice].chats.append(new_chat)