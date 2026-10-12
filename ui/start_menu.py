def start_menu(save_exists=False):
    print('Welcome Mortals to the world of Adventure Game!!')
    print('\n')
    print('Please select what an option!')
    print('\n')
    print('1. New Game')
    print('2. Load Game' if save_exists else '')
    user_input = input('Choose your option')

    if user_input == 1:
        option_chosen = "new"
    elif user_input == 2 & save_exists:
        option_chosen = "load"
    else:
        option_chosen = "error"

    return option_chosen

# TODO If statement should lead to another UI function.
# Returning it into the main function is not efficient
