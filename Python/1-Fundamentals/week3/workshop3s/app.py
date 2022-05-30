'''
Workshop 3 framework v1.1
By Jack Seymour 
Modified by Jon Honhart
'''
from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

# Global (Application) variable definitions
# define the initial state of the database
database = {
    "admin": "password123"
}
# define the initial state of the list of donations
donations = []
# define the initial state of the variable (authorized user)
authorized_user = ""

# Main application loop
while True:
    show_homepage(authorized_user)  # Show homepage

    # Get user action then process user input
    choice = input("Choose an option: ")
    print("")
    if choice == "1":  # login
        username = input("Enter user name: ").lower()
        password = input("Enter user password: ")
        print("")
        authorized_user = login(database, username, password)

    elif choice == "2":  # register
        username = input("Enter user name: ").lower()
        password = input("Enter user password: ")
        print("")
        authorized_user = register(database, username, password)
        if authorized_user != "":
            database[username] = password

    elif choice == "3":  # donate
        if authorized_user == "":
            print("You are not logged in.\n")
        else:
            donation = donate(authorized_user)
            donations.append(donation)

    elif choice == "4":  # show
        show_donations(donations)

    elif choice == "5":  # exit
        print("Leaving DonateMe...\n")
        quit()

    else:
        print("Invalid: Choose from 1-5\n")
