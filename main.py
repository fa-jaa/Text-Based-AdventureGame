
from time import sleep #module to put pauses between statements
import sys,time
from player import *
from Room_Definitions import rooms
from items import *
from game_parser import normalise_input
from Music import music_player

#function to print text slow
#takes string wanted to be printed and how fast you want it to be printed. (0.1 being the fastest going up being slower)
def print_simulate(str,x):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(x)
        
#pause function
def pause(x):
    sleep(x)
    
#Seperates text with empty spaces
def sep(x):
    sep = "\n"
    print(sep*x)
    
#Seperates lines with - can add number to extend line
def linesep(x):
    line = '-'
    print(line*x)
    
#Adds star key when horse is dead
def star_key():
    if enemy_horse["hp"] <= 0:
        room_stable["items"].append(item_starkey)   

    

#quits game
def Quit():
    quit()
     



def torch_ending():

    ans = False

    while ans == False:
        user_input = input("\n>")

        if normalise_input(user_input) == ["take","torch"] or normalise_input(user_input) == ["use","torch"]:
            ans = True
            sep(1)
            print("You have taken the torch")

            break

        else:
            print("Its dark you need a source of light")
            


#Function use torch looks to see if user has switched on torch
def use_torch():
    sep(1)
    print("What would you like to do with the torch?")
    ans = False
    while ans == False:
        user_input = input("\n>")
        
        if normalise_input(user_input) == ["on","torch"] or normalise_input(user_input) == ["torch","on"] or normalise_input(user_input) == ['use','torch'] :
            ans = True
            
            sep(1)
            print("You have switched the torch on")
            sep(1)
            break
        else:
            print("You can barely see anything from how dark it is")

            
#Torch scene, user has to take the torch to continue story           
def torch_scene1():
    from Room_Definitions import starting_items
    
    ans = False
    
    while ans == False:
        user_input = input("\n>")
        
        if normalise_input(user_input) == ["take","torch"] or normalise_input(user_input) == ["use","torch"]:
            ans = True
            inventory.append(item_torch)
            starting_items.remove(item_torch)
            sep(1)
            print_simulate("You have taken the torch",0.05)
            sep(1)
            break
        
        else:
            print("Its dark you need a source of light")
    
        
    

    
    
#knife scene plays once torch is found and swithced on. User must take knife before carrying on
def knife_scene1():
    from Room_Definitions import starting_items
    
    print_simulate("You took the torch and flicked the switch on.",0.05)
    sep(2)
    print_simulate("Pointing it around you come across your swiss army knife.",0.05)
    sep(1)
    
    ans = False
    
    while ans == False:
        user_input = input("\n>")
        if normalise_input(user_input) == ["take","knife"]:
            ans = True
            inventory.append(item_knife)
            starting_items.remove(item_knife)
            sep(1)
            print("You have taken the knife")
            break
        else:
            print("Its a long journey ahead, you migth find it useful")


  
def travel1():
    print_simulate("You have 2 options",0.05) 
    pause(1)
    sep(1)
    print_simulate("Stay with the debri of your once beautiful Mercedes Benz 300 SL",0.05) 
    pause(1)
    sep(1)
    print_simulate("Go towards barn to seek shelter from the storm",0.05)
    sep(1)

    ans =  False
    while ans == False:
        user_input = input("\n>")
        
        if normalise_input(user_input) == ["go"]:
            ans = True
            go_to_barn()  
            break
        elif normalise_input(user_input) == ["stay"]:
            ans = True
            stay_with_debri()
            break
        else:
            print_simulate("You can either go or stay choose wisley",0.05)
    
   
        

def go_to_barn():
    sep(1)
    print_simulate("As you advance towards the structure it comes apparent that behind the bare trees was an abandoned farm.",0.05)
    pause(1)
    sep(1)
    print_simulate("“Crunch” bushes a stone-throw away start rustling.",0.05)
    pause(1)
    sep(1)
    print_simulate("Jack?! Jack?! Is that you ?!",0.05)
    pause(1)
    sep(1)
    print_simulate("Filled with fear.",0.05)
    pause(1)
    sep(1)
    print_simulate("Carry on to the shelter or approach the bush",0.05)
    pause(1)
    sep(1)
    ans =  False
    while ans == False:
        user_input = input("\n>")
        if normalise_input(user_input) == ["go",'shelter'] or normalise_input(user_input) == ["carry",'on']:
            ans = True
            to_shelter()
            break
        elif normalise_input(user_input) == ["go","bush"] or normalise_input(user_input) == ["approach","bush"]:
            ans = True
            approach_bush()
            break
        else:
            print("You can either go to the shelter or go to the bush")
        
       
    


