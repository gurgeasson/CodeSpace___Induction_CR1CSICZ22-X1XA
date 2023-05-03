# load modules
from random import randrange # load random module

# declare functions

# declare global variables
name = input('What is your name?\n')
play_again = '' # at the end of each round human makes a decision if want's to play more or not
is_human_choice_valid = False # is human's choice valid?
human_score = 0
computer_score = 0
god_mode = False # does human want's to cheat?
computer_choices = {
  1: 'Rock',
  2: 'Paper',
  3: 'Scissors'
}

# introduction
print(f'\n\nHi {name},')
print('this is a rock paper scissor game where a human player can compete against the computer. please follow the instructions.\n')

# main while loop
while play_again.lower() not in ('no', 'n'):
  
  # let human choose first 
  while not is_human_choice_valid: # make human choose R/P/S till human makes valid choice
    human_choice_string = input('\ntype R for Rock, P for Papper, S for Scissors. press return\n')
    # convert human's choice to integer, validate choice, write choice on screen
    if human_choice_string.lower() in ('r', 'rock'):
      print('\n=============\nhuman chose Rock')
      human_choice = 1
      is_human_choice_valid = True
    elif human_choice_string.lower() in ('p', 'papper'): 
      print('\n=============\nhuman chose Papper')
      human_choice = 2
      is_human_choice_valid = True
    elif human_choice_string.lower() in ('s', 'scissors'):
      print('\n=============\nhuman chose Scissors')
      human_choice = 3
      is_human_choice_valid = True
    elif human_choice_string == 'iddqd':
      god_mode = True
      is_human_choice_valid = False
    else: 
      is_human_choice_valid = False

  # let computer choose now
  computer_choice = randrange(3) + 1 # generate computer's choice 
  print(f'computer chose {computer_choices[computer_choice]}\n') # write computer's choice on screen in human readable form   
  
  #print(type(humanChoice)) # debug
  #print(type(computerChoice)) # debug
  #print(humanChoice, ' ', computerChoice) # debug

  # calculate winner, announce winner, increment points
  if god_mode:
    print('human wins this round\n')
    human_score += 1
  elif human_choice - computer_choice == 1 or human_choice - computer_choice == -2:
    print('human wins this round\n')
    human_score += 1
  elif human_choice - computer_choice == -1 or human_choice - computer_choice == 2:
    print('computer wins this round\n')
    computer_score += 1
  elif human_choice - computer_choice == 0:
    print('draw\n')
  else:
    print('error\n')
    
  # ask if human want's to play more
  play_again = input('does human want\'s to play more?\nyes/no\n')
  
  is_human_choice_valid = False # reset variable so human will be presented with new choice in next round

# once while loop broken, announce winner
print (f'\nhuman : computer\n{human_score} : {computer_score}\n')
if human_score > computer_score:
  print('human win this game')
elif computer_score > human_score:
  print('computer win this game')
else:
  print('draw')