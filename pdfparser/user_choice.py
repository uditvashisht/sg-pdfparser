from pdfparser.custom_error import *
from colorama import Fore, Back, Style, init
init(autoreset=True)


class UserChoice:
    """ This class creates a UserChoice for each function
    """

    def __init__(self, number_of_choices):
        self.number_of_choices = number_of_choices

    def run_block(self, custom_functions, deletes=False, splits=False, sorts=False):
        """
        This one runs the prompt for taking user's input for each choice and then runs the necessary function."""
        while True:
            try:
                user_choice = int(input(f'Enter your choice (1-{self.number_of_choices}): '))

                if user_choice not in list(range(1, self.number_of_choices + 1)):
                    raise ChoiceNotInOptions

                if deletes:
                    if user_choice == 1:
                        custom_functions[0](deleting=True)
                    elif user_choice == 2:
                        custom_functions[0](deleting=False)
                elif splits:
                    if user_choice == 1:
                        custom_functions[0](all=True)
                    elif user_choice == 2:
                        custom_functions[0](all=False)
                elif sorts:
                    if user_choice == 1:
                        custom_functions[0](reverse=True)
                    elif user_choice == 2:
                        custom_functions[0](swap=True)
                    else:
                        custom_functions[0](move=True)

                else:
                    custom_functions[user_choice - 1]()

                break

            except ValueError:
                print(Fore.RED + f'Not an Integer: Enter a digit from 1 to {self.number_of_choices}')

            except ChoiceNotInOptions:
                print(Fore.RED + f'Option not in choices: Enter a digit from 1 to {self.number_of_choices}')
