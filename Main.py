List = []
Costs_list = []

Food_List = []
Food_costs_list = []

Entertainment_List = []
Entertainment_costs_List = []

Daily_necessities_List = []
Daily_necessities_costs_List = []

Else_List = []
Else_costs_List = []
#//////////////////////////////////////
Dictionaries = {
    "Food and " : Food_costs_list,
    "Entertainment" : Entertainment_costs_List,
    "Daily necessities" : Daily_necessities_costs_List,
    "Else" : Else_costs_List,
} #category

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
    print("Choose any Categories below\n" \
    "        1 : Food and  \n" \
    "        2 : Entertainment\n" \
    "        3 : Daily necessities\n" \
    "        4 : Else\n")
    Vaild_Choice = input("Select an option: ")
    if not Vaild_Choice.isdigit():
        Vaild_Choice = "0"
    option = int(Vaild_Choice)
    if option == 1:
        Set_Category = "Food and "
        Keep = "A"
    elif option == 2:
        Set_Category = "Entertainment"
        Keep = "B"
    elif option == 3 :
        Set_Category = "Daily necessities"
        Keep = "C"
    elif option == 4 :
        Set_Category = "Else"
        Keep = "D"
    else:
        print("ERROR")
        return
    #Depends on the category Ciel add
    #add item
    # Year-Month-Day:Item:Cost
    New_Item = f"{Set_Year:04d}-{Set_Month:02d}-{Set_Day:02d}:{Set_Expense}:{Set_Amount}, Category:{Set_Category}"
    List.append(New_Item)
    Costs_list.append(Set_Amount)
    if Keep == "A":
        Food_List.append(New_Item)
        Food_costs_list.append(Set_Amount)
    elif Keep == "B":
        Entertainment_List.append(New_Item)
        Entertainment_costs_List.append(Set_Amount)
    elif Keep == "C":
        Daily_necessities_List.append(New_Item)
        Daily_necessities_costs_List.append(Set_Amount)
    elif Keep == "D":
        Else_List.append(New_Item)
        Else_costs_List.append(Set_Amount)
    Clear_Screen()
    print("ADDED")
    Select()
    return

def Category_Filter():
    print("What catefory of list do yo want to see?")
    print("Choose any Categories below\n" \
    "        1 : Food and  \n" \
    "        2 : Entertainment\n" \
    "        3 : Daily necessities\n" \
    "        4 : Else\n")
    Vaild_Choice = input("Select an option: ")
    if not Vaild_Choice.isdigit():
          Vaild_Choice = "0"
    option = int(Vaild_Choice)
    if option == 1:
           
        for item in Food_List:
            print(item)
            Total_costs_calculation(Dictionaries["Food and "])
            print (f"Total Expenses: {Total_costs}")
    elif option == 2:
           
        for item in Entertainment_List:
            print(item)
            Total_costs_calculation(Dictionaries["Entertainment"])
            print (f"Total Expenses: {Total_costs}")
    elif option == 3 :
           
           for item in Daily_necessities_List:
            print(item)
            Total_costs_calculation(Dictionaries["Daily necessities"])
            print (f"Total Expenses: {Total_costs}")
    elif option == 4 :
           
        for item in Else_List:
            print(item)
            Total_costs_calculation(Dictionaries["Else"])
            print (f"Total Expenses: {Total_costs}")
    else:
        print("ERROR")
        return
    
def Total_costs_calculation(a):
    global Total_costs
    Total_costs = float(sum(a))
#   Main User Interface menu
def Select():

#////////FOR TESTING/////////////////// - Can be modify later
    for item in List:
        print(item)
    Total_costs_calculation(Costs_list)
    print (f"Total Expenses: {Total_costs}")
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
        Clear_Screen()
        Category_Filter()
        Select()
    else:
        print("ERROR")
        Select()
    return

Select()
