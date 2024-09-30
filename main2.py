import random
choices = ['rock', 'paper', 'scissors']

player_choice = input('enter rock, paper, or scissors (all lowercase): ')
computer_choice = random.choice(choices)

print('you chose: ', player_choice)
print('computer chose: ', computer_choice)

if player_choice == computer_choice:
    print('it is a tie!')
elif player_choice == 'rock' and computer_choice == 'scissors':
    print('rock smashes scissors! you win!')
elif player_choice == 'paper' and computer_choice == 'rock':
    print('paper covers rock! you win!')
elif player_choice == 'scissors' and computer_choice == 'paper':
    print('scissors cuts paper! you win!')
else:
    print('you lose! play again.') 