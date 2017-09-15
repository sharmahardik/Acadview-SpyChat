from spy_details import Friends
from select_friend  import select_friend
from steganography.steganography import Steganography
from datetime import datetime
from spy_details import Friends, ChatMessage

import re


def send_message():

    friend_choice = select_friend()

    original_image = raw_input("Provide the name of the image to hide the message : ")
    pattern_i = '^[a-zA-Z]+\.jpg$'

    output_image = raw_input("Provide the name of the output image  : ")
    pattern_o = '^[a-zA-Z]+\.jpg$'

    text = raw_input("Enter your message here : ")
    Steganography.encode(original_image, output_image, text)

    new_chat = ChatMessage(text, True)

    Friends[friend_choice].chats.append(new_chat)

    print("Your message encrypted successfully.")

    new_chat = {
        'message': text,
        'time': datetime.now(),
        'sent_by_me': True
    }

    Friends[friend_choice].chats.append(new_chat)
    print("your secret message is ready.")

    if (re.match(pattern_i, original_image) != None and re.match(pattern_o, output_image) != None):
        print('All perfect')
    else:
        print('Sorry! Invalid entry. We can\'t validate your input and output\n ')
        print('The convention to follow is: \n')
        print('1. Input should ends with (.jpg) format.\n ')
        print('2. Output should also ends with (.jpg) format.\n ')
        print('Keep in mind and Try Again\n ')