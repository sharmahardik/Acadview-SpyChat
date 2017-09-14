from status_messages import current_status,Status_Messages

def add_status(current_status):
    updated_status = None

    if current_status != None :
        print("Current Ststus : " + current_status + "\n")
    else:
        print("You don\'t have any status message currently\n")

    default = raw_input("Do you want to select from older status \n")

    if default == 'n':
        new_status = raw_input("Enter your status message\n")

        if len(new_status) > 0:
            Status_Messages.append(new_status)
            updated_status = new_status

    elif default =='y':

        item_position = 1
        for message in Status_Messages:
            print("%s,%s")%(item_position,message)
            item_position = item_position + 1
        message_selection = int(raw_input("Choose from above Messages\n"))
        if len(Status_Messages) >= message_selection:
            updated_status = Status_Messages[message_selection - 1]
    else :
        print("Enter valid option")

    print(updated_status)