def to_shelter():
    sep(1)
    print_simulate("Trembling from the icy cold winds. You continue the walk to the farm.",0.05)
    pause(1)
    sep(1)
    print_simulate("While you near to the farm a light in one of the windows trickled. ",0.05)
    pause(1)
    sep(1)
    print_simulate("Advancing towards the small shaft with relief. You knock on the door with all your remaining strength. ",0.05)
    pause(1)
    sep(1)
    print_simulate("No one answers.",0.05)
    pause(1)
    sep(1)
    print_simulate("You turn around and . . . . . . .",0.05)
    pause(1)
    sep(1)
    scene2()
    
    

def approach_bush():
    print_simulate("You draw near to the overgrown bushes. ",0.05) 
    pause(1)
    sep(1)
    print_simulate("What would you like to do ? ",0.05)
    pause(1)
    sep(1)
    ans = False
    while ans == False:
        user_input = input("\n>")
        if normalise_input(user_input) == ["inspect",'bush'] or normalise_input(user_input) == ["look",'bush']:
            print_simulate("You take a closer look and in the corner of your eye Jack's necklace hangs.",0.05)
            pause(1)
            sep(1)
            print_simulate(" Your heart is frozen. Trembling with fear you try to take the necklace from the bush but it's tangled.",0.05)
            pause(1)
            sep(1)
            print_simulate("You get down on your knees. Getting slammed by rain you try to untangle the necklace. ",0.05)
            pause(1)
            sep(1)
            print_simulate("Disguised by the rain you hear footsteps behind you. . . . . . . . .",0.05)
            pause(1)
            sep(1)
            print_simulate("Turn around or Run into the forest",0.05)
            user_input = input("\n>")
            if normalise_input(user_input) == ["turn",'around'] or normalise_input(user_input) == ["turn"]:
                ans = True
                turn_around()
                break
            elif normalise_input(user_input) == ["run",'forest'] or normalise_input(user_input) == ["run"]:
                ans = True
                run_to_forest()
                break
            else:
                print("Turn or Run")
        else:
            print("A silver item catches your attention would you like to inspect the bush?")
        

            
            
def turn_around():
    print_simulate("As you turn around..............",0.1)
    pause(1)
    sep(1)
    print_simulate("“BANG”")
    sep(1)
    scene2()

def run_to_forest():
    print_simulate("You run into the forest trembling with fear.",0.05)
    pause(1)
    sep(1)
    print_simulate("You run with all your remaining energy.",0.05)
    pause(1)
    sep(1)
    print_simulate("Starving you become famished.",0.05)
    pause(1)
    sep(1)
    print_simulate("Searching for food a chicken hung to a rope stares at you",0.05) 
    pause(1)
    sep(1)
    print_simulate("You reach for the food and fall into an animal trap.",0.05)
    sep(1)
    scene2()

            
def stay_with_debri():
    global health
    print_simulate("It began as a whisper in the air,",0.05)
    pause(1)
    sep(1)
    print_simulate("but transformed into silver icicles fizzing from the sky. Accompanied by strong gusts of wind, parts of debri hurl towards you",0.05)
    pause(1)
    sep(1)
    print_simulate("and pierce your skin. After a bit you decided to move towards the barn as you could not weather the storm. ",0.05)
    pause(1)
    sep(1)
    loss_health = random.randint(1,20)
    health -=  loss_health
    print_simulate("You have lost {}hp. Your remaining health is {}hp".format(loss_health,health),0.05)
    pause(1)
    sep(1)
    approach_bush()
    
    

