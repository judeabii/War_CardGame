import random

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.valuecard = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append((Card(suit, rank)))

    def shuffle_cards(self):
        random.shuffle(self.all_cards)

    def get_card(self):
        return self.all_cards.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_card(self):
        return self.all_cards.pop(0)

    def add_cards(self, cards):
        if type(cards) == type([]):
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)

    def __str__(self):
        return f'Player name: {self.name} has {len(self.all_cards)} cards.'


player_one = Player("player one")
player_two = Player("player_two")

new_deck = Deck()
new_deck.shuffle_cards()

for x in range(26):
    player_one.all_cards.append(new_deck.get_card())
    player_two.all_cards.append(new_deck.get_card())

game_on = True
round_num = 0
while game_on:

    round_num += 1
    print(f'round {round_num}')
    print(player_one)
    print(player_two)

    if len(player_one.all_cards) == 0:
        print(f'{player_two.name} wins!!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print(f'{player_one.name} wins!!')
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_card())

    player_two_cards = []
    player_two_cards.append(player_two.remove_card())

    at_war = True
    while at_war:

        if player_one_cards[-1].valuecard > player_two_cards[-1].valuecard:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].valuecard < player_two_cards[-1].valuecard:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        else:
            print("WAR!!")

            if len(player_one.all_cards) < 5:
                print(f'{player_two.name} wins!! Player one cannot continue the war')
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print(f'{player_one.name} wins!! Player two cannot continue the war')
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())
