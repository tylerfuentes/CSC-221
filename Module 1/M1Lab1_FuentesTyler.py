'''
This program is designed to allow the user to create a list and manipulate it
CSC221 M1LAB1
Tyler Fuentes
08/30/2021
'''


import sys

# Initialize list within the main function instead of globally the calls getOption
def main():
    list1 =[]
    getOption(list1)


# getOption drives the menu-driven program by asssigning options to numbers
def getOption(list1): 
    
    option = 0
    while option != 5:
        display_menu(list1)
        option = int(input("Enter a menu option: "))
# At the end of each option, a function  is used to direct the user's choice 
# to the appropriate module
        if option == 1:
            print("Create a list: ")
            createList(list1)
            return getOption(list1)
        elif option == 2:
           print("Below is your list: ")
           print(list1)
        elif option == 3:
             print("You have chosen to double the numbers in your list.")
             Dbl_list(list1)
        elif option == 4:
            print("Program ended. The list you created is displayed below: ")
            print(list1)
            sys.exit()
        else:
# Encourages the user to use the designated commands
            print("Please enter a valid menu entry.")
            print()
            return getOption(list1)

# createList loops to add numbers until the user wishes to stop
def createList(list1):
        choice = "Yes"
        while choice != "N":
            a_num = int(input("Enter a number: "))
            list1.append(a_num)
            print(list1)
            choice = input(str("Type Y to add another number or N to quit: "))
            if choice == "N":
                print("You current list is ", list1)
                print("Returning to menu.")
#Upon the "N" selection, the program reroutes the user to the main menu
        return getOption(list1)
                
                
# Doubles the numbers in sqr then reassigns sqr to variable list1 to manage
# data under one list

def Dbl_list(list1):
    sqr = []
    for i in list1:
        sqr.append(i*2)
    print(sqr) 
    list1 = sqr
    return getOption(list1)
    
# Display menu for user interface
def display_menu(list1):
    print()
    print()
    print("MENU")
    print("---------------")
    print("1) Create list")
    print("2) Display list")
    print("3) Display doubled values for the elements in your list")
    print("4) Exit")
    print()

main()