import random

def play():
    user = input("Pick your choice, 'r' for rock, 'p' for paper, 's' for scissor: \n").lower()
    if user not in ['r', 'p', 's']:
        return "Not a valid choice"
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "You both chose {} resulting to a tie.".format(computer)

    if win(user, computer):
        return "You chose {} and the computer chose {}. You won".format(user, computer)
    return "You chose {} and the computer chose {}. You lost".format(user, computer)

def win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

if __name__ == '__main__':
    while True:
        print(play())