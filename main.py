from spy_details import spy_name,spy_salutation,spy_rating,spy_age,spy_is_online
from start_chat import start_chat

question = "Do you want to continue as\n"+ "Name : " + spy_name +\
           "\nAge : " + str(spy_age) +"\nRating : " + str(spy_rating) +"(Y/N)"

existing = raw_input(question)


if (existing) == 'y' :
    #spy_name = spy_salutation + " " + spy_name
    start_chat(spy_name, spy_age, spy_rating)

elif (existing) == 'n' :
    spy_name = raw_input("What is your name?")
    if len(spy_name)>0:
        spy_salutation = raw_input("What should we call you\n Mr. or Ms")
        spy_name = spy_salutation + " " + spy_name
        print("Welcome!!! " + spy_name + ",\nGlad to have you here")
        print("Alright" + spy_name + " We need to know more about you before we proceed.")

        spy_age = int(raw_input("What is your age ?"))
        spy_rating = float(raw_input("What is your rating ?"))

        if spy_rating > 4.5 :
            print("Great Ace !!!\n")
        elif spy_rating > 3.5 and spy_rating < 4.5 :
            print("You are one of the bests !!!\n")
        elif spy_rating > 2.5 and spy_rating < 3.5 :
            print("You got the potential!!!\n")

        spy_is_online = True

        start_chat(spy_name, spy_age, spy_rating)

    else :
        print("Spy needs to enter a valid name !!!")

else :
    print("Enter correct option")






