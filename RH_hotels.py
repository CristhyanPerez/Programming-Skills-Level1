#Import libraries
from datetime import datetime

#List of available options
available_options = ["1", "2", "3", "4", "5"]
available_countries = ["Spain", "France", "Portugal", "Italy", "Germany"]
available_cities_spain = ["Madrid", "Barcelona", "Valencia"]
available_cities_france = ["Paris", "Marseille"]
available_cities_portugal = ["Madeira", "Lisbon", "Porto"]
available_cities_italy = ["Rome", "Milan"]
available_cities_germany = ["Munich", "Berlin"]
available_yes_no = ["yes", "y", "YES", "no", "n", "NO"]
available_rooms = ["VIP Suits", "Single rooms", "Double rooms", "Group rooms", "Luxury suits"]
initial_amount = [6, 3, 6, 6, 3]
initial_cost = [450, 100, 200, 350, 550]

#Define a function to check if the username and password are correct
def verify_log_in(username, password):
    lenght_username = len(username)
    password_system = username + " " + str(lenght_username)
    if password_system == password:
        return True
    else:
        return False

#Define function to verify log in in a defined number of attempts
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
            print("Wrong option. Let's go again\n")
    return option_user

#Function to choose country
def hotel_country(options_available):
    question = "What country do you want to stay in? (1-5): "
    option_country = check_answer(question, options_available)
    index = int(option_country) - 1
    hotel_country = available_countries[index]
    return hotel_country

#Function to choose city from the country
def hotel_city(country, options_available):
    list_cities = []
    options = options_available
    if country == "Spain":
        list_cities = available_cities_spain
        options = options_available[0:3]
        lenght = 3
    elif country == "France":
        list_cities = available_cities_france
        options = options_available[0:2]
        lenght = 2
    elif country == "Portugal":
        list_cities = available_cities_portugal
        options = options_available[0:3]
        lenght = 3
    elif country == "Italy":
        list_cities = available_cities_italy
        options = options_available[0:2]
        lenght = 2
    elif country == "Germany":
        list_cities = available_cities_germany
        options = options_available[0:2]
        lenght = 2
    question = f"What city do you want to stay in? (1-{lenght}): "
    option_city = check_answer(question, options)
    index = int(option_city) - 1
    hotel_city = list_cities[index]
    return hotel_city

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

#Function to show the number of available rooms
def show_rooms_available(type_rooms, list_rooms_available, new_list_options):
    print("\nAvailability rooms:\n")
    for i in range(5):
        if list_rooms_available[i] == 0:
            message = "There aren't rooms available"
        elif list_rooms_available[i] == 1:
            message = "There is a room available"
            option = str(i + 1)
            new_list_options.append(option)
        else:
            message = "There are " + str(list_rooms_available[i]) + " rooms available"
            option = str(i + 1)
            new_list_options.append(option)
        print(f"{i + 1}- {type_rooms[i]}:  {message}")
    print()
    return new_list_options

#Function that receives a list and returns True if at least one of its elements is non-zero
def list_non_zero(number_list):
    elements = len(number_list)
    count = 0
    for i in range(elements):
        if number_list[i] != 0:
            count = count + 1
    if count ==  0:
        return False
    else:
        return True

#Function to create list from a number
def create_list_number(number):
    list_number_string = []
    for i in range(1, number + 1):
        element = str(i)
        list_number_string.append(element)
    return list_number_string

#Function to choose rooms
def hotel_rooms(type_rooms, amount_rooms):
    #We define two variables, the first to evaluate the loop and the second, 
    #to start the reserved quantity at zero
    reset = True
    reserve_quantity = [0, 0, 0, 0, 0]
    while reset == True:
        new_options_available = []
        new_options_available = show_rooms_available(type_rooms, amount_rooms, new_options_available)
        first_question = "What type of room do you want to reserve? (1-5): "
        option_room = check_answer(first_question, new_options_available)
        #Throught this index we will access to change the values in the list of initial
        #number of rooms and the list of reserved rooms
        index = int(option_room) - 1
        number_available = amount_rooms[index]
        options_amount = create_list_number(number_available)
        print()
        second_question = "How many rooms of this type will you reserve?: "
        chosen_quantity_option = check_answer(second_question, options_amount)
        chosen_quantity_option = int(chosen_quantity_option)
        reserve_quantity[index] = reserve_quantity[index] + chosen_quantity_option
        amount_rooms[index] = amount_rooms[index] - chosen_quantity_option
        print()
        #We verify that there are still rooms available to chosen from
        amount_diferent_zeros = list_non_zero(amount_rooms) 
        if amount_diferent_zeros == True:
            third_question = "Do you want to reserve more rooms?(y/n): "
            more_rooms = check_answer(third_question, available_yes_no)
            if more_rooms in available_yes_no[0:3]:
                reset = True
                print("\nOk. Let's go again.!!!\n")
            else:
                reset = False
        else:
            print("There aren't rooms available to reserve")
            reset = False
    return reserve_quantity

#Function to store user data
def user_data():
    list_user = []
    print("\nPersonal Information:\n")
    name = input("What is your name?: ")
    last_name = input("What is your last name?: ")
    id = input("What is your ID/passport?: ")
    list_user.append(name)
    list_user.append(last_name)
    list_user.append(id)
    return list_user

#Function to print the final summary of the reservations made and personal information
def final_summary(country, city, date, list_user_data, list_type_rooms, list_rooms_reserve, cost):
    #Loop to calculate total cost
    count = 0
    for i in range(0, 5):
        count = count + cost[i]*list_rooms_reserve[i]
    #First part of the final message, general information
    summary_final = f"""
    ****************    Final Summary    *********************

        Date:       {date}
        Country:    {country}
        City:       {city}

    ---------------     Reserved rooms    -------------------- 
    """
    #Second part. Information on reserved rooms
    print(summary_final)
    j = 0
    for i in list_rooms_reserve:
        if i != 0:
            print(f"         *{list_type_rooms[j]}:     {list_rooms_reserve[j]} rooms ($ {cost[j] * list_rooms_reserve[j]}.00)")
            print()
        j = j + 1
    #Third part. Personal information and total cost of reserve
    personal_information = f"""
    ---------------   Personal Information    ----------------
    
        Name:       {list_user_data[0]}
        Last name:  {list_user_data[1]}
        ID/Passport:{list_user_data[2]}

    ----------------------------------------------------------

    Total Cost =    {count}

    **********************************************************
    """
    print(personal_information)

#Message to exit the program
def message_custom(sentence):
    print()
    print(sentence)
    print("Thank you")
    print("Come back soon\n")

