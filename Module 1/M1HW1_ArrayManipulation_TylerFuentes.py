# This project is to practice creating an array and manipulate it
# 09/03/2021
# CSC221 M1HW1 – Array Manipulations
# Tyler Fuentes

import sys
import numpy as np

def main():
    values = np.array([]) 
    getOption(values)
    

#Displays the menu options for the user to see and reference
def display_menu(values):
    print()
    print()
    print("MENU")
    print("---------------")
    print("1) Create a 3-by-3 Array")
    print("2) Display cubed values for elements in array")
    print("3) Add 7 to every element and display result") 
    print("4) Multiply elements by 6 and display result") 
    print("5) Exit")
    print()
    

#This module will allow the user to make menu-driven decisions
def getOption(values): 
    valueArray = np.array(values)
    option = 0
    while option != 6:
        display_menu(values)
        option = int(input("Enter a menu option: "))
        print()
        if option == 1:
            values = create_array(values)
        elif option == 2:
            cube_array(values,valueArray)
        elif option == 3:
            add_array(values,valueArray)
        elif option == 4:
            mult_array(values,valueArray)
        elif option == 5:
            print("Ending program.")
            sys.exit()
        else:
            print("Please enter a valid menu entry.")
            print()
            return getOption(values)



#Creating the array from the ground up        
def create_array(values):
    values = ([])
    print("Input values for a 3-by-3 array")

    for i in range(9):
       a_num  = int(input("Enter a whole number: "))
       values.append(a_num) 
       print()
              
    valueArray = np.array(values).reshape(3,3)
    print("Your new array is posted below: ")
    print()
    
    for row in valueArray:
        for col in row:
            print(col, end = " ")
        print()
    
    print()
    print()
    return getOption(values)
    

#This module will cube the array values provided by the user
def cube_array(values,valueArray):
    if len(valueArray) == 0:
        print('The array is empty. Please return to the main menu')
        return getOption
    else:
        print("Source Array: ")
        print()
        valueArray = np.array(values).reshape(3,3)
        
        for row in valueArray:
            for col in row:
                print(col, end = " ")
            print()
        print("Cubed Array: ")
        print()
        valueArray_cubed = valueArray * valueArray * valueArray
        for row in valueArray_cubed:
            for col in row:
                print(col, end = " ")
            print()
        
        return valueArray





#This module will add 7 to the array values provided by the user
def add_array(values,valueArray):
    if len(valueArray) == 0:
        print('The array is empty. Please return to the main menu')
        return getOption
    
    else:
        print("Source Array: ")
        print()
        valueArray = np.array(values).reshape(3,3)
        print()
        for row in valueArray:
            for col in row:
                print(col, end = " ")
            print()
        
        print()
        
        print("Added Array: ")
        print()
        addValue_array = np.add(valueArray,7)
        for row in addValue_array:
            for col in row:
                print(col, end = " ")
            print()
        
    
#This module will multiply the array values provided by the user by 6
def mult_array(values,valueArray):
    if len(valueArray) == 0:
        print('The array is empty. Please return to the main menu')
        return getOption
    
    else:
        print("Source Array: ")
        print()
        valueArray = np.array(values).reshape(3,3)
        print()
        for row in valueArray:
            for col in row:
                print(col, end = " ")
            print()
        
        print()
        print("Product Array: ")
        print()
        product_array = np.multiply(valueArray,6)
        for row in product_array:
            for col in row:
                print(col, end = " ")
            print()
        

main()

'''
IMPORT system library
IMPORT numpy as np

DEFINE main function
    CREATE empty array
    CALL getOption function

CREATE display menu
CREATE menu driven function getOption using if-elif-else statements
PASS values,valueArray throughout function to allow comms between functions

CREATE empty list
REQUEST user to enter whole integers for 3 by 3 array
CONVERT list to array
    REMOVE brackets using for (col,row) loop
    RETURN getOption

DEFINE cube_array function
    if length of valueArray == 0:
        DISPLAY The array is empty. Please return to the main menu
        RETURN getOption
    
    else
    
    Create an array where all the original values are cubed
    for row in valueArray:
            for col in row:
                print(col, end = " ")
            print()
    valueArray_cubed = valueArray * valueArray * valueArray
    for row in valueArray_cubed:
            for col in row:
                print(col, end = " ")
            print()

DEFINE function add_array

    if length of valueArray == 0:
        DISPLAY The array is empty. Please return to the main menu
        RETURN getOption
    
    else
    
    USE np.add function to add 7 to all the values in valueArray
    for row in valueArray:
            for col in row:
                print(col, end = " ")
            print()
    addValue_array = np.add(valueArray,7)
    for row in addValue_array:
            for col in row:
                print(col, end = " ")
            print()
            
DEFINE function mult_array
     if length of valueArray == 0:
        DISPLAY The array is empty. Please return to the main menu
        RETURN getOption
    
    else
    
    USE np.multiply function to multiply all values in valueArray by 6
    for row in valueArray:
            for col in row:
                print(col, end = " ")
            print()
    addValue_array = np.multiply(valueArray,6)
    for row in addValue_array:
            for col in row:
                print(col, end = " ")
            print()
            
CALL main

the sys.exit function with option 5 allows the user to terminate the program
if desired by inputting 5
'''