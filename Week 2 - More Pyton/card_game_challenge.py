import random
import time

suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
suitSymbols = {
    'Diamonds' : '\033[91m♦\033[00m',
    'Clubs' : '♣',
    'Hearts' : '\033[91m♥\033[00m',
    'Spades' : '♠'
}

class card():

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number


class player():

    def __init__(self, id):
        self.id = id
        self.player_hand = {
            'Diamonds' : [],
            'Clubs' : [],
            'Hearts' : [],
            'Spades' : []
        }
        self.round_card = []
    
    def add_to_hand(self, card):
        self.player_hand[card.suit] += [card.number]

    def show_hand(self):
        returned_text = []
        for suit in self.player_hand:
            cards = ', '.join(map(str, self.player_hand[suit]))
            returned_text.append(f'You have the {cards} of {suit} {suitSymbols[suit]}\n')
        return '\n'.join(returned_text)

player_user = player('p1')
player_2 = player('p2')
player_3 = player('p3')
player_4 = player('p4')

all_cards = []
all_players = [player_user, player_2, player_3, player_4]

def assignSuits():

    for suit in suits:
        for x in range(1, 14):
            all_cards.append([suit, x])
    
    card_index = [i for i in range(0, 52)]

    
    for selected_player in all_players:
        for i in range(0, 13):
            random_card = random.choice(card_index)
            if all_cards[random_card][1] == 11:
                test_card = card(all_cards[random_card][0], 'Jack')
            elif all_cards[random_card][1] == 12:
                test_card = card(all_cards[random_card][0], 'Queen')
            elif all_cards[random_card][1] == 13:
                test_card = card(all_cards[random_card][0], 'King')
            elif all_cards[random_card][1] == 1:
                test_card = card(all_cards[random_card][0], 'Ace')
            else:
                test_card = card(all_cards[random_card][0], all_cards[random_card][1])
            selected_player.add_to_hand(test_card)
            card_index.remove(random_card)

assignSuits()

# Ace > King > Queen > Jack

time.sleep(1)
print('\nCards being shuffled ...\n')
time.sleep(2)
print(player_user.show_hand())
time.sleep(1.5)

def userTurn():

    played_card = input('Which card would you like to play (\x1B[3mnumber \x1B[0mof \x1B[3msuit\x1B[0m)?    ')
    played_card_list = played_card.split()
    if len(played_card_list) != 3:
        print('Incorrect Format')
        userTurn()
    played_card_suit = played_card_list[2]
    played_card_number = played_card_list[0]
    if played_card_number.isnumeric():
        played_card_number = int(played_card_number)

    if played_card_suit not in suits:
        print('Not a suit\n')
        userTurn()
    elif played_card_number not in player_user.player_hand[played_card_suit]:
        print('You dont have this card\n')
        userTurn()
    
    player_user.round_card.append(played_card_number)
    player_user.round_card.append(played_card_suit)
    return played_card_number, played_card_suit

chosen_card = userTurn()
time.sleep(0.5)
bold = '\033[1m'
standard = '\033[0m'
print(f'You have chosen the {bold}{chosen_card[0]}\033[0m {suitSymbols[chosen_card[1]]}')

def botTurn():
    time.sleep(1)
    print('\nOther players have chosen')

    for botPlayer in all_players[1:4]:
        randomSuit = random.choice(suits)
        while random.choice(botPlayer.player_hand[randomSuit]) == None:
            print(f'No {randomSuit}')
            randomSuit = random.choice(suits)
        randomCard = random.choice(botPlayer.player_hand[randomSuit])
        time.sleep(1)
        print(f'{bold}{randomCard}{standard} {suitSymbols[randomSuit]}\n')
        botPlayer.round_card.append(randomCard)
        botPlayer.round_card.append(randomSuit)

botTurn()

tricks = {}
for x in all_players:
    tricks[x.id] = x.round_card

print(tricks)

