Dictionaries = {} #Dictionaries

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
#////////FOR TESTING/////////////////// - Can be modify later
#Time from locl machine (For testing)
def Date():
    DateNow = datetime.datetime.now()
    print(DateNow)
    return
#//////////////////////////////////////

#function 1
def Add_Expense():
    print("Add an new expense!")
    #Set Time
    #year
    Valid_Choice = input("Enter the Year in numbers: ")
    if not Valid_Choice.isdigit():
        Valid_Choice = "0"
    Set_Year = int(Valid_Choice)
    #month
    Valid_Choice= input("Enter the Month in numbers: ")
    if not Valid_Choice.isdigit():
        Valid_Choice = "0"
    Set_Month = int(Valid_Choice)
    #date
    Valid_Choice = input("Enter the date in numbers: ")
    if not Valid_Choice.isdigit():
        Valid_Choice = "0"
    Set_Day = int(Valid_Choice)
    #check if the date is real
    try:
        datetime.datetime(Set_Year, Set_Month, Set_Day)
    except ValueError:
        Clear_Screen()
        print("This date does not exist.")
        Add_Expense()
        return
    Set_Expense = input("Enter the item: ")
    #Enter amount spend
    Valid_Choice = input("Enter The cost: ")
    if not Valid_Choice.isdigit():
        Valid_Choice = "0"
    Set_Cost = int(Valid_Choice)
    #////////FOR TESTING/////////////////// - Can be modify later
    #Choose Category
    #Depends on the category Ceil add
    #//////////////////////////////////////
    #add item
    # Year-Month-Day:Item:Cost
    New_Item = f"Date: {Set_Year:04d}-{Set_Month:02d}-{Set_Day:02d} Item: {Set_Expense} Cost:{Set_Cost}"
    List.append(New_Item)
    Clear_Screen()
    Select()
    return

def Remove_Expense():
    print("Choose any option below\n" \
    "        1 : Remove an expense\n" \
    "        2 : Remove Everything\n" \
    "        3 : Remove all expense in a category \n")
    Valid_Choice = input("Select an option: ")
    if not Valid_Choice.isdigit():
        Valid_Choice = "0"
    option = int(Valid_Choice)
    #Remove an expense
    if option == 1:
        #////////FOR TESTING/////////////////// - Can be modify later
        for item in List:
            print(item)
        #//////////////////////////////////////
        Item_delete = input("Enter the event's date and name in the same format to delete the event: \n")
            #found the item and delete it
        if Item_delete in List:
            List.remove(Item_delete)
            Clear_Screen()
            print("Item removed")
            Select()
        else:
            Clear_Screen()
            print("Item can not be found")
            Select()
    #Remove Everything
    elif option == 2:
        Valid_Choice = input("Press 1 to comfirm TO REMOVE EVERY ITEMS: ")
        if not Valid_Choice.isdigit():
            Valid_Choice = "0"
        Item_Remove = int(Valid_Choice)
        if Item_Remove == 1:
            List.clear()
            Clear_Screen()
            Select()
        else:
            Clear_Screen()
            print("Option canceled")
            Select()
    #Remove all expense in a category
    elif option == 3:
        print("In progress 3")
    else:
        print("Error")
        Remove_Expense()
    return
    
def Total_costs_calculation(a):
    global Total_costs
    Total_costs = sum(a)
    Total_costs_calculation(Costs_list)
    print (f"Total Expenses: {Total_costs}")


    
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
    Valid_Choice = input("Select an option: ")
    if not Valid_Choice.isdigit():
        Valid_Choice = "0"
    option = int(Valid_Choice)
    if option == 1:
        Add_Expense()
    elif option == 2:
        Clear_Screen()
        Remove_Expense()
    elif option ==3 :
        print("In progress 3")
        Select()
    else:
        #////////FOR TESTING/////////////////// - Can be modify later
        print(Dictionaries)
        #//////////////////////////////////////
        print("ERROR")
        Select()
    return

Select()
