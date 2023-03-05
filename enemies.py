import random
from items import *
enemy_horse = {"name": "horse", "hp": 100, "damage": random.randint(5, 20), "item": item_hay}
enemy_pig = {"name": "pig", "hp": 100, "damage": random.randint(5, 20),"item": item_carrot }
enemy_dog = {"name": "dog", "hp": 100, "damage": random.randint(5, 20), "item": item_bone}

enemies = [enemy_horse, enemy_pig, enemy_dog]
