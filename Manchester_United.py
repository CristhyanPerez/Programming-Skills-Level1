#Import libraries
import pandas as pd

#Declare list
jersey_numbers = ["5", "7", "8", "11", "17"]

#Declarate the dataframe
df = pd.DataFrame(columns=["Name", "Goals", "Points Speed", "Points Assists", "Passing accuracy", "Defensive Involving", "Jersey Number"])
data = pd.DataFrame([
    {"Name": "Bruno Fernandez", "Goals": 5, "Points Speed": 6, "Points Assists": 9, "Passing accuracy": 10, "Defensive Involving": 3, "Jersey Number": 8},
    {"Name": "Rasmus Hojlund", "Goals": 12, "Points Speed": 8, "Points Assists": 2, "Passing accuracy": 6, "Defensive Involving": 2, "Jersey Number": 11},
    {"Name": "Harry Maguire", "Goals": 1, "Points Speed": 5, "Points Assists": 1, "Passing accuracy": 7, "Defensive Involving": 9, "Jersey Number": 5},
    {"Name": "Alejandro Garnacho", "Goals": 8, "Points Speed": 7, "Points Assists": 8, "Passing accuracy": 6, "Defensive Involving": 0, "Jersey Number": 17},
    {"Name": "Mason Mount", "Goals": 2, "Points Speed": 6, "Points Assists": 4, "Passing accuracy": 8, "Defensive Involving": 1, "Jersey Number": 7}
])
df = pd.concat([df, data], ignore_index = True)

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

#Function to show the characteristics of a specific player throught the jersey number
def player_characterics(list_options_jersey):
    print("Jersey number available to review: 5, 7, 8, 11, 17")
    print()
    question = "Choose a jersey number: "
    option_jersey = int(check_answer(question, list_options_jersey))
    #Searched in the dataframe, to which index the entered jersey corresponds
    index = df[df["Jersey Number"] == option_jersey].index[0]
    summary = f"""
    ********************************************
            
            Jersey Number: {str(option_jersey)}

    Name:                   {df.loc[index, 'Name']} 
    Goals:                  {df.loc[index, 'Goals']}
    Points Speed:           {df.loc[index, 'Points Speed']}
    Points Assists:         {df.loc[index, 'Points Assists']}
    Passing accuracy:       {df.loc[index, 'Passing accuracy']}
    Defensive Involving:    {df.loc[index, 'Defensive Involving']}

    ********************************************
    """
    print(summary)

#Function to compare two players using the jersey numbers
def player_compare(list_options_jersey):
    list_available = []
    list_available = list_options_jersey
    print("Jersey number available to review: 5, 7, 8, 11, 17\n")
    #We request the first jersey number to compare
    question_1 = "Choose a jersey number: "
    option_jersey_1 = check_answer(question_1, list_available)
    print(list_available)
    list_available.remove(option_jersey_1)
    option_jersey_1 = int(option_jersey_1)
    index_1 = df[df["Jersey Number"] == option_jersey_1].index[0]
    print("\nRemember to choose a different jersey number to be  able to compare.\n")
    #We request the second jersey number to compare
    question_2 = "Choose a jersey number: "
    option_jersey_2 = check_answer(question_2, list_available)
    option_jersey_2 = int(option_jersey_2)
    index_2 = df[df["Jersey Number"] == option_jersey_2].index[0]
    #Summary to show the comparision
    summary = f"""
    **********************************************************
            
                        {df.loc[index_1, 'Name']}     {df.loc[index_2, 'Name']}   

    Jersey Number:          {str(option_jersey_1)}                  {str(option_jersey_2)}
    Goals:                  {df.loc[index_1, 'Goals']}                  {df.loc[index_2, 'Goals']}
    Points Speed:           {df.loc[index_1, 'Points Speed']}                  {df.loc[index_2, 'Points Speed']}       
    Points Assists:         {df.loc[index_1, 'Points Assists']}                  {df.loc[index_2, 'Points Assists']} 
    Passing accuracy:       {df.loc[index_1, 'Passing accuracy']}                  {df.loc[index_2, 'Passing accuracy']}      
    Defensive Involving:    {df.loc[index_1, 'Defensive Involving']}                  {df.loc[index_2, 'Defensive Involving']}     

    **********************************************************
    """
    print(summary)

#Function to show the most relevant statistic
def players_statistics():
    summary = f"""
    ********************************************
            
            General Statistics

    The fastest player:                   
        {df.loc[index, 'Name']} 

    The top goal scorer:                  
        {df.loc[index, 'Goals']}

    The player with the most assists:           
        {df.loc[index, 'Points Speed']}

    The player with the highest passing accuracy:         
        {df.loc[index, 'Points Assists']}

    the player with the most defensive involvements:      
        {df.loc[index, 'Passing accuracy']}
    
    ********************************************
    """
    print(summary)
    pass