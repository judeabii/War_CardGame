# War
This is simulation of the card game - War, using Python.

Wiki link for better explanation of the game - [War (card game)](https://en.wikipedia.org/wiki/War_(card_game))

## Code Explanation

Class `Card` defines the attributes of each card required for the game and also has a str() function for easy printing, if required.
```commandline
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.valuecard = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit
```

The `Deck` class is used to generate a shuffled deck of cards and provides a list of cards which allows players to draw cards from.
```commandline
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
```

Lastly, the class `Player` has information on the player, such as the cards in the player's hand, the number of cards and the Player's name.
Also adds the function of removing cards from the hand.

```commandline
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
```

### Gameplay

The deck of 52 is distributed to the two players such that each has 26 cards. The last card in the hands of the players
are compared. Whoever has the highest value, keeps both the cards.

If however, both the cards have the same value, we go to ***War***.

In war, each player takes 5 cards into the playing hand. If any player is unable to, the player forfeits. 

Again, the last card in each player's playing hand is compared, and the process goes on.

#### Snippet of portion of output
```commandline
round 50
Player name: player one has 2 cards.
Player name: player_two has 50 cards.
WAR!!
player_two wins!! Player one cannot continue the war
```

**NOTE : This is a simulation of the gameplay, and not user is not involved in it.** 