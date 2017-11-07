from random import shuffle
class Card:
    suits = ['Spades',
             'Hearts',
             'Diamonds',
             'Clubs']
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    '''def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.Value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False'''

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for l in range(0,4):
                self.cards.append(Card(i,l))
        shuffle(self.cards)
    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, n):
        self.name = n
        self.wins = 0
 #       self.card = None


class Game:
    def __init__(self):
        name1 = input("P1 please type your name")
        name2 = input("P2 please type your name")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        print(winner + " Wins this round!")

    def draw(self, p1n, p1c, p2n, p2c):
        print(p1n, 'drew', p1c, p2n, 'drew', p2c)

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            print(p1.name, 'has defeated', p2.name + '.', p1.name, 'may claim their victory prize.',
                  'The score was', p1.name, p1.wins, 'to', p2.name, p2.wins)
        elif p2.wins > p1.wins:
            print(p2.name, 'has defeated', p1.name + '.', p2.name, 'may claim their victory prize.',
                  'The score was', p1.name, p1.wins, 'to', p2.name, p2.wins)
        else:
            print("Damn it was tie. No victory prize for anyone!")

    def play_game(self):
        cards = self.deck.cards
        print("War time baby!")
        while len(cards) >= 2:
            response = input("Enter q to quit at anytime otherwise any other key to play then next round")
            if response == 'q':
                break
            else:
                p1c = self.deck.rm_card()
                p2c = self.deck.rm_card()
                p1n = self.p1.name
                p2n = self.p2.name

                self.draw(p1n, p1c, p2n, p2c)

                if p1c > p2c:
                    self.p1.wins += 1
                    self.wins(self.p1.name)
                else:
                    self.p2.wins += 1
                    self.wins(self.p2.name)

        self.winner(self.p1, self.p2)

let_do_it = Game()
let_do_it.play_game()
# I don't think you need the card attribute in player or the __lt__ method for card.