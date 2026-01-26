Dictionaries = {} #category
#////////FOR TESTING/////////////////// - Can be modify later
List = []
#//////////////////////////////////////
#Clear the screen
import os
def Clear_Screen():
    #clear screen
    if os.name == 'nt': #For Windows
        os.system('cls')
    else: #For macOS and Linux
        os.system('clear')
    return

import datetime
#Time from locl machine (For testing)
def Date():
    DateNow = datetime.datetime.now()
    print(DateNow)
    return

def Add_Expense():
    print("Add an new expense!")
    global Set_Day,Set_Month,Set_Year,Set_Expense,Set_Category,Set_Amount
    #Set Time
    #year
    Vaild_Choice = input("Enter the Year in numbers: ")
    if not Vaild_Choice.isdigit():
        Vaild_Choice = "0"
    Set_Year = int(Vaild_Choice)
    #month
    Vaild_Choice = input("Enter the Month in numbers: ")
    if not Vaild_Choice.isdigit():
        Vaild_Choice = "0"
    Set_Month = int(Vaild_Choice)
    #date
    Vaild_Choice = input("Enter the date in numbers: ")
    if not Vaild_Choice.isdigit():
        Vaild_Choice = "0"
    Set_Day = int(Vaild_Choice)
    #check if the date is real
    try:
        datetime.datetime(Set_Year, Set_Month, Set_Day)
    except ValueError:
        print("This date does not exist.")
        Add_Expense()
        return
    Set_Expense = input("Enter the item: ")
    #Enter amount used
    Vaild_Choice = input("Enter The cost: ")
    if not Vaild_Choice.isdigit():
        Vaild_Choice = "0"
    Set_Amount = int(Vaild_Choice)
    #Choose Category
    #Depends on the category Ceil add
    #add item
    # Year-Month-Day:Item:Cost
    New_Item = f"{Set_Year:04d}-{Set_Month:02d}-{Set_Day:02d}:{Set_Expense}:{Set_Amount}"
    List.append(New_Item)
    Clear_Screen()
    print("ADDED")
    Select()
    return

#   Main User Interface menu
def Select():

#////////FOR TESTING/////////////////// - Can be modify later
    for item in List:
        print(item)
#//////////////////////////////////////

    print("Choose any option below\n" \
    "        1 : Add expense\n" \
    "        2 : Remove an expense\n" \
    "        3 : Filter expenses\n")
    Vaild_Choice = input("Select an option: ")
    if not Vaild_Choice.isdigit():
        Vaild_Choice = "0"
    option = int(Vaild_Choice)
    if option == 1:
        Add_Expense()
        Clear_Screen()
    elif option == 2:
        print("In progress 2")
        Select()
    elif option ==3 :
        print("In progress 3")
        Select()
    else:
        print("ERROR")
        Select()
    return

Select()
