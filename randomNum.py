import random


def guess(z):
    rand_no = random.randint(1,z)
    guess = 0
    while guess != rand_no:
        guess = int(input(f'Guess a number between 1 and {z}: '))
        if guess < rand_no:
            print('Sorry, guess again. Too low.')
        elif guess > rand_no:
            print('Sorry, guess again. Too high.')
    
    print(f'Woah, You find the exact number {rand_no}')

guess(10)