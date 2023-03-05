from Room_Definitions import *
experience = 0 #starts experience level at 0
inventory = []
equipment = item_axe
health = 100
current_room = rooms["Hay room"]
stamina = 100

def experience_for_player():
    global experience
    xp = random.randint(5,20)
    experience += xp
    print("Experience level |{}|".format(experience))



def health_check():
    global health 
    if health < 0:
        print("You are dead")
        