#Scene 1 
def scene1():
    
    print_simulate("\nDarkness.",0.1)
    pause(2)
    sep(1)
    print_simulate("\nIt surrounds you.",0.05)
    pause(2)
    sep(1)
    print_simulate("\nYou ask yourself where am I ?  ",0.05)
    pause(1)
    sep(1)
    print_simulate("\n\nYou look left, but Jack is not there",0.05)
    pause(1)
    sep(1)
    print_simulate("\nSurrounded by nothing but a field of debri.",0.05)
    pause(1)
    sep(1)
    print_simulate("\nYour heart starts slamming against your ribs.",0.1)
    pause(1)
    sep(1)
    print_simulate("\nYou look right and find a torch ",0.1)
    sep(1)
    pause(1)
    torch_scene1()
    use_torch()
    pause(2)
    knife_scene1()
    sep(1)
    print_simulate("The sky is tar black. Huge clouds approach your location.",0.05)
    sep(1)
    print_simulate("The clusters of plants can hardly be seen because of how dark it is. You rally all your confidence and move forth. ",0.05)
    sep(1)
    print_simulate("In the distance hidden behind the towering figures was an old structure of sorts. ",0.05)
    travel1()
    

    
    
   
    
def scene2():
    print_simulate("Your vision blurred. You try to move but are constrained by rope.",0.05)
    pause(1)
    sep(1)
    print_simulate("The smell of hay mixed with animal dung is pregnant in the air.",0.05)
    pause(1)
    sep(1)
    print_simulate("You look around and see your wallet, knife, torch and notepad placed\non a table a meter away from you.",0.05)
    pause(1)
    sep(1)
    print_simulate("Scooting forward you manage to reach the table.",0.05)
    pause(1)
    sep(1)
    print_simulate("You grab the knife with your teeth and drop it to your hand.\nYou then cut yourself free.",0.05)
    sep(1)
    pause(3)
                   









game_instructions = {
         
          "take" : "will add item to inventory",
         
          "drop" : "Will remove item from inventory",
         
          "go" : "Will allow you to explore the map",
         
        "map" : "Will display a 2d map",
         
          "tame" : "Will give item to desired animal/person etc",
         
         "attack" : "Will deal damage to enemy",
         
         "inspect" : "Will examine item",
         
         "help" : "Will display game instructions and may display a hint"

         
 }


def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
     returns a comma-separated list of item names (as a string). For example:
"""
    item_list = []
    for item in range(0,len(items)):
        item_list.append(items[item]['name'])
        
    return ", ".join(item_list)
    
    pass


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:
    """
    if len(room["items"]) > 0:
        print("There is",list_of_items(room["items"]),'here.')
        print()
    else:
        pass
    

def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example
    """
    if len(inventory) > 0:
        print("You have",list_of_items(items)+'.')
        print()
    else:
        print("You have 0 items in inventory")
        print()


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:
    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    print_room_items(room)
    

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    print("You can:")
    sep(1)
    
    
    for item in inv_items:
        if item == item_toolbox:
            print("Open TOOLBOX, to open the toolbox.")
            
            
    # Iterate over available exits
    linesep(50)
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
        
    linesep(50)
    
    for item in room_items:
        print("TAKE",item["id"].upper(), "to take",item["name"]+'.')
        
    linesep(50)
    
    for item in inv_items:
        if item in foods:
            print("Eat",item["id"].upper(), "to eat",item["name"]+'.')
    
    
        
    linesep(50)
    
    
    for item in inv_items:
        print("Drop",item["id"].upper(), "to drop",item["name"]+'.')

    linesep(50)
    
    
    for enemy in enemies:
        if enemy in current_room["enemies"] and enemy in enemies:
            print("Attack", enemy["name"].upper(),"to attack", enemy["name"]+'.' )
        
    linesep(50)
    
    
    
    

    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:
    """
    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    
    global current_room
    
    if is_valid_exit(current_room["exits"],direction):
        new_room = move(current_room['exits'],direction)
        current_room = new_room
    else:
        print("You cannot go there.")

    
    
