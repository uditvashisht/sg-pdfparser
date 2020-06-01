"""SaralGyaan PDF Parser
Installation:
------------
$ pip install sg-pdfparser

Usage:
------
$ pdfparser

Available Options:
1. Delete Pages from a PDF
2. Merge PDFs
3. Sort Pages of a PDF
4. Split a PDF

Inputs:

Top Level:

Single PDF file with file extension (.pdf) for option 1, 3 & 4 and atleast two PDF files (separated by comma) with file extension (.pdf) for option 2.

Each Function:

Delete Pages from a PDF:

Page numbers or page ranges separated by comma or both e.g. 1, 3, 4 or 1-2, 4 or 1-7, 9-11

Merge PDFs:

Atleast two PDF files (separated by comma) with file extension(.pdf). The PDFs will be merged in the order of input.

Sort Pages of PDF:

Reverse the order will reverse the order of the pages.

A hyphen separated combination of page numbers. Can add multiple separated by comma e.g. 1-9, 2-6

Swap:- Will swap page number 1 & 9 and 2 & 6.
Move:- Will move page number 1 to Page 9 and 2 to 6 moving the rest of the pages to the right.

Split a PDF:

Split all will split n-paged files into n split files one page in each.

Page numbers or page ranges separated by comma or both e.g. 1, 3, 4 or 1-2, 4 or 1-7, 9-11

1-2, 4 will make two PDF files.


Contact:
--------
- admin@saralgyaan.com

More information is available at:
- https://pypi.org/project/sg-pdfparser/
- https://github.com/uditvashisht/sg-pdfparser

Version:
---------
pdfparser v1.0.0
"""
# Inbuilt library imports
import os
import sys
# Import top level functions
from pdfparser.main_operations import pdf_delete, pdf_merge, pdf_sort, pdf_split
from pdfparser.user_choice import UserChoice
# Import colorama for color effects
from colorama import Fore, Back, Style, init
init(autoreset=True)


ALL_OPERATIONS = [pdf_delete, pdf_merge, pdf_sort, pdf_split]

welcome_choices = UserChoice(4)


def display_welcome_message():
    """ Prints the welcome screen with all the top level options of PDF Parsing

    Parameters:
    Input : int (1-4)
    """
    while True:
        try:
            print("\nWelcome to PDF Parser\n")
            print("What do you want to do?\n")
            print("""1. Delete Pages from a PDF\n2. Merge PDFs\n3. Sort Pages of a PDF\n4. Split a PDF\n""")
            print("Press ctrl + c to exit.")

            welcome_choices.run_block(ALL_OPERATIONS
                                      )
        # Keyboard interrupt
        except KeyboardInterrupt:
            print(Fore.RED + "\nExiting...")
            sys.exit()


def main():
    display_welcome_message()


if __name__ == '__main__':
    main()
