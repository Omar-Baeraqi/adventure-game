import time
import random


def print_pause(string):
    print(string)
    time.sleep(2)


def valid_input(message, option1, option2):
    while True:
        response = input(message)
        if option1 == response:
            break
        elif option2 == response:
            break
        else:
            print_pause("Try again.")
    return response


def intro(enemy):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.")


def field(items, enemy, weapon):
    print_pause("")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    response = valid_input(
            "What would you like to do?\n(Please enter 1 or 2.)\n", "1", "2")
    if response == "1":
        house(items, enemy, weapon)
    elif response == "2":
        cave(items, enemy, weapon)


def cave(items, enemy, weapon):
    print_pause("You peer cautiously into the cave.")
    if weapon in items:
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        field(items, enemy, weapon)
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause(f"You have found the magical {weapon} of Ogoroth!")
        print_pause("You discard your silly old dagger and "
                    f"take the {weapon} with you.")
        items.remove("dagger")
        items.append(weapon)
        print_pause("You walk back out to the field.")
        field(items, enemy, weapon)


def house(items, enemy, weapon):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and "
                f"out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")
    if "dagger" in items:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
    response = valid_input(
                    "Would you like to (1) fight or (2) run away?\n", "1", "2")
    if response == "1":
        fight(items, enemy, weapon)
        play_again()
    elif response == "2":
        print_pause("You run back into the field. Luckily, "
                    "you don't seem to have been followed.")
        field(items, enemy, weapon)


def fight(items, enemy, weapon):
    if weapon in items:
        print_pause(f"As the {enemy} moves to attack, "
                    f"you unsheath your new {weapon}.")
        print_pause(f"The {weapon} of Ogoroth shines brightly in your hand "
                    "as you brace yourself for the attack.")
        print_pause(f"But the {enemy} take one look at your shiny new toy and "
                    "runs away!")
        print_pause(f"You have rid the town of the {enemy}. "
                    "You are victorious!")
    else:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {enemy}.")
        print_pause("You have been defeated!")


def play_again():
    response = valid_input(
                "GAME OVER\nWould you like to play again? (y/n)\n", "y", "n")
    if response == "y":
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif response == "n":
        print_pause("Thanks for playing! See you next time.")


def play_game():
    items = ["dagger"]
    enemy = random.choice(["dragon", "wicked fairie", "pirate", "troll"])
    weapon = random.choice(["Sword", "Axe"])
    intro(enemy)
    field(items, enemy, weapon)


play_game()
