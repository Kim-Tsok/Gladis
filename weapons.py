import random

weapon = {
    "name": "Excalibur",
    "base_damage": 11,
    "total_damage": 0,
    "modifiers": {
        "goblin": 1.3,
        "ogre": 0.8
    },
    "flavor_lines": [
        "✨ Excalibur hums with ancient power",
        "⚔️ The blade gleams as it strikes"
    ]
}

def calculate_weapon(weapon):
    roll = random.randint(1, 6)
    weapon["total_damage"] = weapon["base_damage"] + roll
