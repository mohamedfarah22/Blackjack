from random import randint, random
import random
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
    random.shuffle(list)
    return list
def print_card(list):
    return print("{} of {}".format(list[0],list[1]))

All_Cards = deck([])


dealer_cards=[]
player_cards=[]

def select_random_card(upper_limit = 51):
    random_index= random.randint(0,upper_limit)
    card = All_Cards[random_index]
    return card

def deal_card(list):
    upper_limit = 51
    upper_limit = len(All_Cards) - 1
    card = select_random_card(upper_limit)
    list.append(card)
    All_Cards.remove(card)
    return list

def calculate_card_points(card_list):
    card_points=0
    for card in card_list:
        if card[0] == 'Jack' or card[0] == 'Queen' or card[0] == 'King':
            card[0]=10
        elif card[0] == 'Ace':
            card[0]=1 
        card_points += card[0]
        
    return card_points

    
def deal_initial_cards(dealer_card_list, player_card_list):
    for i in  range(0,2):
        deal_card(dealer_card_list)
        deal_card(player_card_list)
        if i <1:
            print('Dealer has dealt the visible card which is: {card} of {suit}'.format(card = dealer_card_list[0][0], suit = dealer_card_list[0][1]))
            print('Player has been dealt the first card which is: {card} of {suit} '.format(card = player_card_list[0][0], suit = player_card_list[0][1]))
        else:
            print('Dealer has been dealt the hidden card')
            print('Player has been dealt the second card which is: {card} of {suit} '.format(card = player_card_list[1][0], suit = player_card_list[1][1]))
        i+=1
    return [dealer_card_list, player_card_list]

def string_dealer_card(dealer_cards):
    dealer_card_string="The dealers cards are: "
    for card in dealer_cards:
        dealer_card_string += " {} of {}".format(card[0],card[1]) + ', '
        
    
    return dealer_card_string

deal_initial_cards(dealer_cards,player_cards)
player_points = calculate_card_points(player_cards)
dealer_points = calculate_card_points(dealer_cards)

player_cards_being_dealt = True
while player_cards_being_dealt:
 if player_points < 22:
  var = input('Do you want to be dealt another card?: ')
  var.lower()
  if var=='yes':
    deal_card(player_cards)
    player_points = calculate_card_points(player_cards)
    print("You have been dealt {card} of {suit}".format(card = player_cards[-1][0], suit = player_cards[-1][1]))
    if player_points > 21:
      print("You are bust!")
      break
  elif var == "no":
      break

upper_limit_dealer = randint(16,19)

while True:
    if player_points > 21:
        break
    elif dealer_points < upper_limit_dealer and player_points < 22:
     deal_card(dealer_cards)
     print('The dealer has dealt {card} of {suit}'.format(card = dealer_cards[-1][0], suit = dealer_cards[-1][1]))
     dealer_points=calculate_card_points(dealer_cards)
    else:
        break


if dealer_points > player_points and dealer_points <22:
    print(string_dealer_card(dealer_cards))
    print('You Lose!')
    
elif dealer_points < player_points and player_points < 22:
    print(string_dealer_card(dealer_cards))
    print("You Win!")
    
elif dealer_points > 21:
    print(string_dealer_card(dealer_cards))
    print("The dealer has gon bust with {card_points} points, therefore you win!".format(card_points = dealer_points))
    


