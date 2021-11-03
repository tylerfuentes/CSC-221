# This project organizes a class into various rooms and provides a description for each
# 09/26/2021
# CSC221 M3T1 – Class Rooms
# Tyler Fuentes


rooms = {

    1: {'bedroom': 'You wake up looking up at your ceiling. The door to the living room lies to the east and the master bath is located to the west.', 'east': 2, 'west':1},
    2: {'master bath': 'The floor is wet and moist towels are strewn about.', 'east': 2},
    3: {'living room': 'This is a brighter room. You see the patio to the north, and the study to the west.', 'north': 3, 'west': 1},
    4: {'Patio': 'The sun is shining and you feel a cool breeze.', 'south':4},
    5: {'kitchen': 'The counters are clean but the room smells of burnt toast.', 'south': 4}}


current_room = 1

keepPlaying = True
while keepPlaying:
    choice = int(input("Enter a choice between 2 and 6: "))
    if choice== 7:
        keepPlaying = False
    else:
        roomNumber = choice - 1  # because the room is actually 0, 1, 2, 3, 4
        myRoom = rooms[roomNumber]
        print(myRoom)
