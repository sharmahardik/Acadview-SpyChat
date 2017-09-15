from status_messages import current_status,Status_Messages
from add_status import add_status
from add_friend import add_friend
from select_friend import select_friend
from spy_details import  Friends
from send_message import send_message
from read_message import read_message
def start_chat(spy_name,spy_age,spy_rating):
    current_status = None

   # spy_name = spy_salutation + " " + spy_name
    print("Authentication complete.\n" +
          "Name : " + spy_name + "\nAge : " + str(spy_age) +
          "\nRating : " + str(spy_rating) + "\nProud to have you onboard !!!")
    show_menu = True

    while show_menu :
        menu_choices = "What do you want to do? \n1. Add a status update \n" \
                       "2. Add a friend \n3. Select friend \n" \
                       "4. Send a secret message \n5. Read a secret message\n" \
                       "6. Read Chats from a user \n7. Close Application\n "

        menu_choice = raw_input(menu_choices)

        if len(menu_choice) > 0 :
            menu_choice = int(menu_choice)

            if menu_choice == 1:
                current_status = add_status(current_status)
            elif menu_choice == 2:
                number_of_friends = add_friend()
            elif menu_choice == 3:
                index = select_friend()
                print(Friends[index])
            elif menu_choice == 3:
                send_message()
            elif menu_choice == 4:
                read_message()

            else :
                print("Enter valid option\n")