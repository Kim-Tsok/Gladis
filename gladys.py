import random
import traceback

def main():
    from combat import fight
    from weapons import weapons
    from armour import armour
    from enemies import enemies

    player = {
        "health": 100,
        "mystery_stat": random.randint(5, 9),
        "gender": "Sir",
        "status": None
    }

    input("Press Enter to start the game...")
    print(" ")

    input("Unknown: What is your motivation for all of this, why do you do this? ")
    input("Make it easier on yourself, just give up. ")
    input("Give up on this stupid dream of trying to beat me. ")
    input("")
    input("person01: Hey wake up! wakeup you idiot. ")
    input("You: What happened? ")
    input("person01: You were shaking and mumbling something in your sleep. ")
    input("You: I had a dream. ")
    input("person01: You saw him again, didn't you? ")
    input("You: It was terrifying. ")

    choice = input(
        "person01: Wanna spar cause we're weirdos? (y/n) "
    ).lower()

    weapon = weapons["excalibur"].copy()

    fight(player, weapon, armour, enemies["goblin"])

    input("You have defeated the goblin! Now you must face the ogre! ")
    fight(player, weapon, armour, enemies["ogre"])


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        input("\nGame crashed. Press Enter to exit...")