def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    
    


    item_in_room = False
    for item in current_room['items']:
        if item['id'] == item_id:
            inventory.append(item)
            
            current_room['items'].remove(item)
            
            item_in_room = True
    if item_in_room == False:
        print("You cannot take that.")
    

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    item_in_inventory = False
    for item in inventory:
        if item_id == item['id']:
            item_in_inventory = True
            inventory.remove(item)
            current_room['items'].append(item)
    if item_in_inventory == False:
        print("You cannot drop that.")
    

def execute_help(game_instructions):
    sep(4)
    for instruction in game_instructions:
        print(instruction,' - ', game_instructions[instruction])
        sep(1)
    pause(3)
        
        
def execute_eat(item_id):
    from attack import eat 
    edible = False 
    for item in foods:
        if item_id == item['id']:
            eat(item)
            edible = True
            if item_id == item_meat['id']:
                current_room['items'].append(item_moonkey)
    if edible == False:
        print("You cannot eat this item")


def execute_attack(enemy_id):
    from enemies import enemies
    from attack import attack
    valid_attack = False
    for enemy in current_room["enemies"]:
        if enemy_id == enemy["name"] and enemy['hp'] > 0:
            attack(enemy, enemy["hp"], enemy["damage"], item_axe)
            valid_attack = True
        elif enemy_id == enemy["name"] and enemy['hp'] <= 0:
            print("Enemy has been defeated")
            star_key()
            valid_attack = False
    if valid_attack == False:
        print("Why are you attacking?")
        enemies.remove(enemy)

        
