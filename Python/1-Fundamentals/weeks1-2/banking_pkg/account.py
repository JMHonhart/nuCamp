'''
Jon M Honhart
'''


def show_balance(balance):
    '''
    show balance function
    '''
    print(f"Current Balance: ${balance}")

def deposit(balance):
    '''
    deposit function
    '''
    print(f"$ {balance}")
    amount = input("Enter amount to deposit: ")
    return(float(balance) + float(amount))
 
def withdraw(balance):
    '''
    withdraw function
    '''
    print(f"$ {balance}")
    amount = input("Enter amount to withdraw: ")

    if int(amount) > int(balance):
        print("Whare are you going to get the kind of money?")
        return float(balance)
    else:
        return float(balance) - float(amount)

def logout(name):
    '''
    logout function
    '''
    print(f"Goodbye {name}!")
    quit()
