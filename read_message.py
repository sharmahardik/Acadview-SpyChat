from spy_details import Friends
from select_friend  import select_friend
from steganography.steganography import Steganography
from datetime import datetime

def read_message():

    sender = select_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }

    Friends[sender]['chats'].append(new_chat)

    print "Your secret message has been saved!"