def execute_sunkey():
    room_corridor1["items"].append(item_sunkey)        
    inventory.remove(item_toolbox)
        

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    from mapforgame import map
    
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
   
    elif command[0] == "help":
        execute_help(game_instructions)
        
    elif command[0] == "eat":
        if len(command) > 1:
            execute_eat(command[1])

    elif command[0] == "attack":
        if len(command) > 1:
            execute_attack(command[1])
        else:
            print("Attack what?")

    elif command[0] == "map":
         sep(1)
         print(map)
         sep(1)
    
    elif command[0] == "open":
        if len(command) > 1:
            execute_sunkey()
            
    elif command[0] == "quit":
        Quit()
    
    
    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:
    """

    # Next room to go to
    return rooms[exits[direction]]






        
#3 function that is called prints game instructions and starts the game
def intro_text(game_instructions):
    sep(1)
    print_simulate("To play the game, type short phrases into the command line below.",0.05)
    sep(1)
    print_simulate("Here is a list of the key words you will need to use",0.05)
    sep(1)
    linesep(100)
    #prints game instruction
    for instruction in game_instructions:
        print(instruction,' - ', game_instructions[instruction])
        sep(1)
    print("Type help if you get stuck.")
    sep(1)
    pause(2)
    print_simulate("Type START to begin",0.05)
    sep(1)

   
    game_over = False
    while game_over == False:
        user_input = input("\n> ")
        normalised_user_input = normalise_input(user_input)
        if normalised_user_input == ["start"]:
            scene1()
            break
            
        else:
            print("Please type start . . . . . .")
            

#2nd function that is run, calls intro text to print instructions
def intro():
    keypressed = False
    print_simulate("""
                   
                   
                   
                                                                                                                                                                                                    
                                @@@        @@@@@@    @@@@@@   @@@@@@@     @@@  @@@  @@@     @@@@@@@    @@@@@@   @@@@@@@   @@@  @@@  @@@  @@@  @@@@@@@@   @@@@@@    @@@@@@   
                                @@@       @@@@@@@@  @@@@@@@   @@@@@@@     @@@  @@@@ @@@     @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@ @@@  @@@@@@@@  @@@@@@@   @@@@@@@   
                                @@!       @@!  @@@  !@@         @@!       @@!  @@!@!@@@     @@!  @@@  @@!  @@@  @@!  @@@  @@!  !@@  @@!@!@@@  @@!       !@@       !@@       
                                !@!       !@!  @!@  !@!         !@!       !@!  !@!!@!@!     !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!!  !@!!@!@!  !@!       !@!       !@!       
                                @!!       @!@  !@!  !!@@!!      @!!       !!@  @!@ !!@!     @!@  !@!  @!@!@!@!  @!@!!@!   @!@@!@!   @!@ !!@!  @!!!:!    !!@@!!    !!@@!!    
                                !!!       !@!  !!!   !!@!!!     !!!       !!!  !@!  !!!     !@!  !!!  !!!@!!!!  !!@!@!    !!@!!!    !@!  !!!  !!!!!:     !!@!!!    !!@!!!   
                                !!:       !!:  !!!       !:!    !!:       !!:  !!:  !!!     !!:  !!!  !!:  !!!  !!: :!!   !!: :!!   !!:  !!!  !!:            !:!       !:!  
                                :!:      :!:  !:!      !:!     :!:       :!:  :!:  !:!     :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  :!:           !:!       !:!   
                                :: ::::  ::::: ::  :::: ::      ::        ::   ::   ::      :::: ::  ::   :::  ::   :::   ::  :::   ::   ::   :: ::::  :::: ::   :::: ::   
                                : :: : :   : :  :   :: : :       :        :    ::    :      :: :  :    :   : :   :   : :   :   :::  ::    :   : :: ::   :: : :    :: : :
                                                
                            
                            
                            """,0.0015)

    sep(1)
    print("Press ENTER key to begin . . . . . . . .")
    sep(1)
    anykey = input("")
    keypressed = True 
    if keypressed == True:
        intro_text(game_instructions)
        
def key_check():
    from items import keys 
    all_keys = []
    for item in keys:
     if item in room_door["items"]:
        all_keys.append(item)
    if len(all_keys) == 3:
        endscene() 
        
              
def endscene():
    pause(1)
    sep(1)
    print_simulate("\nAs you place the three keys in sequence, the ground shakes and they begin to fuse together.",0.05)
    pause(1)
    sep(1)
    print_simulate("\nThe door labelled 'Exit' slowly creeps open and bright light shines through the slowly increasing opening. ",0.05)
    pause(1)
    sep(1)
    print_simulate("\nYour hesitation to enter is suddenly removed as the faint sound of footsteps becomes louder.",0.05)
    pause(2)
    sep(1)
    print_simulate("\nYou enter.",0.1)
    pause(2)
    sep(1)
    print_simulate("\nDarkness.",0.5)
    pause(2)
    sep(1)
    print_simulate("\nIt surrounds you.",0.2)
    pause(2)
    sep(1)
    print_simulate("\nDeja vu hits you as you begin to look around. ",0.1)
    pause(2)
    sep(1)
    print_simulate("\nSurrounded by nothing but a field of debri.",0.1)
    pause(1)
    sep(1)
    print_simulate("\nYou ask yourself where am I ?",0.1)
    pause(1)
    sep(1)
    print_simulate("\nYou look left, but Jack is not there. . . . . . .",0.1)
    pause(1)
    sep(1)
    print_simulate("\nYour heart starts slamming against your ribs.",0.1)
    pause(1)
    sep(1)
    print_simulate("\nYou look right and find a torch ",0.1)
    pause(2)
    sep(1)
    torch_ending()
    use_torch()
    pause(2)
    sep(1)
    print_simulate("\nPointing it around you can see two figures in the distance",0.1)
    pause(2)
    sep(1)
    print_simulate("\nYou approach the figures, surrounded by bushes. ", 0.1)
    pause(2)
    sep(1)
    print_simulate("\nWhere you notice.... ", 0.1)
    pause(2)
    sep(1)
    print_simulate("\n...A familiar.", 0.5)
    pause(3)
    sep(1)
    print_simulate("face",1)
    credits()
    Quit() 
    
def credits():
    print_simulate("Brought to you by",0.05)
    sep(3)
    print_simulate("Zak Esposito",0.05)
    print_simulate("Faisal Al-jaaidi",0.05)
    print_simulate("Ebrahim Al-aghbari",0.05)
    print_simulate("Semih Sarisoy",0.05)
    print_simulate("Abdullah Alnajfan",0.05)
    print_simulate("Shreya Garg",0.05)
    sep(1)
    print_simulate("Vishnu",0.05)
    
# This is the entry point of our program
def main():

   # from map import room_reception
    music_player()
    intro()
    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)

        key_check()



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()










        
        
    












        
        
    
