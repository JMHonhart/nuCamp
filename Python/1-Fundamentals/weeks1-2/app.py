'''
Jon M Honhart
'''
from pdb import Restart
from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

name = input("Enter name to register: ")
if not name.isalpha() or len(name) > 10:
    print("No blank, numbers and maximum length is 10 characters")
    quit()
pin = input("Enter PIN: ")
if not pin.isdigit() or len(pin) != 4:
    print("PIN must contain only 4 numbers")
    quit()
balance = 0

print(f"{name} has been registered with a starting balance of ${balance}")
print("")

# First while loop
while True:
    print("          === Automated Teller Machine ===")
    print("LOGIN") 
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")

    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful! ")
        break
    else:
        print("Invalid credentials!")
        print("")
        continue

# Second while loop
while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option.lower() == "1" or option.lower() == "balance":
        account.show_balance(balance)
    elif option.lower() == "2" or option.lower() == "deposit":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option.lower() == "3" or option.lower() == "withdrawl":
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option.lower() == "4" or option.lower() == "logout":
        account.logout(name)
    else:
        print("Unknown Option try again")