enemies = {
    "knight01": {
        "name": "James",
        "health": 35,
        "attack": 10,
        "dialogue": [
            "- Okay, you're doing well!",
            "- I thought you were rusty but it seems like you still got it",
            "- Ohh nice",
             "You're cooking bruh"
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
