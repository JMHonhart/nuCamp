import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    random.shuffle(diamonds)
    option = input("Press enter to pick a card, or Q then enter to quit: ")
    if option.lower() == "q":
        quit()
    else:
        hand.insert(0, diamonds.pop())
        print(f"Your hand: {hand}")
        print(f"Remaing cards: {diamonds}")

if not diamonds:
    print("There are no more cards to pick.")