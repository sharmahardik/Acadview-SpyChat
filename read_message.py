
from select_friend import select_friend
from steganography.steganography import Steganography
from spy_details import Friends
from send_message_help import send_message_help
from spy_details import ChatMessage

import re


def read_message():
    sender = select_friend()

    encrypted_image = raw_input("Provide encrypted image : ")
    pattern_e = '^[a-zA-Z]+\.jpg$'

    try:
        secret_message = Steganography.decode(encrypted_image)
        print ("The secret message is ")
        print (secret_message)
        words = secret_message.split()

        new = (secret_message.upper()).split()

        Friends[sender].count += len(words)
        if "SOS" in new or "SAVE" in new or "HELP" in new or "ACCIDENT" in new or "ALERT" in new:

            print("!")

            print("The friend who sent this message need your help.")
            print("You can help your friend by sending helping message.")
            print("Select the friend to send helping message")

        send_message_help()

        print("You just sent a message to help your friend.")

        new_chat = ChatMessage(secret_message, False)
        Friends[sender].chats.append(new_chat)
        print("Your secret message has been saved.")

        print "Average words said by : ",
        print(Friends[sender].name)
        print(" is ")
        print(Friends[sender].count)

        if(len(words)>100):
            print(Friends[sender].name)
            print(" removed from friends list. He was out of his mind, huh!.")
            Friends.remove(Friends[sender])

    except TypeError:
        print("This image has no secret message. No decoding. Aah!")

        if (re.match(pattern_e, encrypted_image) != None):
            print('All perfect')
        else:
            print('Sorry! Invalid entry. We can\'t validate your input and output\n ')
            print('The convention to follow is: \n ')
            print('1. Encrypted should ends with (.jpg) format.\n ')
            print('Keep in mind and Try Again\n\n ')