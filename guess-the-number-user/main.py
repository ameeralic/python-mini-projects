import random

def randnumber(x):
    guess=random.randint(1,x)
    ans=input(f'Is the number is {guess}- (Yes, Too high, Too low):')
    while ans != 'Yes':
        if ans=='Too high':
            guess=random.randint(1,guess)
            ans=input(f'Is the number is {guess}- (Yes, Too high, Too low):')
        elif ans=='Too low':
            guess=random.randint(guess,x)
            ans=input(f'Is the number is {guess}- (Yes, Too high, Too low):')
        else:
            ans=input(f'Is the number is {guess}- (Yes, Too high, Too low):')
    print('Got it!')


        

x=int(input('Welcome! Guess a number \nEnter the upper limit: '))
randnumber(x)

