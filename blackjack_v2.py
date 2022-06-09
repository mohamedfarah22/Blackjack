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
        self.card_points = 0
        self.is_bust = False
    def welcome_player(self):
        return print("Hello {}, welcome to the game!".format(self.name))
    
    def deal_card(self,deck):
      dealt_card = random.choice(deck.deck)
      self.cards.append(dealt_card)
      deck.deck.remove(dealt_card)
      self.card_points+=self.get_card_point(dealt_card)
      return print("{} has dealt {} of {}".format(self.name,dealt_card[0],dealt_card[1]))
    def get_cards(self):
        return self.cards
    def deal_dealer_card(self,deck):
            dealt_card = random.choice(deck.deck)
            self.cards.append(dealt_card)
            deck.deck.remove(dealt_card)
            self.card_points+=self.get_card_point(dealt_card)
            if len(self.cards)==2:
                   print("{} has dealt the hidden card".format(self.name))
                   return dealt_card
            print("{} has dealt {} of {} ".format(self.name,dealt_card[0],dealt_card[1])) 
            return dealt_card
    def get_card_point(self,card):
             if card[0] == 'Jack' or card[0] == 'Queen' or card[0] == 'King':
                card[0]=10
             elif card[0] == 'Ace':
                  card[0]=1 
             return card[0]
    def get_is_bust(self):
              return self.is_bust  
      
    
    def get_card_points(self):
            return self.card_points   
   

        
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
                players_link_list = LinkPlayers(player_list[0])
                j = len(player_list)
                for j in range(j):
                        players_link_list.insert_player(player_list[j])
                        j-=1
                print(players_link_list.list_of_players())
        





def deck(list):
    for i in range(1,14):
        for s in ["Spades","Clubs","Hearts","Diamonds"]:
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
        while True:
         try:
                int(num_players)
                break
         except ValueError:
                print("Input is not a number! Try Again!")
                num_players=input("How many people will be playing this round? Please note there is a maximum of 6 people: ")
        if int(num_players)>6 or int(num_players)<1:
                print("Wrong input! Please try again!")
                get_num_players()
        elif int(num_players)<6 and int(num_players)<0:
                var = input("There will be " +  num_players +  " in the next blackjack game. Press any button to confirm or t to try again: ")
                if var.lower()=="t":
                 get_num_players()

        
        return int(num_players)

        

       

#helper Functions
                
def init_players_in_linkedlist(player_names,num_players,player_num=1):
        while player_num<num_players+1:
              player_names[player_num] = input("Please input player {} name: ".format(player_num))
              player_num+=1
        players=LinkPlayers(player_names[num_players])
        return players,player_names
def reverse_dict_and_init_linkedlist(num_players,players,player_names={}):
        for i in range(num_players-1,0,-1):
          players.insert_player(player_names[i])
        players.insert_player("The Dealer")
        return players
def insert_dealer(players):
        return players.insert_player("The Dealer")


def blackjack():
      print("Welcome to blackjack!")
      # create deck and shuffle deck
      deck_list = deck([])
      deck_obj = Deck(deck_list)
      deck_obj.shuffle_deck()
      #number of players input
      var = input("Please press any letter on your keyboard to continue: ")
      num_players=get_num_players()
      player_names={}
      # init players and put player data into linkedlist'
      players, player_names=init_players_in_linkedlist(player_names,num_players)
      for i in range(num_players-1,0,-1):
        players.insert_player(player_names[i])
      players.insert_player("The Dealer") 
      #deal initial cards to players and dealer
      current_player = players.get_head_player()
      current_player.deal_dealer_card(deck_obj)
      current_player.deal_dealer_card(deck_obj)
      current_player = current_player.get_next_player()
      while current_player:
              current_player.deal_card(deck_obj)
              current_player.deal_card(deck_obj)
              current_player = current_player.get_next_player()
      current_player = players.get_head_player().get_next_player()
      #deal additional cards based on player choice
      while current_player:
              var = input("{}, press y to deal another card or press any button to continue: ".format(current_player.name))
              var.lower()
              if var == "y":
                     current_player.deal_card(deck_obj) 
                     if current_player.get_card_points()>21:
                        print("{} has gon bust!".format(current_player.name))
                        current_player.is_bust = True
                        current_player = current_player.get_next_player()
              else:
                current_player = current_player.get_next_player()
      #deal additional cards based on dealer choice
      dealer = players.get_head_player()
     
      
      while True:
        if dealer.card_points < 17:
             dealer.deal_dealer_card(deck_obj)
             
        

        if dealer.card_points >= 17 and dealer.card_points<22:
               break
               
        if dealer.card_points>21:
               print("The dealer has gone bust!")
               dealer.is_bust=True
               break
              
      
      current_player = players.get_head_player()
      player_points_not_bust = {}
      while current_player:
              if current_player.is_bust == False:
                      player_points_not_bust[current_player.name] = current_player.get_card_points()
                      current_player = current_player.get_next_player()
              else:
                      current_player = current_player.get_next_player() 

      current_player = players.get_head_player()
      all_player_points = {}
      while current_player:
           all_player_points[current_player.name] = current_player.cards
           current_player.get_next_player()
           current_player = current_player.get_next_player()
      

      if len(player_points_not_bust)>0:
        values = player_points_not_bust.values()
        max_value = max(values)
        winners = []
        for name in player_points_not_bust:
                if player_points_not_bust[name]==max_value:
                        winners.append(name)
        
        if len(winners)==1:   
         winner = winners[0]             
         winner_cards = all_player_points[winner]
         winning_statement = ""
         for card in winner_cards:
                winning_statement += "{} of {}, ".format(card[0],card[1])
        
         print("{} is the winner of this game with the following cards: ".format(winner) + winning_statement)
        if len(winners)>1:
                draw_statement=""
                for winner in winners:
                        draw_statement+= winner + " with cards " 
                        winner_cards=all_player_points[winner] 
                        for card in winner_cards:
                                draw_statement +="{} of {} ".format(card[0],card[1]) 
                        
                print("No Winner! There is a draw between " + draw_statement)

                                


blackjack()             
continue_play = True
while continue_play:
 var = input("Press y to play again: ")
 var.lower 
 if var == "y":
   blackjack()
 else:
   continue_play = False

# refractor to helper functions
# design test for all cases
