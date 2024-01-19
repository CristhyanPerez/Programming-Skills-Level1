#Import libraries
import random
from datetime import datetime

#List of available options
available_options = ["1", "2", "3", "4", "5"]
available_meal = ["Regular", "Vegetarian", "Kosher"]
available_yes_no = ["yes", "y", "YES", "no", "n", "NO"]
available_countries = ["Turkey", "Greece", "Lebanon", "Spain", "Portugal"]

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
    return option_user

#Define a function to return the country of origin and country of destinatation
def country_origin_destination(menu, available_countries):
    print(menu)
    origin_country = check_answer("\nChoose the country of origin (1-5): ", available_options)
    index_in_country = int(origin_country) - 1
    #With the index we access the country
    origin_country = available_countries[index_in_country]
    #Ensure that the country of origin is an option
    reset = True
    while reset == True:
        dtn_country = check_answer("\nChoose the country of destination (1-5): ", available_options)
        index_out_country = int(dtn_country) - 1
        if index_in_country == index_out_country:
            print("Wrong option. Let's go again")
            reset = True
        else:
            dtn_country = available_countries[index_out_country]
            reset = False
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
            date_oficial = date_oficial.strftime("%d-%m-%Y")
            return date_oficial
            break
        else:
            print("Retry..!!!\n")

#Define a function to return the date of departure and the date of return
def date_dpt_rtn():
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
        flight_cost = 200
    else:
        flight_option = "First Class"
        flight_cost = 250
    return flight_option, flight_cost

#Function to extra luggage
def extra_luggage(menu):
    print(menu)
    question = "Do you want to add extra luggage? (y/n): "
    option_luggage = check_answer(question, available_yes_no)
    if option_luggage in available_yes_no[3:6]:
        cost_luggage = 0
        amount = 0
    else:
        available_amount = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        amount = check_answer("How much luggage do you want to add? (0-9): ", available_amount)
        amount = int(amount)
        cost_luggage = amount * 20
    return cost_luggage, amount

#Function to choose favourite food
def flight_food(menu, options_meal):
    print(menu)
    question = "Chose your favourite food (1-3): "
    list_answers_class = ["1", "2", "3"]
    option_food = check_answer(question, list_answers_class)
    index = int(option_food) - 1
    flight_meal = options_meal[index]
    return flight_meal

#Funtion to collect user data
def user_data():
    list_user = []
    name = input("What is your name?: ")
    last_name = input("What is your last name?: ")
    number_id = input("What is your ID or Passport number?: ")
    list_user.append(name)
    list_user.append(last_name)
    list_user.append(number_id)
    return list_user

#Function to print the initial summary of each flight
def initial_summary(number, country_1, country_2, date_1, date_2):
    if number == 0:
        summary_start = f"""
        ****************    Outbound Flight    *********************
        
        {country_1}   --->   {country_2}              |      {date_1}      
        """
    else:
        summary_start = f"""

        ****************    Return Flight    *********************
        
        {country_2}   --->   {country_1}              |      {date_2}     
        """
    print(summary_start)

#Function to print the final summary of the two flights and personal information
def final_summary(country_1, country_2, date_1, date_2, list_chosen, list_cost, list_user):
    summary_final = f"""
    ****************    Final Summary    *********************
        
        {country_1}   --->   {country_2}              |      {date_1} 

        Class:      {list_chosen[0]}
        Luggage:    {list_chosen[2]}
        Food:       {list_chosen[1]}
        Cost:       {list_cost[0]}
    
    ----------------------------------------------------------
    
        {country_1}   --->   {country_2}              |      {date_2} 

        Class:      {list_chosen[3]}
        Luggage:    {list_chosen[5]}
        Food:       {list_chosen[4]}
        Cost:       {list_cost[1]}

    ----------------------------------------------------------

                    Personal Information
    
        Name:       {list_user[0]}
        Last name:  {list_user[1]}
        ID/Passport:{list_user[2]}

    ----------------------------------------------------------

    Total Cost =    {list_cost[0]+ list_cost[1]}

    **********************************************************
    
    """
    print(summary_final)

#Message to exit the program
def message_custom(sentence):
    print()
    print(sentence)
    print("Thank you")
    print("Come back soon\n")

#Menus
#Program entry menu
menu_entry = """
****************    Turkish Airlines    *********************

Welcome, first, you have to log in.

* The password is made up of the following:
  Username + space + number of characteres in the user word

Example:
Username: Cristhyan
Password: Cristhyan 9

Remember that you only have three attempts
"""

#Show available countries
menu_countries ="""
This airline has operations in the
following countries:

1- Turkey
2- Grecce
3- Lebanon
4- Spain
5- Portugal

* Notes:
 - The destination country must be different than the origin country
 - We only have flights available for this 2024. The date must be
   entered with the following format: 01-09-24
"""

#Menu - Economic vs First Class
menu_class = """
            Feature      | Economy class (1) |   First Class (2)
        -----------------------------------------------------------
        Seat space and   |  Narrower seats,  |   wider seats,
           comfort       |  limited legroom  |   more legroom
        -----------------------------------------------------------
          Additional     |  Basic services   |   Access to VIP
          services       |                   | lounges, priority
                         |                   |     boarding
        -----------------------------------------------------------
           Cost ($)      |        200        |        250     
        -----------------------------------------------------------
"""

#menu to add suitcase
menu_luggage ="""
Notes: 
* Hand luggage is free of charge.
* There is a $20.00 charge for additional luggage.
"""

#Menu food Regular - Vegetarian - Kosher
menu_food = """
Type of food available:

1 |  Regular
2 |  Vegetarian
3 |  Kosher
"""

#Main Function
def main():
    print(menu_entry)
    login = login_attempts(3)
    if login == True:
        print("****************    Login Successfully   ********************")
        reset_main_menu = True
        while reset_main_menu == True:
            print("\n**************************************************************\n")
            origin_country, destin_country = country_origin_destination(menu_countries, available_countries)
            date_departure, date_return = date_dpt_rtn()
            list_cost_in_out = []
            list_chosen_options = []
            for i in range(2):
                total_cost = 0
                initial_summary(i, origin_country, destin_country, date_departure, date_return)
                class_option, cost_flight = flight_class(menu_class)
                cost_luggage, amount_luggage = extra_luggage(menu_luggage)
                favourite_food = flight_food(menu_food, available_meal)
                print()
                total_cost = cost_flight + cost_luggage
                list_cost_in_out.append(total_cost)
                list_chosen_options.append(class_option)
                list_chosen_options.append(favourite_food)
                if amount_luggage == 0:
                    list_chosen_options.append("Only hand luggage")
                else:
                    luggage_message = "Hand luggage + " + str(amount_luggage) + " extra pieces of luggage"
                    list_chosen_options.append(luggage_message)
            print("\nPersonal Information\n")
            list_user_data = user_data()
            final_summary(origin_country, destin_country, date_departure, date_return, list_chosen_options, list_cost_in_out, list_user_data)
            buy_flight = check_answer("\nDo you want to buy the plane ticket?(y/n): ", available_yes_no)
            if buy_flight in available_yes_no[0:3]:
                message_custom("\nSuccessful purchase")
                reset_main_menu = False
            else:
                exit_program = check_answer("\nDo you want to exit the program?(y/n): ", available_yes_no)
                if exit_program in available_yes_no[0:3]:
                    message_custom("")
                    reset_main_menu = False
                else:
                    print("\nLet's start again..!!!!\n")
                    reset_main_menu = True
    else:
        message_custom("Maximum number of attempts")

#Entry point
if __name__ == "__main__":
    main()