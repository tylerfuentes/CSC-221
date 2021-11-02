# Text-based Adventure. version 4
# This version has rooms which can be navigated and present descriptions on user intput.
# CSC 221-M3Lab1 Linked Lists
# 10/8/21
# Tyler Fuentes

# Imports elements from sister file "Room"
from Room import Room

inventory = []
# Allows for smoother passing of variables 
class Game:
    """
    The Game class organizes all game data in a central location.
    Usage:
    - Set up game using your choice of room configurations
      (TODO: Read these from a file in future)
    - call loop()
    """
# Initializes variables to be utilized for text adventure
    def __init__(self):
        """ Initialize object (with no rooms) """
        #self.player = player.Player()
        self.rooms = { } # stored in dictionary
        self.here = None # TODO: move this to Player
        self.isPlaying = True
        self.isVerbose = True # auto-look on move

# Provides names and descriptions for rooms and places them into a dictionary
    def setup(self):
        """ setup(): create a graph of rooms for play. """
        # just a test -- needs work
        bedroom = Room( "Bedroom", 
                   "This is an average bedroom.",
                     { "north": "Bathroom",
                     "south": "Living Room",
                     "west" : "Kitchen",
                     "east" : "Front Porch"} )
            
        
        livingRoom = Room ( "Living Room",
                           "A TV, sofa, and game console are here.",
                           { "north" : "Bedroom" } )
        
        bathroom = Room ( "Bathroom", 
                         "There are wet towels hanging.",
                         { "south" : "Bedroom" } )
        
        kitchen = Room ( "Kitchen", 
                         "Although clean, there is a faint smell of burnt toast.",
                         { "east" : "Bedroom" } )

        porch = Room  ("Front Porch",
                            "You look towards the driveway. You hear birds chirping in the distance.",
                            { "west" : "Bedroom" })

# Place rooms in a dictionary.
        self.rooms = { bedroom.name: bedroom, 
                    livingRoom.name: livingRoom,
                    bathroom.name: bathroom,
                    kitchen.name: kitchen,
                    porch.name: porch}
        
        print(self.rooms)
        self.here = bedroom # starting location

# Loops program until user decides to quit    
    def loop(self):
        """ loop(): the main game loop.
        Continues until the user quits. """
        self.isPlaying = True
        while self.isPlaying:
            self.playerAction()
        print("Game over, thanks for playing")

# Drives commands to navigate through room objects
    def playerAction(self):
        """ Ask user for input, validate it, update the game state. """
        command = input(">")
        command = command.lower()
        words = command.split() # split on whitespace
        if len(words) < 1:
            print("No input detected")
            return
# Provides effectiveness for travel by slicing the verb go and the direction       
        verb = words[0]
        if verb == "go":
            direction = words[1]
            # Can we go in the chosen direction from here?
            if self.here.exits.get(direction) == None:
                print("You can't go that way.")
            else:   
                # this key does exist
                newRoomName = self.here.exits[direction]
                newRoom     = self.rooms[newRoomName]
                self.here   = newRoom
                if self.isVerbose:
                    self.here.describe()

# Allows the user to view the room they are in and view options for travel
        elif verb == "look":
            self.here.look()
# The program will end when the user types "quit"
        # elif verb == "get":
        #     self.getItem()
            
        
        elif verb == "quit":
            self.isPlaying = False
            print("quitting")
        
        else: # first word is verb
            print("I don't know how to", words[0])

# Organizes program functions 
def main():
    game = Game()
    game.setup()
    game.loop()
    game.end()

if __name__ == "__main__":
    main()