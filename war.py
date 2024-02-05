import random
'''
War card game implementation
Classes of:
Card (define cards in a deck), 
Deck (shuffle the deck and deal to two players),
Player (defining players actions - give and take cards) and
Game (define stage of the game, if there is the winner, or there is draw).
'''
class Card:
    def __init__(self, card_id, card_value):
        self.card_id = card_id
        self.card_value = card_value
    
    def __str__(self):
        return(f"ID: {self.card_id}, Value: {self.card_value}")

class Deck:
    def __init__(self, card_deck):
        self.deck = self.mix_card_deck(card_deck)
        self.players_deck, self.computers_deck = self.deal_cards()
    
    def mix_card_deck(self, card_deck):
        mixed_cards = list(card_deck)
        random.shuffle(mixed_cards)
        return mixed_cards
    
    def deal_cards(self):
        total_deck_length = len(self.deck) // 2
        deck_1 = self.deck[:total_deck_length]
        deck_2 = self.deck[total_deck_length:]
        return deck_1, deck_2 


class Player:
    def __init__(self, ID, player_card_deck):
        self.ID = ID
        self.player_card_deck = player_card_deck
        
    def play_card(self):
        card = self.player_card_deck.pop(0)
        return card
    
    def take_cards(self, won_cards):
        self.player_card_deck.extend(won_cards)


class Game:
    def __init__(self, player_card, computer_card):
        self.player_card = player_card
        self.computer_card = computer_card
        
        
    def check_cards(self):
        if self.player_card.card_value > self.computer_card.card_value:
            return "player"
        elif self.player_card.card_value < self.computer_card.card_value:
            return "computer"
        else:
            print("draw")
        return "draw"
        
'''
Main function has the defined deck of card ID and card value.
Card ID values stands for:
H - Hearts, D - Diamonds, C - Clubs, S - Spades, A - Ace, J - Jack, Q - Queen, K - King;
2-10 - numbers 2-10.
Functionality:
Card values are read through the Card class.
Deck is shuffled and dealt through Deck class.
Players are defined and their decks dealt with Player class.
Main while block:
Checks if the players are out of cards;
Players play the cards, checking card values and defining the round winner.
If draw block:
Played cards are put into the list, running while loop for players to play the cards.
Checking if there is draw again.
Once the winner is set, all cards add to the winner's deck.
'''
def main():
    deck = [
        {"card_id" : "HA", "card_value" : 1},
        {"card_id" : "H2", "card_value" : 2},
        {"card_id" : "H3", "card_value" : 3},
        {"card_id" : "H4", "card_value" : 4},
        {"card_id" : "H5", "card_value" : 5},
        {"card_id" : "H6", "card_value" : 6},
        {"card_id" : "H7", "card_value" : 7},
        {"card_id" : "H8", "card_value" : 8},
        {"card_id" : "H9", "card_value" : 9},
        {"card_id" : "H10", "card_value" : 10},
        {"card_id" : "HJ", "card_value" : 11},
        {"card_id" : "HQ", "card_value" : 12},
        {"card_id" : "HK", "card_value" : 13},
        {"card_id" : "DA", "card_value" : 1},
        {"card_id" : "D2", "card_value" : 2},
        {"card_id" : "D3", "card_value" : 3},
        {"card_id" : "D4", "card_value" : 4},
        {"card_id" : "D5", "card_value" : 5},
        {"card_id" : "D6", "card_value" : 6},
        {"card_id" : "D7", "card_value" : 7},
        {"card_id" : "D8", "card_value" : 8},
        {"card_id" : "D9", "card_value" : 9},
        {"card_id" : "D10", "card_value" : 10},
        {"card_id" : "DJ", "card_value" : 11},
        {"card_id" : "DQ", "card_value" : 12},
        {"card_id" : "DK", "card_value" : 13},
        {"card_id" : "CA", "card_value" : 1},
        {"card_id" : "C2", "card_value" : 2},
        {"card_id" : "C3", "card_value" : 3},
        {"card_id" : "C4", "card_value" : 4},
        {"card_id" : "C5", "card_value" : 5},
        {"card_id" : "C6", "card_value" : 6},
        {"card_id" : "C7", "card_value" : 7},
        {"card_id" : "C8", "card_value" : 8},
        {"card_id" : "C9", "card_value" : 9},
        {"card_id" : "C10", "card_value" : 10},
        {"card_id" : "CJ", "card_value" : 11},
        {"card_id" : "CQ", "card_value" : 12},
        {"card_id" : "CK", "card_value" : 13},
        {"card_id" : "SA", "card_value" : 1},
        {"card_id" : "S2", "card_value" : 2},
        {"card_id" : "S3", "card_value" : 3},
        {"card_id" : "S4", "card_value" : 4},
        {"card_id" : "S5", "card_value" : 5},
        {"card_id" : "S6", "card_value" : 6},
        {"card_id" : "S7", "card_value" : 7},
        {"card_id" : "S8", "card_value" : 8},
        {"card_id" : "S9", "card_value" : 9},
        {"card_id" : "S10", "card_value" : 10},
        {"card_id" : "SJ", "card_value" : 11},
        {"card_id" : "SQ", "card_value" : 12},
        {"card_id" : "SK", "card_value" : 13},
        
    ]

    card_deck = [Card(card["card_id"], card["card_value"]) for card in deck]
    game_deck = Deck(card_deck)

    player = Player("player", game_deck.players_deck)
    computer = Player("computer", game_deck.computers_deck)

    while True:
        if not player.player_card_deck:
            print("Computer wins! Player is out of cards.")
            break
        elif not computer.player_card_deck:
            print("Player wins! Computer is out of cards.")
            break

        player_card = player.play_card()
        computer_card = computer.play_card()

        game = Game(player_card, computer_card)
        winner = game.check_cards()

        if winner == "draw":
            print("It's a draw. Time for war.")
            war_cards = [player_card, computer_card]
            while True:
                war_cards.extend(player.player_card_deck[:3])
                war_cards.extend(computer.player_card_deck[:3])
                player_card = player.play_card()
                computer_card = computer.play_card()
                war_cards.extend([player_card, computer_card])
                
                war_winner = Game(player_card, computer_card).check_cards()
                if war_winner != "draw":
                    print(f"War winner: {war_winner}")
                    if war_winner == "player":
                        player.take_cards(war_cards)
                    else:
                        computer.take_cards(war_cards)
                    break
                else:
                    print("War continues!")
        elif winner == "player":
            player.take_cards([player_card, computer_card])
        elif winner == "computer":
            computer.take_cards([player_card, computer_card])



if __name__ == "__main__":
    main()