'''
Workshop 4
Jon M Honhart
'''

class User:
    '''    User class    '''

    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        '''change name'''
        if len(name) >= 2 and len(name) <= 10:  # Bonus Task 3 
            self.name = name 
        else: 
            print('Invalid username') 

    def change_pin(self, pin):
        '''change pin'''
        if len(str(pin)) == 4 and isinstance(pin, int):  # Bonus Task 3 
            self.pin = pin 
        else: 
            print('Invalid PIN') 

    def change_password(self, password):
        '''change password'''
        if len(password) >= 5: 
            self.password = password  # Bonus Task 3 
        else: 
            print('Invalid password') 


class BankUser(User):
    '''BankUser subclass '''

    def __init__(self, name, pin, password):
        # def __init__(self, name, pin, password): 
        super().__init__(name, pin, password)
        self.balance = float(0)

    def show_balance(self):
        '''Show balance'''
        print(f'{self.name} has a balance of: ${self.balance:.2f}')

    def withdraw(self, withdraw_amount):
        '''withdraw'''
        # Bonus Task 1 && 2 
        try: 
            if self.balance >= withdraw_amount and self.balance > 0: 
                self.balance -= float(withdraw_amount) 
            else: 
                print('Insufficient funds, withdrawal canceled.') 
        except TypeError: 
            print('Invalid withdraw') 

    def deposit(self, deposit_amount):
        '''deposit'''
        # Bonus Task 1 && 2 
        try: 
            if deposit_amount > 0 and float or deposit_amount > 0 and int: 
                self.balance += float(deposit_amount) 
            else: 
                print('Insufficient deposit, deposit canceled.') 
        except TypeError: 
            print('Invalid deposit') 

    def transfer_money(self, requestor, transfer_amount):
        '''transfer money'''
        print(f'\n{self.name} are transferring ${transfer_amount} to {requestor.name}\nAuthentication required')
        transfer_pin = int(input('Enter your PIN: '))
        if transfer_pin == self.pin:
            # new balance after successful transfer 
            self.balance -= transfer_amount
            requestor.balance += transfer_amount 
            print(f'Transfering ${transfer_amount} to {requestor.name}')
            return True
        print('Invalid PIN.  Transaction canceled.')
        return False

    def request_money(self, transferor, requestee_amount):
        '''request money'''
        print(f'\n{self.name} are requesting ${requestee_amount} from {transferor.name}\nUser authentication is required...')
        transferor_pin = int(input(f'Enter {transferor.name}\'s PIN: '))

        if transferor_pin == transferor.pin:
            requestee_passord = input('Enter your password: ')
            if requestee_passord == self.password:
                self.balance += requestee_amount
                transferor.balance -= requestee_amount
                print(f'Request authorized\n{transferor.name} sent ${requestee_amount}')
                return True
            print('Invalid password. Transaction canceled.')
            return False
        print('Invalid PIN. Transaction canceled.')
        return False


# """ Driver Code for Task 1 """
# user1 = User('Bob', 1234, 'password')
# user2 = User('Jon', 1234, 'password')
# print(dir(user1))
# print(help(user2))
# print(user1.name, user1.pin, user1.password)
# print(user2.name, user2.pin, user2.password)

# """ Driver Code for Task 2 """
# user1.change_name('Bobby')
# user2.change_name('JonHon')
# user1.change_pin(4321)
# user2.change_pin(4321)
# user1.change_password('newpass')
# user2.change_password('newpass')
# print(dir(user1))
# print(help(user2))
# print(user1.name, user1.pin, user1.password)
# print(user2.name, user2.pin, user2.password)

# """ Driver Code for Task 3"""
# user1 = BankUser('Bob', 1234, 'password')
# user2 = BankUser('Jon', 1234, 'password')
# print(user1)
# print(user2)
# print(user1.name, user1.pin, user1.password, user1.balance)
# print(user2.name, user2.pin, user2.password, user2.balance)

