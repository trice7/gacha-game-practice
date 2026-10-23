from .new_game import new_game
from .load_game import load_game


def start_menu(save_exists=False, save_data=""):
    print('Welcome Mortals to the world of Adventure Game!!')
    print('\n')
    print('Please select what an option!')
    print('\n')
    print('1. New Game')
    print('2. Load Game' if save_exists else '')
    user_input = input('Choose your option')

    if int(user_input) == 1:
        new_game()
    elif int(user_input) == 2 and save_exists:
        load_game()
    else:
        option_chosen = "error"
        print('You hit the error else')

    return
