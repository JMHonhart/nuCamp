'''
User functions
'''
def login(database, username, password):
    '''
    login
        # Login action
    '''
    if username in database:
        if password == database[username]:
            print(f"Welcome back {username}!\n")
            return username
        print(f"Incorrect password for {username}.\n")
        return ""
    else:
        print(f"{username} not found. Please register.\n")
        return ""

def register(database, username, password):
    '''
    register
        # Register user action
    '''
    if username in database:
        print(f"{username} already registered.\n")
        return ""  # return empty string

    if len(username) > 10 or username[0].isalpha() == False:
        print("Username must be 10 characters or less and must start with a letter.  Please try again.\n")
        return ""  # return empty string

    for letter in username:
        if letter.isalpha() == False and letter.isnumeric() == False:
            print(
                "Username must only contain alphanumeric characters.  Please try again.\n")
            return ""  # return empty string

    if len(password) < 5:
        print("Password must be at least 5 characters.  Please try again.\n")
        return ""

    else:
        database[username] = password
        print(f"Username {username} has been registered!\n")
        return username
