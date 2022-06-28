import random

def play():
    user = input("plz pick one! r for Rock, p for Paper, s for Scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'it\'s a tie'

    if is_win(user, computer):
        return 'You Won!'

    return "You Lost!"


def is_win(player, opponent):
    if (player =='r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True


print(play())