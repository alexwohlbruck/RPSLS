import random

WINNING_SCORE = 3
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
LIZARD = 'lizard'
SPOCK = 'spock'
CHOICES = [ROCK, PAPER, SCISSORS, LIZARD, SPOCK]
COMBINATIONS = [
  (SCISSORS, 'cuts', PAPER),
  (PAPER, 'covers', ROCK),
  (ROCK, 'crushes', LIZARD),
  (LIZARD, 'poisons', SPOCK),
  (SPOCK, 'smashes', SCISSORS),
  (ROCK, 'crushes', SCISSORS),
  (SCISSORS, 'decapitates', LIZARD),
  (LIZARD, 'eats', PAPER),
  (PAPER, 'disproves', SPOCK),
  (SPOCK, 'vaporizes', ROCK)
]

computer_score = 0
user_score = 0

def generate_choice():
  return random.choice(CHOICES)

def determine_winner(choice1, choice2):
  if choice1 == choice2:
    return None
  
  for combo in COMBINATIONS:
    winner = combo[0]
    verb = combo[1]
    loser = combo[2]
    
    def print_result():
      print(winner.capitalize() + ' ' + verb + ' ' + loser)
      
    if choice1 == winner and choice2 == loser:
      print_result()
      return True
    
    if choice2 == winner and choice1 == loser:
      print_result()
      return False

while user_score < WINNING_SCORE and computer_score < WINNING_SCORE:
  # Generate prompt string, eg. 'Rock, paper, scissors, lizard, or spock? '
  choices_english = CHOICES.copy()
  choices_english[-1] = 'or ' + choices_english[-1]
  prompt_string = ', '.join(choices_english)
  prompt_string = prompt_string.capitalize() + '? '
  
  user_choice = input(prompt_string).lower()
  
  if not user_choice in CHOICES:
    print('Invalid choice')
    continue
  
  computer_choice = generate_choice()
  print('Computer picked ' + computer_choice)
  
  user_won_round = determine_winner(user_choice, computer_choice)
  
  if user_won_round == None:
    print('Tie')
  elif user_won_round:
    print('You win the round')
    user_score += 1
  else:
    print('Computer wins the round')
    computer_score += 1
    
  print(str(user_score) + ' - ' + str(computer_score))
  
if user_score == WINNING_SCORE:
  print('You won!')

if computer_score == WINNING_SCORE:
  print('You lost!')
