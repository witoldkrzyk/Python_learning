import random 

player = None   

computer = random.choice(['rock','paper','scissors'])

while player == None:
    player = input("Write here your choice: ")
    if player not in ['rock','paper','scissors']:
        print("You must choose the valid value")
        player = None


if player == computer:
    print("Draw!")

if player == 'sccissors':
    if computer == 'rock':
        print("Computer wins!")
    elif computer == 'paper':
        print("Player wins!")

if player == 'paper':
    if computer == 'rock':
        print('Player wins!')
    elif computer == 'scissors':
        print('Computer wins!')

if player == 'rock':
    if computer == 'paper':
        print('Computer wins!')
    elif computer == 'scissors':
        print('Computer wins!')


print('Computer choose:  {}'.format(computer))
print('Player choose: {}'.format(player))