
#Hint 1: Create a deal_a_card() function that uses the List below to *return* a random card. 11 is the ace
#11 is the Ace.

import random

def deal_a_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card



#Hint 3: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.


def calculate_score(cards):
    
    #Hint 4: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #Hint 5: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        return sum(cards)









#Hint 10: Create a function called compare() and pass in the user_score and computer_score. 
def compare(user_score, computer_score):   
   
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
#If the computer and user both have the same score, then it's a draw.     
    if user_score == computer_score:
        return "Draw 🙃"
# If the computer has a blackjack (0), then the user loses.    
    elif computer_score == 0:
        return "You lose. Opponent has Blackjack 😱"
# If the user has a blackjack (0), then the user wins.    
    elif user_score == 0:
        return "You win. Blackjack 😱"
# If the user_score is over 21, then the user loses.    
    elif user_score > 21:
        return "You went over. You lose 😤"
# If the computer_score is over 21, then the computer loses.     
    elif computer_score > 21:
        return "You win. Opponent went over 😱"
 # If none of the above, then the player with the highest score wins.     
    elif user_score > computer_score:
        return "You win. 😱"
    
    else:
        return "You lose"
    
  

def play_game():    

    user_cards = []
    computer_cards = []  
    is_game_over = False
  
#Hint 2: Deal the user and computer 2 cards each using deal_card() and append().    
    for _ in range(2):
        user_cards.append(deal_a_card())
        computer_cards.append(deal_a_card())
        
        
    while not is_game_over:
        
#Hint 6: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}    currentscore: {user_score}")
        print(f"    Computer cards: {computer_cards}")
        
 


#Hint 7: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 8: The score will need to be rechecked with every new card drawn and the checks in Hint 6 need to be repeated until the game ends.

#Hint 9: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.



#Hint 11: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.