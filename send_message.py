from spy_details import Friends
from select_friend  import select_friend
from steganography.steganography import Steganography
from datetime import datetime


def send_message():

    friend_choice = select_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }

    Friends[friend_choice]['chats'].append(new_chat)

    print "Your secret message image is ready!"