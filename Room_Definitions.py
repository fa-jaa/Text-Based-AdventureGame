from items import *
from enemies import *


starting_items =  [item_knife, item_torch]


room_hay = {
    "name": "Hay room",

    "description":
    """The place where you started. When you woke up.""",

    "exits":  {"north": "Door room", "east": "Stable", "west": "Pig place", "south": "Dog house"},

    "items": [item_hay,item_pitchfork,item_carrot],

    "enemies": []
}

room_corridor4 = {
    "name": "Corridor 4",

    "description":
    """Just a basic corridor.""",

    "exits": {"north": "Stable", "west": "Dog house"},

    "items": [],
    
    "enemies": []
}

room_corridor3 = {
    "name": "Corridor 3",

    "description":
    """Just a basic corridor.""",

    "exits": {"north": "Pig place", "east": "Dog house"},

    "items": [],
    
    "enemies": []
}

room_corridor2 = {
    "name": "Corridor 2",

    "description":
    """Just a basic corridor.""",

    "exits": {"south": "Stable", "west": "Door room"},

    "items": [],
    
    "enemies": []
}

room_corridor1 = {
    "name": "Corridor 1",

    "description":
    """Just a basic corridor.""",

    "exits": {"south": "Pig place", "east": "Door room"},

    "items": [item_toolbox],
    
    "enemies": []
}

room_stable = {
    "name": "Stable",

    "description":
    """There are horses in the room, they look like ghosts and realize you are in the room.""",

    "exits": {"north": "Corridor 2", "west": "Hay room", "south": "Corridor 4"},

    "items":[item_apple,],

    "enemies": [enemy_horse]
}

room_doghouse = {
    "name": "Dog house",

    "description":
    """There are dogs in the room, they seem to not have eat anything for two days.""",

    "exits": {"north": "Hay room", "east": "Corridor 4", "west": "Corridor 3"},

    "items":[item_bone,item_meat],

    "enemies": [enemy_dog]
}

room_pigplace = {
    "name": "Pig place",

    "description":
    """There are pigs everywhere, they all look into your eyes in a creepy way.""",

    "exits": {"north": "Corridor 1", "south": "Corridor 3", "east": "Hay room"},

    "items":[item_carrot],

    "enemies": [enemy_pig]
}

room_door = {
    "name": "Door room",

    "description":
    """There is a big, seemingly locked door with an obscure locking mechanism. It appears to require 3 keys to unlock.""",

    "exits": {"east": "Corridor 2", "west": "Corridor 1", "south": "Hay room"},

    "items":[],
    
    "enemies": []
}

rooms = {
    "Hay room": room_hay,
    "Corridor 4": room_corridor4,
    "Corridor 3": room_corridor3,
    "Corridor 2": room_corridor2,
    "Corridor 1": room_corridor1,
    "Stable": room_stable,
    "Dog house": room_doghouse,
    "Pig place": room_pigplace,
    "Door room": room_door
}

