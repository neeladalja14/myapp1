import player as player

from classes.game import Person, bcolors

magic = [{"name": "fire", "cost": 10, "dmg": 60},
         {"name": "thunder", "cost": 10, "dmg": 80},
         {"name": "blizzard", "cost": 10, "dmg": 60},

]

players = Person(460, 65, 60, 34, magic)
