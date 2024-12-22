import random

dice_simu = {
    1: (
        " __________",
        "|          |",
        "|    1     |",
        "|     ●    |",
        "|          |",
        "|__________|",
    ),
    2: (
        " __________",
        "|          |",
        "|       ●  |",
        "|    2     |",
        "|  ●       |",
        "|__________|",
    ),
    3: (
        " __________",
        "|          |",
        "|   3  ●   |",
        "|    ●     |",
        "|  ●       |",
        "|__________|",
    ),
    4: (
        " __________",
        "|          |",
        "|  ●    ●  |",
        "|    4     |",
        "|  ●    ●  |",
        "|__________|",
    ),
    5: (
        " __________",
        "|          |",
        "|  ● 5  ●  |",
        "|    ●     |",
        "|  ●    ●  |",
        "|__________|",
    ),
    6: (
        " __________",
        "|          |",
        "|  ●    ●  |",
        "|  ●  6 ●  |",
        "|  ●    ●  |",
        "|__________|",
    ),
}


def roll():
    choice = input("Do you want to roll the dice? (y/n) : ")
    
    while choice.lower() == "y":
        guess = int(input("Guess the dice no. : "))
        dice1 = random.randint(1, 6)
        if guess == dice1:
            print("YOU GUESSED CORRECT!")
        else:
            print("YOU GUESSED WRONG!")
        print("dice rolled {} and you guessed {}".format(dice1,guess))
        print("\n".join(dice_simu[dice1]))

        choice = input("\nRoll again? (y/n): ")
print("Thanks for playing !")

roll()
