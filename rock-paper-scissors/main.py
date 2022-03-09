import random

def play():
    user=input('What is your choice ?\np = for paper, r = for rock, s = for scissors: ')
    computer = random.choice(['p','r','s'])
    if user == computer:
        print('It\'s a tie!')
    
    elif (user == 'r' and computer == 's') or (user == 'p' and computer =='r') or (user == 's' and computer =='p'):
        print('You win')
    else:
        print('You lose!')
play()
