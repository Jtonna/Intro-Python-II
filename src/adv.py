import os
from player import Player
from room import Room


# Declare all the rooms
room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),
    'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#


# Make a new player object that is currently in the 'outside' room.
player = Player(room = room['outside'], name = str(os.getlogin()))

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).

# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print (f"Hello {str(os.getlogin())}, welcome back! \nLooks like youve started your journy in the {player.room}:")


input_key = input("[N] North, [E] East, [S] South, [W] West. || [Q] to quit the game!:").upper()


while not input_key == "Q":
    
    #Re-usable class because im lazy af
    class users_room:
        print(f"You have moved towards the {player.room}")

    # Moves the user to the north room
    if input_key == "N" and hasattr(player.room, "n_to"):
        player.room = player.room.n_to
        users_room()

    # Moves the user to the east room
    elif input_key == "E" and hasattr(player.room, "n_to"):
        player.room = player.room.n_to
        users_room()

    # Moves the user to the south
    elif input_key == "S" and hasattr(player.room, "n_to"):
        player.room = player.room.s_to
        users_room()

    # Moves the user to the west room
    elif input_key == "W" and hasattr(player.room, "n_to"):
        player.room = player.room.w_to
        users_room()

    # If the input_key isnt anything defined above do this
    else:
        print(f"Sorry {player.name}, you cant move that way. Its too dangerous right now. Try something else.")

    input_key = input("[N] North, [E] East, [S] South, [W] West. || [Q] to quit the game! :").upper()
