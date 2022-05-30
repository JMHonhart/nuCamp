'''
Character | Hitpoints | Damage
--------- | --------- | ----------
Wizard | 70 | 150
Elf | 100 | 100
Human | 150 | 20
Orc | 250 | 75   
Dragon | 300 | 50
'''
wizard = "Wizard"
wizard_hp = 70
wizard_damage = 150

elf = "Elf"
elf_hp = 100
elf_damage = 100

human = "Human"
human_hp = 150
human_damage = 20

orc = "Orc"
orc_hp = 250
orc_damage = 75

dragon_hp = 300
dragon_damage = 50

while True:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    print("4) Orc")
    print("5) Exit")
    character = input("Choose your character: ")
    if character == "1" or character.lower() == "wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    if character == "2" or character.lower() == "elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if character == "3" or character.lower() == "human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    if character == "4" or character.lower() == "orc":
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage
        break
    if character == "5" or character.lower() == "exit":
        print("Goodbye!")
        quit()
    print("Unknown character")

print(f"You have chosen the character: {character}")
print("Health: " + str(my_hp))
print(f"Damage: {my_damage}")
print("")

while True:
    dragon_hp = dragon_hp - my_damage
    my_hp = my_hp - dragon_damage
    print(f"The {character} damaged the Dragon!")
    print(f"The Dragon's hitpoints are now: {dragon_hp}")
    print("")
    if dragon_hp <= 0:
        print(f"{character} Wins!! the Dragon has lost the battle")
        print("")
        break
    if my_hp <= 0:
        print(f"The {character} has lost the battle.")
        print("")
        break
    print(f"The Dragon strikes back at the {character}")
    print(f"The {character} hitpoints are now: {my_hp}")
    print("")

print("Play Again")
print("")