from status_messages import current_status,Status_Messages
from add_status import add_status
import spy_details

def start_chat(spy_name,spy_age,spy_rating):
    current_status = None

   # spy_name = spy_salutation + " " + spy_name
    print("Authentication complete.\n" +
          "Name : " + spy_name + "\nAge : " + str(spy_age) +
          "\nRating : " + str(spy_rating) + "\nProud to have you onboard !!!")
    show_menu = True

    while show_menu :
        menu_choices = "What do you want to do? \n" \
                       " 1. Add a status update \n 2. Add a friend \n " \
                       "3. Send a secret message \n 4. Read a secret message \n " \
                       "5. Read Chats from a user \n 6. Close Application \n"
        menu_choice = raw_input(menu_choices)

        if len(menu_choice) > 0 :
            menu_choice = int(menu_choice)

            if menu_choice == 1:
                current_status = add_status(current_status)
            else :
                print("Enter valid option\n")