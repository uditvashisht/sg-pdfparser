import os
import sys
from main_operations import pdf_delete, pdf_merge, pdf_sort, pdf_split
from user_choice import UserChoice
from colorama import Fore, Back, Style, init
init(autoreset=True)

ALL_OPERATIONS = [pdf_delete, pdf_merge, pdf_sort, pdf_split]

welcome_choices = UserChoice(4)


def display_welcome_message():
    # pass
    while True:
        try:
            print("\nWelcome to PDF Parser\n")
            print("What do you want to do?\n")
            print("""1. S\n2. Merge PDFs\n3. Sort Pages of a PDF\n4. Split a PDF\n""")
            print("Press ctrl + C to exit.")

            welcome_choices.run_block(ALL_OPERATIONS
                                      )
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit()


def main():
    display_welcome_message()


if __name__ == '__main__':
    main()
