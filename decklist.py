import random
import numbers
class Deck:
    def __init__(self,deck):
        self.deck=deck
    def get_deck(self):
        return self.deck
    def shuffle_deck(self):
        return random.shuffle(self.deck)
class Player:
    def __init__(self,name):
        self.name=name
        self.cards=[]
    def welcome_player(self):
        return print("Hello {}, welcome to the game!".format(self.name))
    
    def deal_card(self,deck):
      dealt_card = random.choice(deck.deck)
      self.cards+=dealt_card
      deck.deck.remove(dealt_card)
      random.shuffle(deck.deck)
      return dealt_card
    def get_cards(self):
        return self.cards
    def get_player(self):
            return self.name  

def deck(list):
    for i in range(1,14):
        for s in ["Spades","Clubs","Heart","Diamonds"]:
            if i== 1:
                    i = 'Ace'
            elif i == 11:
                    i = 'Jack'
            elif i == 12:
                    i = 'Queen'
            elif i == 13:
                    i = 'King'
            list.append([i,s])
    return list

         
def get_num_players():
        num_players=input("How many people will be playing this round? Please note there is a maximum of 3 people: ")
        try:
                int(num_players)
        except ValueError:
                print("Input is not a nnumber! Try Again!")
                get_num_players()
        var = input("There will be " +  num_players +  " in the next blackjack game. Press c to confirm or t to try again: ")
        

        if int(num_players)>3:
                print("Wrong input! Please try again!")
                get_num_players()
        if var.lower()=="t":
                get_num_players()
        

        
        return int(num_players)
def players_to_init(num_players):
        print("Ok! We will need some more information before we can begin the game!")
        players_name_list=[]
        for i in range(num_players):
                name = input("Please input player name: ")
                name.lower()
                players_name_list.append(name)
        while num_players>0:
                if num_players==1:
                        player_1=Player(players_name_list[0])
                        num_players-=1
                if num_players == 2:
                       player_2=Player(players_name_list[1]) 
                       num_players-=1
                if num_players==3:
                        player_3 = Player(players_name_list[2])
                        num_players-=1
        num_players = len(players_name_list)
        if num_players==1:
                return player_1
        if num_players == 2:
                return player_1, player_2
        if num_players==3:
                return player_1, player_2, player_3
        
        

       


                

def blackjack():
      print("Welcome to blackjack!")
      var = input("Please press any letter on your keyboard to continue: ")
      num_players=get_num_players()
      dealer = Player("dealer")
      if num_players==3:
        player_1,player_2,player_3 = players_to_init(num_players)
      if num_players==2:
              player_1, player_2 = players_to_init(num_players)
      if num_players==1:
              player_1 = players_to_init(num_players)






      print("Now its time for the dealer to deal the cards")
      deck_list = deck([])
      deck_obj = Deck(deck_list)
      deck_obj.shuffle_deck()
      dealer.deal_card(dealer.cards)
      

      
      
      



        



              


blackjack()
