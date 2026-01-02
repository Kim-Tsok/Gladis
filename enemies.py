enemies = {
    "goblin": {
        "name": "Goblin",
        "health": 35,
        "attack": 10,
        "dialogue": [
            "Grrk! Shiny knight!",
            "Hehehe… soft eyes 😈"
        ],
        "special_moves": [
            {
                "name": "Sand Toss",
                "chance": 0.3,
                "status": "stunned",
                "line": "The goblin throws sand in your eyes!"
            }
        ]
    },

    "ogre": {
        "name": "Ogre",
        "health": 70,
        "attack": 20,
        "dialogue": [
            "Ogre smash!",
            "Tiny knight scream funny!"
        ],
        "special_moves": [
            {
                "name": "Nut Crusher",
                "chance": 0.25,
                "bonus_damage": 8,
                "line": "The ogre punches you in the nuts 💀"
            }
        ]
    }
}
