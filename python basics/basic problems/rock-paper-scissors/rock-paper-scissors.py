import random

game_items = {
    1: 'rock',
    2: 'paper',
    3: 'scissors',
}
computer_choice = game_items[random.randint(1, 3)]
print(computer_choice)
user_win = False
draw = False
while True:
    try:
        user_choice = int(input('Pick one:\n1. Rock\n2. Paper\n3. Scissors\n'))
        match user_choice:
            case 1:
                print('Your pick: rock.')
                if computer_choice == 'scissors':
                    user_win = True
                elif computer_choice == 'rock':
                    draw = True
                break
            case 2:
                print('Your pick: paper.')
                if computer_choice == 'rock':
                    user_win = True
                elif computer_choice == 'paper':
                    draw = True
                break
            case 3:
                print('Your pick: Scissors.')
                if computer_choice == 'paper':
                    user_win = True
                elif computer_choice == 'scissors':
                    draw = True
                break
            case _:
                print('You need to enter number from 1 to 3.')
    except ValueError:
        print('You need to enter the integer number from 1 to 3.')
print(f'My pick: {computer_choice}.')
if draw:
    print('It is draw!')
else:
    print('You won!' if user_win else 'You lose.')
