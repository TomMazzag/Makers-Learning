import random
import time

suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']

class card():

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number


class player():

    def __init__(self):
        self.player_hand = {
            'Diamonds' : [],
            'Clubs' : [],
            'Hearts' : [],
            'Spades' : []
        }
    
    def add_to_hand(self, card):
        self.player_hand[card.suit] += [card.number]

    def show_hand(self):
        returned_text = []
        for suit in self.player_hand:
            cards = ', '.join(map(str, self.player_hand[suit]))
            returned_text.append(f'You have the {cards} of {suit}\n')
        return '\n'.join(returned_text)

player_user = player()
player_2 = player()
player_3 = player()
player_4 = player()

all_cards = []

def assignSuits():

    for suit in suits:
        for x in range(1, 14):
            all_cards.append([suit, x])
    
    card_index = [i for i in range(0, 52)]

    all_players = [player_user, player_2, player_3, player_4]
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

#time.sleep(1)
print('\nCards being shuffled ...\n')
#time.sleep(2)
print(player_user.show_hand())
#time.sleep(1.5)

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
    
    return played_card_number, played_card_suit

chosen_card = userTurn()
print(f'\nYou have chosen the {chosen_card[0]} of {chosen_card[1]}')

