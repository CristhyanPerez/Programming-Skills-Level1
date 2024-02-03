#Declare list
seasons = ["Summer", "Winter", "Autumn", "Spring"]
options_menu = ["1", "2"]
available_yes_no = ["y", "yes", "YES", "n", "no", "NO"]

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

#Funtion to evaluate the activities that can be carried out with 100 dollars
def option_100():
    question_1 = "\nWould you like to take a tour of the Swiss Alps? (y/n): "
    answer_1 = check_answer(question_1, available_yes_no)
    if answer_1 in available_yes_no[0:3]:
        summary_list = ["100", "Winter", "Switzerland", "to take a tour of the Swiss Alps"]
    else:
        summary_list = ["100", "Winter", "Andorra", "Skiing activities"]
    return summary_list

#Funtion to evaluate the activities that can be carried out with 200 dollars
def option_200():
    question_1 = "\nWould you like extrem sports? (y/n): "
    answer_1 = check_answer(question_1, available_yes_no)
    if answer_1 in available_yes_no[0:3]:
        summary_list = ["200", "Autumn", "Belgium", "Hiking and extreme sports activities"]
    else:
        question_2 = "\nWould you like cultural activities? (y/n): "
        answer_2 = check_answer(question_2, available_yes_no)
        if answer_2 in available_yes_no[0:3]:
            summary_list = ["200", "Autumn", "Austria", "Cultural and historical activities."]
        else:
            summary_list = option_100()
    return summary_list

#Funtion to evaluate the activities that can be carried out with 300 dollars
def option_300():
    question_1 = "\nWould you like extrem sports? (y/n): "
    answer_1 = check_answer(question_1, available_yes_no)
    if answer_1 in available_yes_no[0:3]:
        question_2 = "\nDo you prefer spring to fall? (y/n): "
        answer_2 = check_answer(question_2, available_yes_no)
        if answer_2 in available_yes_no[0:3]:
            summary_list = ["300", "Spring", "France", "Hiking and extreme sports activities"]
        else:
            summary_list = ["200", "Autumn", "Belgium", "Hiking and extreme sports activities"]
    else:
        question_3 = "\nWould you like cultural activities? (y/n): "
        answer_3 = check_answer(question_3, available_yes_no)
        if answer_3 in available_yes_no[0:3]:
            question_4 = "\nDo you prefer spring to fall? (y/n): "
            answer_4 = check_answer(question_4, available_yes_no)
            if answer_4 in available_yes_no[0:3]:
                summary_list = ["300", "Spring", "Italy", "Cultural and historical activities"]
            else:
                summary_list = ["200", "Autumn", "Autria", "Cultural and historical activities"]
        else:
            summary_list = option_100()
    return summary_list

#Funtion to evaluate the activities that can be carried out with 400 dollars
def option_400():
    question_1 = "\nWould you like extrem sports? (y/n): "
    answer_1 = check_answer(question_1, available_yes_no)
    if answer_1 in available_yes_no[0:3]:
        question_2 = "\nDo you like the summer season? (y/n): "
        answer_2 = check_answer(question_2, available_yes_no)
        if answer_2 in available_yes_no[0:3]:
            summary_list = ["400", "Summer", "Spain", "Hiking and extreme sports activities"]
        else:
            question_3 = "\nDo you prefer spring to fall? (y/n): "
            answer_3 = check_answer(question_3, available_yes_no)
            if answer_3 in available_yes_no[0:3]:
                summary_list = ["300", "Spring", "France", "Hiking and extreme sports activities"]
            else:
                summary_list = ["200", "Autumn", "Belgium", "Hiking and extreme sports activities"]
    else:
        question_4 = "\nWould you like to go to the crystal clear sea? (y/n): "
        answer_4 = check_answer(question_4, available_yes_no)
        if answer_4 in available_yes_no[0:3]:
            summary_list = ["400", "Summer", "Portugal", "Activities on the beaches"]
        else:
            question_5 = "\nWould you like cultural activities? (y/n): "
            answer_5 = check_answer(question_5, available_yes_no)
            if answer_5 in available_yes_no[0:3]:
                question_6 = "\nDo you prefer spring to fall? (y/n): "
                answer_6 = check_answer(question_6, available_yes_no)
                if answer_6 in available_yes_no[0:3]:
                    summary_list = ["300", "Spring", "Italy", "Cultural and historical activities"]
                else:
                    summary_list = ["200", "Autumn", "Autria", "Cultural and historical activities"]
            else:
                summary_list = option_100()
    return summary_list

