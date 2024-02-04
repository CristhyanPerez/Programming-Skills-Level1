#Import libraries
import pandas as pd

#List of available options
available_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
available_specialties = ["General Medicine", "Emergency Care", "Clinical Analysis", "Cardiology", "Neurology", "Nutrition", "Occupational Therapy", "Traumatology", "Internal Medicine"]

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

df = transform_dataset("specialties.csv")
print(df)