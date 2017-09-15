from spy_details import Friends

def select_friend():
    count = 0
    for friend in Friends :
        print("%d \n%s \n%d \n%f is online")%(count+1,friend['name'],friend['age'],friend['rating'])
        #print(count + 1 + "Name : " + friend.name + "\nAge : " + friend.age + "\nRating : " + friend.rating + "is online\n")
        count = count + 1

    friend_choice = int(raw_input("Choose your Friend !!!"))
    index = friend_choice - 1
    return index
    #print(Friends[index])

