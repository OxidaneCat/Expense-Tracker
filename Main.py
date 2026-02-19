#Lists for All expenses
List = []
Costs_list = []
#Lists for food expenses
Food_List = []
Food_costs_List = []
#Lists for entertainment expenses
Entertainment_List = []
Entertainment_costs_List = []
#Lists for necessities expenses
Daily_necessities_List = []
Daily_necessities_costs_List = []
#Lists for necessities expenses
Else_List = []
Else_costs_List = []

#Filtered list
Dictionaries = {
    "Food and Drink" : Food_costs_List,
    "Entertainment" : Entertainment_costs_List,
    "Daily necessities" : Daily_necessities_costs_List,
    "Else" : Else_costs_List,
}

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

#Allow users to add expenses to the list and categories 
def Add_Expense():
    print("Add an new expense!")
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
    #if that date does not exist
    except ValueError:
        print("This date does not exist.")
        Add_Expense()
        return
    Set_Expense = input("Enter the item: ")
    if Set_Expense == "":
        Clear_Screen()
        print("ERROR, please write some word to describe the expense")
        Add_Expense()
    #Enter amount used
    Vaild_Choice = input("Enter The cost: ")
    if not Vaild_Choice.isdigit():
        Vaild_Choice = "0"
    Set_Cost = float(Vaild_Choice)
    #Choose Category for the expense
    print("Choose a Category below\n" \
    "        1 : Food and Drink \n" \
    "        2 : Entertainment\n" \
    "        3 : Daily necessities\n" \
    "        4 : Else\n")
    Vaild_Choice = input("Select an option: ")
    if not Vaild_Choice.isdigit():
        Clear_Screen()
        print("ERROR, please chose a vaild option")
        Add_Expense()
    option = int(Vaild_Choice)
    if option == 1:
        Set_Category = "Food and Drink"
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
        Clear_Screen()
        print("ERROR, please chose a vaild option")
        Add_Expense()
        return
    #add item
    # Year-Month-Day:Item:Cost
    New_Item = f"{Set_Year:04d}-{Set_Month:02d}-{Set_Day:02d}, {Set_Expense}, cost:{Set_Cost}, Category:{Set_Category}"
    List.append(New_Item)
    Costs_list.append(Set_Cost)
    if Keep == "A":
        Food_List.append(New_Item)
        Food_costs_List.append(Set_Cost)
    elif Keep == "B":
        Entertainment_List.append(New_Item)
        Entertainment_costs_List.append(Set_Cost)
    elif Keep == "C":
        Daily_necessities_List.append(New_Item)
        Daily_necessities_costs_List.append(Set_Cost)
    elif Keep == "D":
        Else_List.append(New_Item)
        Else_costs_List.append(Set_Cost)
    Clear_Screen()
    print("expense ADDED")
    Select()
    return

def Remove_Expense():
    print("Choose any option below\n" \
    "        1 : Remove an expense\n" \
    "        2 : Remove Everything\n" \
    "        3 : Remove all expense in a category \n")
    Valid_Choice = input("Select an option: ")
    if not Valid_Choice.isdigit():
        Clear_Screen()
        print("Option canceled")
        Select()
    option = int(Valid_Choice)
    #Remove an expense
    if option == 1:
        for item in List:
            print(item) #print the list
        Item_delete = input("Enter the event in the same format to delete the event: \n"
                            "YEAR-MONTH-DAY, EXPENSE, cost:COST, Category:CATEGORY \n")
            #found the item and delete it
        if Item_delete in List:
            index_of_List = List.index(Item_delete)
            List.remove(Item_delete)
            Costs_list.remove(Costs_list[index_of_List])

            if Item_delete in Food_List:
                index_of_List = Food_List.index(Item_delete)
                Food_List.remove(Food_List[index_of_List])
                Food_costs_List.remove(Food_costs_List[index_of_List])

            elif Item_delete in Entertainment_List:
                index_of_List = Entertainment_List.index(Item_delete)
                Entertainment_List.remove(Entertainment_List[index_of_List])
                Entertainment_costs_List.remove(Entertainment_costs_List[index_of_List])

            elif Item_delete in Daily_necessities_List:
                index_of_List = Daily_necessities_List.index(Item_delete) 
                Daily_necessities_List.remove(Daily_necessities_List[index_of_List])
                Daily_necessities_costs_List.remove(Daily_necessities_costs_List[index_of_List])

            elif Item_delete in Else_List:
                index_of_List = Else_List.index(Item_delete)
                Else_List.remove(Else_List[index_of_List])
                Else_costs_List.remove(Else_costs_List[index_of_List])

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
            Clear_Screen()
            print("Option canceled")
            Select()
        Item_Remove = int(Valid_Choice)
        if Item_Remove == 1:
            List.clear()
            Costs_list.clear()
            Food_List.clear()
            Food_costs_List.clear()
            Entertainment_List.clear()
            Entertainment_costs_List.clear()
            Daily_necessities_List.clear()
            Daily_necessities_costs_List.clear()
            Else_List.clear()
            Else_costs_List.clear()
            Clear_Screen()
            Select()
        else:
            Clear_Screen()
            print("Option canceled")
            Select()
            
    #Remove all expense in a category
    elif option == 3:
        Clear_Screen()
        print("Choose any Categories below to REMOVE all item\n" \
        "        1 : Food and Drink \n" \
        "        2 : Entertainment\n" \
        "        3 : Daily necessities\n" \
        "        4 : Else\n")
        Valid_Choice = input("Select an category: ")
        if not Valid_Choice.isdigit():
          Clear_Screen()
          print("Option canceled")
          Select()
        option = int(Valid_Choice)
        # remove everything in Food and Drink category
        if option == 1:
            Clear_Screen()
            print("All Expenses in Food and Drink category will be removed")
            print("input 1 to comfirm")
            comfirm = int(input("Input: "))
            if comfirm == 1:
                for item in Food_List:
                    if item in List:
                        index = List.index(item)
                        List.pop(index)
                        Costs_list.pop(index)
                Food_List.clear()
                Food_costs_List.clear()
                Clear_Screen()
                print("Removed")
                Select()
            else:
                Clear_Screen()
                print("Remove Canceled")
                Select()
        #Remove everything in entertainment category
        elif option == 2:
            print("All Expenses in Entertainment category will be removed")
            print("input 1 to comfirm")
            comfirm = int(input("Input: "))
            if comfirm == 1:
                for item in Entertainment_List:
                    if item in List:
                        index = List.index(item)
                        List.pop(index)
                        Costs_list.pop(index)
                Entertainment_List.clear()
                Entertainment_costs_List.clear()
                Clear_Screen()
                print("Removed")
                Select()
            else:
                Clear_Screen()
                print("Remove Canceled")
                Select()
        #remove everything in Daily necessities category
        elif option == 3:
            print("All Expenses in Daily necessities category will be removed")
            print("input 1 to comfirm")
            comfirm = int(input("Input: "))
            if comfirm == 1:
                for item in Daily_necessities_List:
                    if item in List:
                        index = List.index(item)
                        List.pop(index)
                        Costs_list.pop(index)
                Daily_necessities_List.clear()
                Daily_necessities_costs_List.clear()
                Clear_Screen()
                print("Removed")
                Select()
            else:
                Clear_Screen()
                print("Remove Canceled")
                Select()
        #remove everything in else category 
        elif option == 4:
            print("All Expenses in else category will be removed")
            print("input 1 to comfirm")
            comfirm = int(input("Input: "))
            if comfirm == 1:
                for item in Else_costs_List:
                    if item in List:
                        index = List.index(item)
                        List.pop(index)
                        Costs_list.pop(index)
                Else_List.clear()
                Else_costs_List.clear()
                Clear_Screen()
                print("Removed")
                Select()
            else:
                Clear_Screen()
                print("Remove function Canceled")
                Select()

        else:
            Clear_Screen()
            print("Remove function Canceled")
            Select()
    else:
        Clear_Screen()
        print("Remove function Canceled")
        Select()
    return

