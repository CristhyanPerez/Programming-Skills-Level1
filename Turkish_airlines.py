#Import libraries
import random
from datetime import datetime

#List of available options
available_countries =["Turkey", "Greece", "Lebanon", "Spain", "Portugal"]
available_options = ["1", "2", "3", "4", "5"]
available_meal = ["Regular", "Vegetarian", "Kosher"]
available_yes_no = ["yes", "y", "YES", "no", "n", "NO"]

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

#Given a question and a list of answers, the function will evaluate if the
#answer to the question is within the list
def check_answer(question, list_answers):
    start_check = False
    while start_check == False:
        option_user = input(question)
        if option_user in list_answers:
            start_check = True
        else:
            print("Wrong option. Let's go again")
    option_user = int(option_user)
    return option_user

#Define a function to return the country of origin and country of destinatation
def country_origin_destination(menu):
    print(menu)
    origin_country = check_answer("\nChoose the country of origin (1-5): ", available_options)
    index_in_country = int(origin_country) - 1
    #Ensure that the country of origin is an option
    available_options.pop(index_in_country)
    #With the index we access the country
    origin_country = available_countries[index_in_country]
    print("\nNote:")
    print("The destination country must be different than the origin country")
    dtn_country = check_answer("\nChoose the country of destination (1-5): ", available_options)
    index_out_country = int(dtn_country) - 1
    dtn_country = available_countries[index_out_country]
    #To return both countries as string
    return origin_country, dtn_country

#Function to verify the existence of a date of 2024
def existence_date(date_str):
    if len(date_str) == 8 and date_str[2] == "-" and date_str[5] == "-":
        dd = int(date_str[0:2])
        mm = int(date_str[3:5])
        aa = int(date_str[6:8])
        if aa == 24:
            if mm > 0 and mm <= 12:
                if mm == 2:
                    if dd > 0 and dd <= 29:
                        date_in = True
                    else:
                        print("Febrary has a 29 days")
                        date_in = False
                elif mm in [1, 3, 5, 7, 8, 10, 12]:
                    if dd > 0 and dd <= 31:
                        date_in = True
                    else:
                        print("This month has 31 days")
                        date_in = False
                elif mm in [4, 6, 9, 11]:
                    if dd > 0 and dd <= 30:
                        date_in = True
                    else:
                        print("This month has 30 days")
                        date_in = False
            else:
                print("Wrong month")
                date_in = False
        else:
            print("Wrong year")
            date_in = False
    else:
        print("The date doesn't comply with the format")
        date_in = False
    return date_in

#Function designed to iterate until the user enters a correct date
def date_loop(sentence):
    date_in = False
    while date_in == False:
        date_format = input(sentence)
        date_string = date_format.replace(" ", "")
        existe = existence_date(date_string)
        if existe == True:
            dd = int(date_string[0:2])
            mm = int(date_string[3:5])
            date_oficial = datetime(2024,mm,dd)
            return date_oficial
            break
        else:
            print("Retry..!!!\n")

#Define a function to return the date of departure and the date of return
def date_dpt_rtn(menu):
    print(menu)
    correct_dates = False
    while correct_dates == False:
        date_departure = date_loop("\nChoose your departure date: ")
        date_return = date_loop("\nChoose your return date: ")
        if date_departure < date_return:
            correct_dates = True
            return date_departure, date_return
        else:
            correct_dates = False
            print("Incorrect dates\nRetry..!!!")

#Function to choose Fist class or economy
def flight_class(menu):
    print(menu)
    question = "Chose the condition, Economic or First class (1-2): "
    list_answers_class = ["1","2"]
    option_class = check_answer(question, list_answers_class)
    if option_class == 1:
        flight_option = "Economy"
    else:
        flight_option = "First Class"
    return flight_option

#Function to choose favourite food
def flight_food(menu, options_meal):
    print(menu)
    question = "Chose your favourite food (1-3): "
    list_answers_class = ["1", "2", "3"]
    option_food = check_answer(question, list_answers_class)
    index = option_food - 1
    flight_meal = options_meal[index]
    return flight_meal


