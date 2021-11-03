# Write a class named Students that holds the following data about students
# 10/03/2021
# CSC221 M3Pro – Students Class
# Tyler Fuentes

#Creates a class for modules to operate within
class Student:
   
      
#Initialize variables to be passed within the 
    def __init__(self, student_id, first_name, last_name, student_major):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.student_major = student_major
        
        
    
    
#Allows the information to be printed in a more readable language for the user
    def __str__(self):
        text = ""
        text += f"{self.student_id:<10}{self.first_name:15}{self.last_name:<15}{self.student_major:<15}\n" 
        return text
       
#Bulk of the data to be displayed for the user to reference using lists ad formatting       
def main():
    
    
    stu1 = Student("47899", "Susan", "Meyers" , "Accounting")
    stu2 = Student("39119", "Mark", "Jones" , "Programming")
    stu3 = Student("39119", "Mark", "Jones" , "Programming") 
    print("_"*55, sep ="")
    print()
    print(f'{"ID Number":<10}{"First Name":<15}{"Last Name":<15}{"Major":<15}', "\n","_"*55, sep ="")
    print(stu1, stu2,stu3, sep = "")
    print("_"*55, sep ="")
#Calls main
if __name__ == '__main__':
    main()