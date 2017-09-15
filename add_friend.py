import spy_details
from spy_details import Friends

def add_friend():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }
    new_friend['name'] = raw_input("Enter friend's name\n")
    new_friend['salutation'] = raw_input("What do they call themselves ?\n"
                                         "Mr. or Ms.")
    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']
    new_friend['age'] = int(raw_input("Enter friend\'s age"))
    new_friend['rating'] = float(raw_input("Enter spy rating"))

    if len(new_friend['name']) > 0 :
        Friends.append(new_friend)
        print("Name : " + new_friend['name'] + "\nAge : " + str(new_friend['age']) +
          "\nRating : " + str(new_friend['rating']))
        print("Friend added !!!\n")
    else:
        print("Sorry !!!, Enter correct details")

    return len(Friends)
