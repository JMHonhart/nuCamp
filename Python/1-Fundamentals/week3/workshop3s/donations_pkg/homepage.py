'''
Homepage functions
'''


def show_homepage(authorized_user):
    '''
    show_homepage
    '''
    print("      === DonateMe Homepage ===           ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.  Register         |")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.  Show Donations   |")
    print("------------------------------------------")
    print("|             5.  Exit                   |")
    print("------------------------------------------")
    if authorized_user == "":
        print("You must be logged in to donate.\n")
    else:
        print(f"Logged in as: {authorized_user.lower()}\n")


def format_currency(_value):
    '''
    format currency
    _value : int or float
    '''
    return "{:,.2f}".format(_value)

total = 0

def donate(username):
    '''
    donate
        # Donation action
    '''
    while True:
        donation_amt = input("Enter amount to donate: ")
        if donation_amt.isnumeric() == False or int(donation_amt) <= 0:
            print("Please enter a valid amount greater than zero.")
        else:
            donation = username + " donated $" + format_currency(float(donation_amt))
            print(f"Thank you {username} for your donation!\n")
            global total
            total += int(donation_amt)
            break
    return donation  # return string value

def show_donations(donations):
    '''
    show_definition
        # show donations view
    '''
    print("--------- All Donations ---------\n")
    if len(donations) == 0:
        print("Currently, there are no donations.\n")
    else:
        total = 0  # bonus
        for donation in donations:
            print(donation)
            donation = donation.replace(',', '')
            funds = donation.find('$') + 1
            total += float(donation[funds:])
        print("Total = $" + format_currency(total))
        print("")