# 10/1/# Text-based Adventure
# CSC 221-M3T3 Linked Lists
# 10/1/21
# Tyler Fuentes


class Room:
    """
    The Room class holds names, descriptions, and exits.
    In future it should also manage objects in rooms, somehow
    v3 - 10/4/21
    """

    def __init__(self):
        """ Initialize an empty room"""
        self.name = "Empty Room"
        self.description = "No description"
        self.exits = {}

    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits

    def __str__(self):
        """ contains the name, description, and exits in a human-readable fashion"""
        text = self.name + "\n"
        text += self.description + "\n"
        # append all exits
        exitList = self.exits.keys() # this gives us a list of all directions ipresent in exits
        for direction in exitList:
            text += direction                     # North, South, etc. 
            text += ": " + self.exits[direction]  # prints in format "North: Living Room", etc.
            text += "\n"
        return text

    def describe(self):
        """ print full room description. """
        print(self.name)

    def look(self):
        """ prints the room description. """
        # Appends all the exits
        text = '\n'
        text += "Exits" + "\n"
        exitList = self.exits.keys() # this gives us a list of all directions present in exits
        for direction in exitList:
            text += direction                     # North, South, etc. 
            text += ": " + self.exits[direction] + "\n"

        print('\n',"Description: ", self.description, text, "\n", sep='')   

    # def getItem(self):
    #     inventory.append(self)


    def exit(self, direction):
        """
        input: an exit direction, as string
        output: a Room object - either the room the player
            has moved to, or the current room if
            movement failed.
        """   
        pass 
                   
            
def main():
    """
    Currently used for testing.
    TODO: uimplement doctests. """
    bedroom = Room( "Bedroom", 
                   "This is an average bedroom.",
                   { "north": "Bathroom",
                     "south": "Living Room",
                     } )
        
    livingRoom = Room ( "Living Room",
                       "A TV, sofa, and game console are here.",
                       { "north" : "Bedroom" } )
    
    bathroom = Room ( "Bathroom", 
                     "Somebody left the toothpaste uncapped again.",
                     { "south" : "Bedroom" } )
    
    kitchen = Room ( "Kitchen", 
                     "Smells like bacon despite a clean appearance.",
                     { "west" : "Bedroom" } )

    # Place rooms in a dictionary.
    # (Game will handle this in the full version)
    roomDict = { bedroom.name: bedroom, 
                livingRoom.name: livingRoom,
                bathroom.name: bathroom,
                kitchen.name: kitchen}
    
if __name__ == "__main__":
    main()