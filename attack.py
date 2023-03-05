from player import *
from Room_Definitions import *

def attack(enemy, enemy_health, enemy_damage, weapon):
    global health
    global stamina
    if enemy["hp"] > 0:
        if health > 0 and stamina > 0:
            choice = input("Do you want to attack say yes or no: ")
            if choice.lower() == "yes":
                stamina -= 10
                enemy.update({"hp": enemy_health - weapon["damage"]})
                print("You attacked the enemy and the enemy loses hp. Enemies hp is |{}|".format(enemy["hp"]))
                print("You lose stamina because of your attack. Stamina |{}|".format(stamina))
                experience_for_player()
                health -= enemy_damage
                print("The enemy attacks you back and you lose hp. Health |{}|".format(health))
            else:
                print("You chose not to attack.")

        else:
            print("You are dead.")
    


def eat(item):
    global health
    global stamina
    if item in foods:
        if item in inventory:
            inventory.remove(item)
            health = health + item["health"]
            stamina = stamina + item["stamina"]
            print("Stamina |{}|  Health |{}|".format(stamina, health))
        else:
            print("You do not have that item to eat.")
    else:
        print("That is not edible.")




def tame(enemy, item):
    if enemy["item"] in inventory:
        if enemy["item"] == item:
            enemy.update({"damage": 0})
            inventory.remove(enemy["item"])
            print("Enemy has eaten",enemy["item"]["id"])
            print("You have tamed", enemy["name"])
        else:
            print("That enemy cannot be tamed with item", item["id"])
    else:
        print("You do not have that item in inventory")



