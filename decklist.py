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
    def __init__(self,name,next_player=None):
        self.name=name
        self.next_player = next_player
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
    def set_next_player(self, next_player):
          self.next_player = next_player 
    def get_next_player(self):
            return self.next_player
    
class LinkPlayers:
        def __init__(self,value):
                self.head_player=Player(value)
        def get_head_player(self):
                return self.head_player
        def insert_player(self,new_value):
                new_player = Player(new_value)
                new_player.set_next_player(self.head_player)
                self.head_player = new_player
        def list_of_players(self):
                string_list=""
                current_player = self.head_player
                while current_player:
                        string_list += str(current_player.get_player())+ "\n" 
                        current_player = current_player.get_next_player()
                return string_list
        def remove_player(self, name_to_remove):
                current_player = self.get_head_player()
                if current_player.get_value()==name_to_remove:
                        self.head_player = current_player.get_next_player()
                else:
                        while current_player:
                                next_player = current_player.get_next_player()
                                if next_player.get_player() == name_to_remove:
                                        current_player.set_next_player(next_player.get_next_player())
                                        current_player = None
                                else:
                                        current_player = next_player
        def reverse_list(self):
                i = 0
                current_player = self.head_player
                player_list = []
                while current_player:
                        i+=1
                        player_list.append(current_player.get_player())
                        current_player = current_player.get_next_player()
                print(player_list)
                j = 0
                players_link_list = LinkPlayers(player_list[j])
                j+=1
                for player in player_list:
                        players_link_list.insert_player(player)
                print(players_link_list.list_of_players())
        





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
        num_players=input("How many people will be playing this round? Please note there is a maximum of 6 people: ")
        try:
                int(num_players)
        except ValueError:
                print("Input is not a number! Try Again!")
                get_num_players()
        var = input("There will be " +  num_players +  " in the next blackjack game. Press any button to confirm or t to try again: ")
        

        if int(num_players)>6:
                print("Wrong input! Please try again!")
                get_num_players()
        if var.lower()=="t":
                get_num_players()
        

        
        return int(num_players)

        

       


                

def blackjack():
      print("Welcome to blackjack!")
      var = input("Please press any letter on your keyboard to continue: ")
      num_players=get_num_players()
      player_names={}
      player_num=1
      while player_num<num_players+1:
              player_names[player_num] = input("Please input player {} name: ".format(player_num))
              player_num+=1
      players=LinkPlayers("The Dealer")
      for i in range(1,num_players+1):
        players.insert_player(player_names[i])
      print(players.list_of_players())
      players.reverse_list()
      # reverse the linked_list before starting next game







              
      





      print("Now its time for the dealer to deal the cards")
      deck_list = deck([])
      deck_obj = Deck(deck_list)
      deck_obj.shuffle_deck()
     
      

      
      
      



        



              


blackjack()
