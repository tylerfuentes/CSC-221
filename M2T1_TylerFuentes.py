'''
 For this assignment, complete the sample code and Self Check code for 9.3, 
 9.4, and 9.5 from the textbook. You should be able to put this code together
 into one or more short programs, to confirm that they work.
'''
# 09/12/2021
# CSC221-M2T1 
# Tyler Fuentes

# 9.3 Sample Code 
with open('accounts.txt', mode='w') as accounts:
    accounts.write('100 Jones 24.98\n')
    accounts.write('200 Doe 345.67\n')
    accounts.write('300 White 0.00\n')
    accounts.write('400 Stone -42.16\n')
    accounts.write('500 Rich 224.62\n')

# 9.3.1 Self Check
with open('grades.txt', mode='w') as grades:
    grades.write('1 Red A\n')
    grades.write('2 Green B\n')
    grades.write('3 White C\n')

# 9.3.2 Reading Data from a text file
with open('accounts.txt', mode='r') as accounts:
    print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
    for record in accounts:
        account, name, balance = record.split()
        print(f'{account:<10}{name:<10}{balance:>10}') 
        

# 9.3.2 Self Check
print()
with open ('grades.txt', 'r') as grades:
    print(f'{"ID":<4}{"Name":<7}{"Grade"}')
    for record in grades:
        student_id, name, grade = record.split()
        print(f'{student_id:<4}{name:<7}{grade}')
        
# 9.4 Sample Code: Updating Text Files
accounts = open('accounts.txt', 'r')

temp_file = open('temp_file.txt', 'w')
with accounts, temp_file:
    for record in accounts:
        account, name, balance = record.split()
        if account != '300':
            temp_file.write(record)
        else:
            new_record = ''.join([account, 'Williams', balance])
            temp_file.write(new_record + '\n')

# 9.4 Self Check
accounts = open('accounts.txt', 'r')
temp_file = open('temp_file.txt', 'w')
with accounts, temp_file:
    for record in accounts:
        account, name, balance = record.split()
        if name != 'Doe':
            temp_file.write(record)
        else:
            new_record = ''.join([account, 'Smith', balance])
            temp_file.write(new_record + '\n')
import os
os.remove('accounts.txt')
os.rename('temp_file.txt','accounts.txt')


#9.5 Serialization with JSON....Sample Code
accounts_dict = {'accounts': [
    {'account': 100, 'name': 'Jones', 'balance': 24.98},
    {'account': 200, 'name': 'Doe', 'balance': 345.67}]}

#Serializing an object to json
import json
with open('accounts.json','w') as accounts:
    json.dump(accounts_dict, accounts)

#Deserializing the json text
with open('accounts.json','r') as accounts:
    accounts_json = json.load(accounts)
print()
print(accounts_json)
print()
print(accounts_json['accounts'])
print()
print(accounts_json['accounts'][0])
print()
print(accounts_json['accounts'][1])
print()

with open('accounts.json','r') as accounts:
    print(json.dumps(json.load(accounts), indent=4))
    
#9.5 Self Check
import json
grades_dict = {'gradebook':
    [{'student_id': 1, 'name': 'Red', 'grade': 'A'},
    {'student_id': 2, 'name': 'Green', 'grade': 'B'},
    {'student_id': 3, 'name': 'White', 'grade': 'A'}]}
    
with open('grades.json','w') as grades:
    json.dump(grades_dict, grades)
    
with open('grades.json','r') as grades:
    print(json.dumps(json.load(grades), indent=4))
    


