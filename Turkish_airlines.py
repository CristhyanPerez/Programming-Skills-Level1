#Import libraries
import random

#List of available options
available_countries =["Turkey", "Greece", "Lebanon", "Spain", "Portugal"]
available_options = ["1", "2", "3", "4", "5"]

#Define a function to check if the username and password are correct
def verify_log_in(username, password):
    lenght_username = len(username)
    password_system = username + " " + str(lenght_username)
    if password_system == password:
        return True
    else:
        return False

#Define function to vr¿erify log in in a defined number of attempts
def login_attempts(number_attempts):
    access_allowed = False
    for i in range(number_attempts):
        username_in = input("What is your username: ")
        password_in = input("What is your password: ")
        print(f"\nAttempt {i+1} of {number_attempts}\n")
        check_login = verify_log_in(username_in, password_in)   #True or False
        if check_login == True:
            access_allowed = True
            break
        else:
            print("\nWarning: Incorrect password")
            if i < ( number_attempts - 1 ):
                print("Reset username and pasword\n")
                print("********** Log in **********\n")
    return access_allowed

#Given a menu, a question and a list of answers, the function will evaluate if the
#answer to the question is within the list
def check_answer(menu, question, list_answers):
    print(menu)
    start_check = False
    while start_check == False:
        option_user = input(question)
        if option_user in list_answers:
            start_check = True
        else:
            print("Opcion incorrecta.Let's go again\n")
    option_user = int(option_user)
    return option_user

#The countries menu has an exception since the country of departure and return
#cannot be the same. 1 -> Origin, 2-> Destination
def country_menu(origin_destination, list_countries):
    if origin_destination == 1:
        print("\nAvailable countries of origin:")
    else:
        print("\nDestination countries available:")
    number_countries = len(list_countries)
    for i in range(number_countries):
        print(f"{i+1}- {list_countries[i]}")
    print()

#Boarding times will be generated randomly
def boarding_times_random():
    print("\nAvailable boarding times:")
    list_boarding_times = []
    for i in range(4):
        minutes = str(random.randint(0,6))
        if i == 0:
            hour = str(random.randint(3,6))
            day_or_night = "a.m"
        elif i == 1:
            hour = str(random.randint(9,11))
            day_or_night = "a.m"
        elif i == 2:
            hour = str(random.randint(2,4))
            day_or_night = "p.m"
        elif i == 3:
            hour = str(random.randint(5,8))
            day_or_night = "p.m"
        boarding_schedule = hour + ":" + minutes + "0 " + day_or_night
        list_boarding_times.append(boarding_schedule)
    return list_boarding_times

#The schedule menu is generated
def boarding_times_menu(list_boarding_times):
    for i in range(4):
        print(f"{i+1}- {list_boarding_times[i]}")
    print()
