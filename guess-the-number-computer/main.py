import random

def guess(x):
    number=random.randint(1,x)
    guess=0
    while guess!=number:
        guess=int(input('Enter your guess: '))
        if guess<number:
            print('Too low')
        else:
            print('Too high')
    print('You won!!')

x=int(input('Welcome! \nEnter an integer upper limit to guess: '))
guess(x)
