import random

blackjack_cards = ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

user_cards = random.sample(blackjack_cards, 2)
computer_cards = random.sample(blackjack_cards, 2)

print(f"your card set is {user_cards}")
print(f"computer card set is {computer_cards}")

continue_game = input("would you like to continue? yes or no?\n").lower()


while continue_game == "yes":
  new_user_cards = random.sample(blackjack_cards, 1)
  user_cards += new_user_cards

  new_computer_cards = random.sample(blackjack_cards, 1)
  computer_cards += new_computer_cards

  print(f"your card set is {user_cards}")
  print(f"computer card set is {computer_cards}")
  continue_game = input("would you like to continue? yes or no?\n").lower()
else:
  def counter(player_array):
    sum = 0
    for i in player_array:
      if i=="A" or i=="J" or i=="Q" or i=="K":
        sum += 10
      else:
        sum += i
    return sum

  user_var = counter(player_array=user_cards)
  computer_var = counter(player_array=computer_cards)


def score_board(user_score, computer_score):
  user_var = 21 - user_score
  computer_var = 21 - computer_score
    
  if user_score > 21:
    if computer_score > 21:
      print(f"Your score is {user_score}.")
      print(f"Computer score is {computer_score}.")
      print("You both lose.")
    if computer_score < 21:
      print(f"Your score is {user_score}.")
      print(f"Computer score is {computer_score}.")
      print("You lose, computer wins.")
  if user_score < 21:
    if  user_var < computer_var or computer_score > 21:
      print(f"Your score is {user_score}.")
      print(f"Computer score is {computer_score}.")
      print("You win, computer loses.")
    if user_var > computer_var:
      print(f"Your score is {user_score}.")
      print(f"Computer score is {computer_score}.")
      print("You lose, computer wins.")
  if user_score == computer_score:
    print(f"Your score is {user_score}.")
    print(f"Computer score is {computer_score}.")
    print("it's a tie")
  
score_board(user_score = user_var, computer_score = computer_var)