#Print Expenses in Category
def Category_Filter():
    print("What catefory of list do yo want to see?")
    print("Choose any Categories below\n" \
    "        1 : Food and Drink \n" \
    "        2 : Entertainment\n" \
    "        3 : Daily necessities\n" \
    "        4 : Else\n")
    Vaild_Choice = input("Select an option: ")
    if not Vaild_Choice.isdigit():
        Clear_Screen
        print("Action Canceled")
        Select()
    option = int(Vaild_Choice)
    #Print all Food and Drink expenses
    if option == 1:
        Clear_Screen()
        print("All Food and Drink expenses")
        for item in Food_List:
            print(item)
        Total_costs_calculation(Dictionaries["Food and Drink"])
        print (f"Total Expenses: {Total_costs}")
    #Print all Entertainment expenses
    elif option == 2:
        Clear_Screen()
        print("All Entertainment expenses")
        for item in Entertainment_List:
            print(item)
        Total_costs_calculation(Dictionaries["Entertainment"])
        print (f"Total Expenses: {Total_costs}")
    #Print all Necessities expenses
    elif option == 3 :
        Clear_Screen()
        print("All Necessities expenses")
        for item in Daily_necessities_List:
            print(item)
        Total_costs_calculation(Dictionaries["Daily necessities"])
        print (f"Total Expenses: {Total_costs}")
    #Print all Else exoenses
    elif option == 4 :
        Clear_Screen()
        print("All Else expenses")
        for item in Else_List:
            print(item)
        Total_costs_calculation(Dictionaries["Else"])
        print (f"Total Expenses: {Total_costs}")
    else:
        Clear_Screen()
        print("Action Canceled")
        Select()
        return
    
#Total costs calculation
def Total_costs_calculation(a):
    global Total_costs
    Total_costs = float(sum(a))

#Main User Interface menu
def Select():
    #Print All Expenses
    print()
    print("_______________________________________________")
    print("All Expenses")
    for item in List:
        print(item)
    #total cost of everything
    Total_costs_calculation(Costs_list)
    print (f"Total Expenses: {Total_costs}")
    print("_______________________________________________")
    #options
    print("Choose any option below\n" \
    "        1 : Add expense\n" \
    "        2 : Remove an expense\n" \
    "        3 : Filter expenses\n")
    Vaild_Choice = input("Select an option: ")
    if not Vaild_Choice.isdigit():
        Clear_Screen()
        Select()
    option = int(Vaild_Choice)
    #Add Expense
    if option == 1:
        Clear_Screen()
        Add_Expense()
    #Remove Expense
    elif option == 2:
        Clear_Screen()
        Remove_Expense()
    #Print Expenses in Category
    elif option == 3 :
        Clear_Screen()
        Category_Filter()
        Select()
    else:
        Clear_Screen()
        print("Please choose an vaild option")
        Select()
    return
#Start program
Select()
