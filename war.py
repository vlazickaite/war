import random
import sys

class Card:
    def __init__(self, card_id, card_value):
        self.card_id = card_id
        self.card_value = card_value
    
    def __str__(self):
        return(f"ID: {self.card_id}, Value: {self.card_value}")

class Deck:
    def __init__(self, card_deck, players_deck, computers_deck):
        self.deck = []
        self.card_deck = card_deck
        self.players_deck = players_deck
        self.computers_deck = computers_deck
    
    def mix_card_deck(self, card_deck):
        mixed_cards = []
        deck = card_deck
        list_ids = list(range(0,len(deck)))
        random.shuffle(list_ids)
        
        for i in list_ids:
            temp_num = int(i)
            mixed_cards.append(deck[temp_num])

        for card in mixed_cards:
            print(card)
        
        return mixed_cards
    
    def deal_cards(self, card_deck):
        mixed_card_deck = self.mix_card_deck(self.card_deck)
        total_deck_length = int(len(mixed_card_deck) / 2)
        print(total_deck_length)
        deck_1 = mixed_card_deck[0:total_deck_length]
        deck_2 = mixed_card_deck[total_deck_length:]
        return deck_1, deck_2
        


class Player:
    def __init__(self, ID, player_card_deck):
        self.ID = ID
        self.player_card_deck = player_card_deck
        
        
    def play_card(self):
        #from player card card take the first card from the list
        card = self.player_card_deck[0]
        self.player_card_deck.pop(0)
        return card
        
        

class Game:
    def __init__(self, player_card, computer_card):
        self.player_card = player_card
        self.computer_card = computer_card
        
        
    def check_cards(self):
        if self.player_card.card_value > self.computer_card.card_value:
            print("player wins")
        elif self.player_card.card_value < self.computer_card.card_value:
            print("computer wins")
        else:
            print("draw")
        return [self.player_card, self.computer_card]
        
            
        
# option 1
'''deck_of_cards = [
    'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK', 'HA',
    'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK', 'DA',
    'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK', 'CA',
    'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'SA'
]

# option 2
deck_of_cards = [
    Card('H2', '2'), Card('H3', '3'), Card('H4', '4'), Card('H', '5'), Card('H', '6'),
    Card('H', '7'), Card('H', '8'), Card('H', '9'), Card('H', '10'), Card('H', 'J'),
    Card('H', 'Q'), Card('H', 'K'), Card('H', 'A'),

    Card('D', '2'), Card('D', '3'), Card('D', '4'), Card('D', '5'), Card('D', '6'),
    Card('D', '7'), Card('D', '8'), Card('D', '9'), Card('D', '10'), Card('D', 'J'),
    Card('D', 'Q'), Card('D', 'K'), Card('D', 'A'),

    Card('C', '2'), Card('C', '3'), Card('C', '4'), Card('C', '5'), Card('C', '6'),
    Card('C', '7'), Card('C', '8'), Card('C', '9'), Card('C', '10'), Card('C', 'J'),
    Card('C', 'Q'), Card('C', 'K'), Card('C', 'A'),

    Card('S', '2'), Card('S', '3'), Card('S', '4'), Card('S', '5'), Card('S', '6'),
    Card('S', '7'), Card('S', '8'), Card('S', '9'), Card('S', '10'), Card('S', 'J'),
    Card('S', 'Q'), Card('S', 'K'), Card('S', 'A')
]'''

def main():
    deck = [
        {"card_id" : "H2", "card_value" : 2},
        {"card_id" : "H3", "card_value" : 3},
        {"card_id" : "H4", "card_value" : 4},
        {"card_id" : "H5", "card_value" : 5},
        {"card_id" : "H6", "card_value" : 6},
        {"card_id" : "H7", "card_value" : 7}
    ]
    card_deck = []
    for card in deck:
        temp_card = ''
        temp_card = Card(card["card_id"], card["card_value"])
        card_deck.append(temp_card)
        # print(temp_card.card_id)

    player_deck = []
    computer_deck = []
    player_deck, computer_deck = Deck(card_deck, player_deck, computer_deck).deal_cards(card_deck)
    player = Player("player", player_deck)
    computer = Player("computer", computer_deck)
    player_card = player.play_card()
    computer_card = computer.play_card()
    game = Game(player_card, computer_card)
    cards_to_give = game.check_cards()
    
    
    

   
    


main()