# This project is to demonstrate reading objects from a file
# and displaying them for the user
# 09/26/2021
# CSC221 M2HW – FileExceptions
# Tyler Fuentes


# intialize the text file and assign it to 'f' and pass to avoid plumbing issues
f = open('sotu.txt',mode='r')


# menu to drive program until user wishes to end
def getOption(f):
    display_menu()
    
    
    keepPlaying = True
    while keepPlaying:
        choice = int(input("Enter choice: "))
        if choice == 1:
            print("Displaying Entire Speech: ")
            speech(f)
        elif choice == 2:
            print("Displaying Total Word Count: ")
            return wordCount(f)
        
        elif choice == 3:
            print("Displaying Total Character Count: ")
            charCount(f)
            
        elif choice == 4:
            print("Displaying Average Word Length: ")
            avgLength(f)
            
        elif choice == 5:
            print("Displaying Top Ten Longest Words: ")
            topTen(f)
        elif choice == 6:
             print("...Ending Program. Please Have a Nice Day...")
             f.close()
             keepPlaying = False       
        else:
            print("Please enter a valid menu entry.")
            print()
            return getOption(f)
        print()
        
# Displays the entire txt file for the user   
def speech(f):
    with open('sotu.txt',mode='r') as f:
        line = f.readlines()
        print(line)
        line = f.close()
    return getOption(f)
    
   
# Counts all the words in the txt file and displays to the user
def wordCount(f):
    with open('sotu.txt',mode='r') as f:
        data = f.read()
        words = data.split()
        print('Number of words in the 2020 SOTU address :', len(words))
       
    return getOption(f)

# Shows the user how many characters present in the txt file 
def charCount(f):
    with open('sotu.txt',mode='r') as f:
        data = f.read()
        numChar = len(data)
        print('Number of characters in the 2020 SOTU address :', numChar)
        
    return getOption(f)

# Presents the average length given all the words present in the txt file
def avgLength(f):
    with open('sotu.txt',mode='r') as f:
        data = f.read()
        words = data.split()
        numChar = len(data)
        avg = numChar / len(words)
        print('Average word length in the 2020 SOTU address :', round(avg))
        return getOption(f)

# Displays the top ten longest words in the txt file
def topTen(f):
    with open('sotu.txt',mode='r') as f:
           data = sorted(f.read().replace('\n','').split(' '),reverse=True)
           print (data[:10])
       
     
          
    
# Called after getOption is called to present menu to user after every decision.
def display_menu():
    print()
    print()
    print("MENU")
    print("---------------")
    print("1) Display Entire Speech.")
    print("2) Display Total Word Count.")
    print("3) Display Total Character Count.")
    print("4) Display Average Word Length.")
    print("5) Display Top Ten Longest Words.")
    print("6) Exit Program.")
    print()
    
if __name__ == '__main__':
   getOption(f)