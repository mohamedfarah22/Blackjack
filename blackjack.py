from random import randint, random
All_Cards =['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine', 'Ten','Jack','Queen','King']
All_suits=['Diamonds', 'Hearts','Clubs','Spade']
cards_with_points={'Ace':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5,'Six':6,'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10}
dealer_cards=[]
player_cards=[]

def select_random_card():
    random_number_for_cards= randint(0,12)
    random_number_for_suits=randint(0,3)
    card = All_Cards[random_number_for_cards]
    suit = All_suits[random_number_for_suits]
    return [card,suit]

def deal_card(list):
   list.append(select_random_card())
   return list

def calculate_card_points(card_list):
    card_points=0
    for card in card_list:
        card_points+=cards_with_points[card[0]]
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
    for number, suit in dealer_cards:
        dealer_card_string += number + " of " + suit + ", "
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
upper_limit_dealer = randint(17,20)
while True:
    if player_points > 21:
        break
    elif dealer_points <upper_limit_dealer:
     deal_card(dealer_cards)
     print('The dealer has dealt {card} of {suit}'.format(card = dealer_cards[-1][0], suit = dealer_cards[-1][1]))
     dealer_points=calculate_card_points(dealer_cards)
    if dealer_points > player_points and dealer_points <22:
         print(string_dealer_card(dealer_cards))
         print(dealer_cards)
         print('You Lose!')
         break
    elif dealer_points < player_points and player_points < 22:
         print(string_dealer_card(dealer_cards))
         print("You Win!")
         break
    elif dealer_points > 21:
        print(dealer_cards)
        print(string_dealer_card(dealer_cards))
        print("The dealer has gon bust with {card_points} points, therefore you win!".format(card_points = dealer_points))
        break


