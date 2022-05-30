import random

high_score = 0


def dice_game():
    global die1
    global die2
    global total
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = sum([die1, die2])


dice_game()

while True:
    print(f"Current High Score: {high_score}")
    print("1) Roll Dice")
    print("2) Leave Game")
    option = input("Enter your choice: ")
    if option == "1" or option.lower() == "Roll Dice":
        dice_game()
        print(f"You rolled a... {die1}")
        print(f"You rolled a... {die2}\n")
        print(f"You have rolled a total of: {total}\n")
    if total > high_score:
        high_score = total
        print("New high score!\n")
    if option == "2" or option.lower() == "Leave Game":
        print("Goodbye!\n")
        quit()
