'''
Portfolio Project BlackJack
By Jon Honhart
'''
from random import shuffle

class Gameplay(object):
    '''Gameplay Class'''

    def __init__(self, player, funds=100):
        '''__init__'''
        self.dealer = Dealer()
        self.player = Player(player, funds)
        self.deck = Deck()
        self.table_setup()

    def table_setup(self):
        '''Table Setup'''
        self.deck.shuffle()
        self.player.place_bet()
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.deal_card(self.player)
        self.calculate_score(self.player)
        self.calculate_score(self.dealer)
        self.main()

    def main(self):
        '''Main'''
        while True:
            print()
            print(self)
            player_move = hit_me()
            if player_move is True:
                self.deal_card(self.player)
                self.calculate_score(self.player)
            elif player_move is False:
                self.dealer_hit()

    def dealer_hit(self):
        '''Dealer Hit'''
        score = self.dealer.score
        while True:
            if score < 17:
                self.deal_card(self.dealer)
                self.calculate_score(self.dealer)
                print(self)
            elif score >= 17:
                self.check_final_score()

    def __str__(self):
        '''Menu'''
        dealer_hand = [card for card, value in self.dealer.hand]
        player_hand = [card for card, value in self.player.hand]

        print("Dealer hand : {}".format(dealer_hand))
        print("Dealer score : {}".format(self.dealer.score))
        print()
        print("{}'s hand : {}".format(self.player.name, player_hand))
        print("{}'s score : {}".format(self.player.name, self.player.score))
        print()
        print("{}'s current bet : ${}.00".format(self.player.name, self.player.bet))
        print("{}'s current bank: ${}.00".format(self.player.name, self.player.funds))
        print("-" * 40)
        return ''

    def deal_card(self, player):
        '''Deal Cards'''
        card = self.deck.stack.pop()
        player.hand.append(card)

    def calculate_score(self, player):
        '''Calculate Score'''
        ace = False
        score = 0
        for card in player.hand:
            if card[1] == 1 and not ace:
                ace = True
                card = ('A', 11)
            score += card[1]
        player.score = score
        if player.score > 21 and ace:
            player.score -= 10
            score = player.score
        self.check_win(score, player)
        return

    def check_win(self, score, player):
        '''Check Win'''
        if score == 21:
            print(self)
            print("{} blackjack!".format(player.name))
            print()
            self.check_final_score()
        elif score > 21:
            print()
            print(self)
            print("{} busts".format(player.name))
            print()
            self.check_final_score()
        else:
            return

    def check_final_score(self):
        '''Check Final Score'''
        dealer_score = self.dealer.score
        player_score = self.player.score

        if ((dealer_score > player_score) and (dealer_score <= 21)) or (player_score > 21): 
            print("Dealer wins!")
            print()
            self.end_game()
        else:
            print("{} wins!".format(self.player.name))
            print()
            self.player.payout()
            self.end_game()
        return

    def end_game(self):
        '''End Game'''
        bank = self.player.funds
        if bank >=10:
            repeat = input("Do you want to play again (Y/N)? ")
            if repeat == "y" or repeat.lower() == "y":
                self.__init__(self.player.name, funds=self.player.funds)
            if repeat == "n" or repeat.lower() == "n":
                quit()  
        elif bank < 10:
            print("You're all out of money!")
            quit()

class Dealer(object):

    def __init__(self):
        '''__init__'''
        self.name = "Dealer"
        self.score = 0
        self.hand = []

class Player(Dealer):

    def __init__(self, name, funds, bet=0):
        super().__init__()
        self.name = name
        self.funds = funds
        self.bet = bet

    def place_bet(self, amount=10):  # Default Bet is 10
        '''Beginning of every hand'''
        self.funds -= amount
        self.bet = amount

    def payout(self):
        '''Payout added to funds'''
        self.funds += (self.bet * 3)

class Deck(object):
    '''Deck Class'''

    def __init__(self):
        '''Tuples: [0] String to show Players hand'''
        self.stack = [('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5),
                      ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10),
                      ('J', 10), ('Q', 10), ('K', 10)] * 4
        self.shuffle()

    def shuffle(self):
        '''Shuffle our deck'''
        shuffle(self.stack)

    def deal_card(self):
        '''Dealing cards'''
        card = self.stack.pop()
        return card

def hit_me():
    '''Game Play'''
    while True:
        choice = input("Do you want another card (Y/N)? ")
        if choice.lower().startswith('y'):
            return True
        elif choice.lower().startswith('n'):
            return False
        else:
            print("I didn't understand")
            continue

def start():
    '''Main starting the Game'''
    player_name = input("Welcome to BlackJack!  What's your name? ")
    Gameplay(player_name)

start()