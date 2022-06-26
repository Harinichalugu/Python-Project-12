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


def computer_guess(z):
    low = 1
    high = z
    feedback = ''
    while feedback !='c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low 
        feedback = input(f'Is {guess} too high(H), too Low (L), or correct (C)??').lower() 
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1

    print(f'Yay! Computer guessed your number,{guess} is correctly!!')

computer_guess(10)