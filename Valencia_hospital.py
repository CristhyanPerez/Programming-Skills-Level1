#Import libraries
import pandas as pd

#List of available options
available_specialties = ["General Medicine", "Emergency Care", "Clinical Analysis", "Cardiology", "Neurology", "Nutrition", "Occupational Therapy", "Traumatology", "Internal Medicine"]
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
    return option_user

#Funtion to transform the csv file into a pandas dataframe
def transform_dataset(file):
    dataframe = pd.read_csv(file, sep = "\t")
    return dataframe

#Function to choose specialty to be attended
def specialty_user(number_options, options_specialty):
    print("Specialties in this hospital:\n")
    list_options_01 = []
    for i in range(1, number_options + 1):
        print(f"{i}- { options_specialty[i-1]}")
        option = str(i)
        list_options_01.append(option)
    question = f"\nChose the specialty (1 - {number_options}): "
    option_choose = check_answer(question, list_options_01)
    index = int(option_choose) - 1
    specialty_final = options_specialty[index]
    return specialty_final

#Function to choose the doctor
def doctor_user(dataframe, specialty_choose):
    print("\nDoctors in this specialty:\n")
    filtered_data = dataframe[dataframe['Specialty'] == specialty_choose]
    doctors_data_list = filtered_data['Doctor'].tolist() 
    list_options_02 = ["1", "2", "3"]
    for i in range(1, 4):
        print(f"{i}- { doctors_data_list[i-1]}")
    question = f"\nChose the doctor (1 - 3): "
    option_choose = check_answer(question, list_options_02)
    index = int(option_choose) - 1
    doctor_final = doctors_data_list[index]
    return doctor_final

#Function to show available schedules
def schedule_user(dataframe, doctor_choose, general_list):
    schedule_list_start = general_list[2::3]
    print("\nAvailable times:\n")
    index_data = dataframe[dataframe['Doctor'] == doctor_choose].index[0]
    selected_row = dataframe.iloc[index_data]
    list_row = selected_row.tolist()
    list_schedules = list_row[2:6]
    #Remove equal schedules from the list
    for w in schedule_list_start:
        for z in list_schedules:
            if w == z:
                list_schedules.remove(w)
    lenght_list = len(list_schedules)
    list_options_03 = []
    for i in range(1, lenght_list + 1):
        print(f"{i}- { list_schedules[i-1]}")
        option = str(i)
        list_options_03.append(option)
    question = f"\nChose the schedule (1 - {lenght_list}): "
    option_choose = check_answer(question, list_options_03)
    index = int(option_choose) - 1
    schedule_final = list_schedules[index]
    return schedule_final

#Function to print the final summary
def final_summary(list_appointments):
    first_part = """
    **********************************************************

    ****************    Final Summary    *********************

    """
    print(first_part)
    #Second part
    lenght_final = len(list_appointments)
    j = 1
    for i in range(0,lenght_final,3):
        print(f"      ----------     Booked appointment #{j}    -------------  \n")
        print(f"         *Specialty:    {list_appointments[i]}")
        print(f"         *Doctor:       {list_appointments[i+1]}")
        print(f"         *Schedule:     {list_appointments[i+2]}")
        print()
        j = j + 1
    #Third part
    last_part = f"""
    **********************************************************
    """
    print(last_part)

#Message to exit the program
def message_custom(sentence):
    print()
    print(sentence)
    print("Thank you")
    print("Come back soon\n")

#Menus
#Program entry menu
menu_entry = """
****************    Valencia Hospital    *********************

Welcome, first, you have to log in.

* The password is made up of the following:
  Username + space + number of characteres in the user word

Example:
Username: Cristhyan
Password: Cristhyan 9

Remember that you only have three attempts
"""

menu_app = """Welcome again.

You must take into account the following to manage your medical
appointment:

* You can only book one appointment per specialty.
* Three is the maximum limit of appointments you can take.
* You cannot choose two appointments of different specialties 
  at the same time.

Let's start
"""

#Main Function
def main():
    print(menu_entry)
    login = login_attempts(3)
    if login == True:
        print("****************    Login Successfully   ********************")
        reset_main_menu = True
        number_appointments = 1
        number_start = 9
        list_user_final = []
        while reset_main_menu == True and number_appointments <= 3:
            print("\n**************************************************************\n")
            print(menu_app)
            df = transform_dataset("specialties.csv")
            specialty_user_app = specialty_user(number_start, available_specialties)
            doctor_user_app = doctor_user(df, specialty_user_app)
            schedule_user_app = schedule_user(df, doctor_user_app, list_user_final)
            reserve_appointment = check_answer("\nDo you want to book this appointment?(y/n): ", available_yes_no)
            if reserve_appointment in available_yes_no[0:3]:
                print(f"\n****************  Succesful reservation #{number_appointments}  ****************** \n")
                list_user_final.append(specialty_user_app)
                list_user_final.append(doctor_user_app)
                list_user_final.append(schedule_user_app)
                number_start = number_start - 1
                number_appointments = number_appointments + 1
                index_specialty = available_specialties.index(specialty_user_app)
                available_specialties.pop(index_specialty)
                if number_appointments <=3:
                    return_menu = check_answer("\nDo you want to return to the main menu?(y/n): ", available_yes_no)
                    if return_menu in available_yes_no[0:3]:
                        print("\nLet's start again..!!!!\n")
                        reset_main_menu = True
                    else:
                        message_custom("")
                        reset_main_menu = False
            else:
                return_menu = check_answer("\nDo you want to return to the main menu?(y/n): ", available_yes_no)
                if return_menu in available_yes_no[0:3]:
                    print("\nLet's start again..!!!!\n")
                    reset_main_menu = True
                else:
                    message_custom("")
                    reset_main_menu = False
        if number_start != 9:
            final_summary(list_user_final)
    else:
        message_custom("Maximum number of attempts")

#Entry point
if __name__ == "__main__":
    main()