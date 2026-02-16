#Lists for All expenses
List = []
Costs_list = []
#Lists for food expenses
Food_List = []
Food_costs_list = []
#Lists for entertainment expenses
Entertainment_List = []
Entertainment_costs_List = []
#Lists for necessities expenses
Daily_necessities_List = []
Daily_necessities_costs_List = []
#Lists for necessities expenses
Else_List = []
Else_costs_List = []

Dictionaries = {
    "Food and Drink" : Food_costs_list,
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
#Time from locl machine (For testing)
def Date():
    DateNow = datetime.datetime.now()
    print(DateNow)
    return

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
    Set_Cost = float(Vaild_Choice)
    #Choose Category
    print("Choose any Categories below\n" \
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
    #Depends on the category Ciel add
    #add item
    # Year-Month-Day:Item:Cost
    New_Item = f"{Set_Year:04d}-{Set_Month:02d}-{Set_Day:02d}:{Set_Expense}:{Set_Cost}, Category:{Set_Category}"
    List.append(New_Item)
    Costs_list.append(Set_Cost)
    if Keep == "A":
        Food_List.append(New_Item)
        Food_costs_list.append(Set_Cost)
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
    print("ADDED")
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
        #////////FOR TESTING/////////////////// - Can be modify later
        for item in List:
            print(item)
        #//////////////////////////////////////
        Item_delete = input("Enter the event's date and name in the same format to delete the event: \n")
            #found the item and delete it
        if Item_delete in List:
            index_of_List = List.index(Item_delete)
            List.remove(Item_delete)
            Costs_list.remove(Costs_list[index_of_List])

            if Item_delete in Food_List:
                index_of_List = Food_List.index(Item_delete)
                Food_List.remove(Food_List[index_of_List])
                Food_costs_list.remove(Food_costs_list[index_of_List])

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
            Food_costs_list.clear()
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
        if option == 1:
            print("All Expenses in Food and Drink will be removed")
            print("input 1 to comfirm")
            comfirm = int(input("Input: "))
            if comfirm == 1:
                Deleate_expence = set(List) & set(Food_List)
                Deleate_expence_cost = set(Costs_list) & set(Food_costs_list)
                List_new = [x for x in List if x not in Deleate_expence]
                List_new_cost = [x for x in Costs_list if x not in Deleate_expence_cost]
                List[:] = List_new
                Costs_list[:] = List_new_cost
                Food_List.clear()
                Food_costs_list.clear()

                Clear_Screen()
                print("Removed")
                Select()
            else:
                Clear_Screen()
                print("Remove Canceled")
                Select()

        if option == 2:
            print("All Expenses in Entertainment will be removed")
            print("Press 1 to comfirm")
            comfirm = int(input("Input: "))
            if comfirm == 1:
                Deleate_expence = set(List) & set(Entertainment_List)
                Deleate_expence_cost = set(Costs_list) & set(Entertainment_costs_List)
                List_new = [item for item in List if item not in Deleate_expence]
                List_new_cost = [item for item in Costs_list if item not in Deleate_expence_cost]
                List[:] = List_new
                Costs_list[:] = List_new_cost
                Entertainment_List.clear()
                Entertainment_costs_List.clear()

                Clear_Screen()
                print("Removed")
                Select()
            else:
                Clear_Screen()
                print("Remove Canceled")
                Select()

        if option == 3:
            print("All Expenses in Daily necessities will be removed")
            print("Press 1 to comfirm")
            comfirm = int(input("Input: "))
            if comfirm == 1:
                Deleate_expence = set(List) & set(Daily_necessities_List)
                Deleate_expence_cost = set(Costs_list) & set(Daily_necessities_costs_List)
                List_new = [x for x in List if x not in Deleate_expence]
                List_new_cost = [x for x in Costs_list if x not in Deleate_expence_cost]
                List[:] = List_new
                Costs_list[:] = List_new_cost
                Daily_necessities_List.clear()
                Daily_necessities_costs_List.clear()

                Clear_Screen()
                print("Removed")
                Select()
            else:
                Clear_Screen()
                print("Remove Canceled")
                Select()

        if option == 4:
            print("All Expenses in Else will be removed")
            print("Press 1 to comfirm")
            comfirm = int(input("Input: "))
            if comfirm == 1:
                Deleate_expence = set(List) & set(Else_List)
                Deleate_expence_cost = set(Costs_list) & set(Else_costs_List)
                List_new = [x for x in List if x not in Deleate_expence]
                List_new_cost = [x for x in Costs_list if x not in Deleate_expence_cost]
                List[:] = List_new
                Costs_list[:] = List_new_cost
                Else_List.clear()
                Else_costs_List.clear()

                Clear_Screen()
                print("Removed")
                Select()
            else:
                Clear_Screen()
                print("Remove Canceled")
                Select()
        else:
            Clear_Screen()
            print("Remove Canceled")
            Select()
    else:
        Clear_Screen()
        print("Remove Canceled")
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
    print("All Expenses")
    for item in List:
        print(item)
    Total_costs_calculation(Costs_list)
    print (f"Total Expenses: {Total_costs}")
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
        Add_Expense()
        Clear_Screen()
    #Remove Expense
    elif option == 2:
        Clear_Screen()
        Remove_Expense()
    #Print Expenses in Category
    elif option ==3 :
        Clear_Screen()
        Category_Filter()
        Select()
    else:
        print("Please choose an vaild option")
        Select()
    return
#Start program
Select()