# """ Driver Code for Task 4"""
# user1 = BankUser('Bob', 1234, 'password')
# user2 = BankUser('Jon', 1234, 'password')
# print(user1)
# print(user2)
# print(user1.name, user1.pin, user1.password, user1.balance)
# print(user2.name, user2.pin, user2.password, user2.balance)
# user1.deposit(1000)
# user2.deposit(2000)
# user1.show_balance()
# user2.show_balance()
# user1.deposit(3000)
# user2.deposit(4000)
# user1.show_balance()
# user2.show_balance()
# user1.withdraw(2500)
# user2.withdraw(1500)
# user1.show_balance()
# user2.show_balance()

# """ Driver Code for Task 5"""
# bob = BankUser('Bob', 1234, 'password')
# jonhon = BankUser('JonHon', 1234, 'password')
# alice = BankUser('Alice', 5678, 'password')
# ian = BankUser('Ian', 1234, 'password')
# lin = BankUser('Lin', 1234, 'password')

# jonhon.deposit(10000)
# ian.deposit(20000)
# lin.deposit(30000)
# jonhon.show_balance()
# ian.show_balance()
# lin.show_balance()

# alice.deposit(4000)
# alice.show_balance()
# bob.show_balance()

# alice.transfer_money(500, bob)
# alice.show_balance()
# bob.show_balance()

# alice.request_money(250, bob)
# alice.show_balance()
# bob.show_balance()

# # # Driver Code for Task One
# # # Output: Bob 1234 password

# user1 = User("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password)

# # # Driver Code for Task Two
# # # Output: Bob 1234 password
# # # Output: Bobby 4321 newpassword

# user1 = User("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password)
# user1.change_name("Bobby")
# user1.change_pin(4321)
# user1.change_password("newpassword")
# print(user1.name, user1.pin, user1.password)


# # # Driver Code for Task Three
# # # Output: Bob 1234 password 0

# bankuser1 = BankUser("Bob", 1234, "password")
# print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)


# # # Driver Code for Task Four
# # # Output:
# # #   Alice has an account balance of: 0
# # #   Alice has an account balance of: 1000.0
# # #   Alice has an account balance of: 500.0

# bankuser1 = BankUser("Alice", 1234, "password")
# bankuser1.show_balance()
# bankuser1.deposit(1000.0)
# bankuser1.show_balance()
# bankuser1.withdraw(500.0)
# bankuser1.show_balance()


# # # Driver Code for Task Five
# # # Output:
# # #   Alice has an account balance of: 5000
# # #   Bob has an account balance of: 0

# # #   You are transferring $500 to Bob
# # #   Authentication required
# # #   Enter your PIN: 5678
# # #   Transfer authorized
# # #   Transferring $500 to Bob
# # #   Alice has an account balance of: 4500
# # #   Bob has an account balance of: 500

# # #   You are requesting $250 from Bob
# # #   User authentication is required...
# # #   Enter Bob's PIN: 1234
# # #   Enter your password: alicepassword
# # #   Request authorized
# # #   Bob sent $250
# # #   Alice has an account balance of: 4750
# # #   Bob has an account balance of: 250

bankuser1 = BankUser("Bob", 1234, "password")
bankuser2 = BankUser("Alice", 5678, "alicepassword")
bankuser3 = BankUser('JonHon', 1234, 'password')
bankuser4 = BankUser('Ian', 1234, 'password')
bankuser5 = BankUser('Lin', 1234, 'password')
bankuser2.deposit(5000)
bankuser3.deposit(5000)
bankuser4.deposit(5000)
bankuser5.deposit(5000)
bankuser5.show_balance()
bankuser4.show_balance()
bankuser3.show_balance()
bankuser2.show_balance()
bankuser1.show_balance()
print()

TRANSFERED = bankuser2.transfer_money(bankuser1, 500)
TRANSFERED = bankuser3.transfer_money(bankuser1, 500)
TRANSFERED = bankuser4.transfer_money(bankuser1, 500)
TRANSFERED = bankuser5.transfer_money(bankuser1, 500)
bankuser5.show_balance()
bankuser4.show_balance()
bankuser3.show_balance()
bankuser2.show_balance()
bankuser1.show_balance()
print()

if TRANSFERED:
    bankuser2.request_money(bankuser1, 250)
    bankuser2.show_balance()
    bankuser1.show_balance()
print()

bankuser5.show_balance()
bankuser4.show_balance()
bankuser3.show_balance()
bankuser2.show_balance()
bankuser1.show_balance()
print()