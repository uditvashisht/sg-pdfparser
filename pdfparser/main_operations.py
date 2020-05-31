from PyPDF2 import PdfFileReader, PdfFileWriter
from user_inputs import file_input
from user_choice import UserChoice
from custom_error import *
from utilities import *
import os
import re
from colorama import Fore, Back, Style, init
import datetime
init(autoreset=True)

INPUT_MATCH = '^[0-9][0-9,-]*[0-9]*$'
CURRENT_DIRECTORY = os.getcwd()

timestamp = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")


def user_range_input(message, number_of_pages, func, final_list, others=None, sorts=False):
    """ This function takes the user's range input and then runs the next function"""
    while True:
        try:
            if sorts:
                user_input = input(f'Please enter combination of pages (separated by hyphen[-]) [{message}]\n')
            else:
                user_input = input(f'Please enter the page numbers or range [{message}]\n')
            user_input = str(user_input).replace(' ', '')
            user_input = user_input.strip(',')
            if not re.match(INPUT_MATCH, user_input):
                raise InvalidSelection
            final_list = process_selections(user_input, sorts=sorts)
            check_pages_in_range(final_list, number_of_pages)

            if others is None:
                exec(f'{func}({final_list})')
            else:
                exec(f'{func}({final_list}, "{others[0]}", {others[1]})')
            break

        except InvalidSelection:
            print(Fore.RED + "\nInvalid Selection- Allowed options are 1,2,3 or 1-2, 3 or 1, or 1-3\n")
        except ChoiceNotInRange:
            print(Fore.RED + f'\nInvalid Page Number- Choose from pages 1 to {number_of_pages}\n')
        except EnterCombination:
            print(Fore.RED + f'\nEnter the combination of page numbers separated by hyphen(-)\n')


def write_pdf(page_number, pdf, to_directory, file_name):
    """This function writes a single page to the pdf"""
    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(pdf.getPage(page_number - 1))
    output = f'{to_directory}/{os.path.splitext(file_name)[0].replace(" ","")}_{page_number}_{timestamp}.pdf'
    with open(output, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)


def write_multiple_pages_pdf(list_of_pages, pdf, to_directory, file_name):
    """This function writes a range of pages to pdf file like 1-5 (1 to 5) and 3-1 (3 to 1)"""
    if list_of_pages[0] > list_of_pages[-1]:
        page_range = range(list_of_pages[0], list_of_pages[-1] - 1, -1)
    else:
        page_range = range(list_of_pages[0], list_of_pages[-1] + 1)

    pdf_writer = PdfFileWriter()
    output = f'{to_directory}/{os.path.splitext(file_name)[0].replace(" ","")}_{"_".join([str(i) for i in list_of_pages])}_{timestamp}.pdf'
    for item in page_range:
        pdf_writer.addPage(pdf.getPage(item - 1))
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)


def do_the_splits(final_list):
    print("Splitting...")
    to_directory = os.path.join(CURRENT_DIRECTORY, 'splits/')
    if not os.path.isdir(to_directory):
        os.mkdir(to_directory)

    for item in final_list:
        if not isinstance(item, list):
            write_pdf(item, single_pdf_element_split, to_directory, file_to_be_split)
        else:
            write_multiple_pages_pdf(item, single_pdf_element_split, to_directory, file_to_be_split)
    print(f'{len(final_list)} split files saved in directory {to_directory}')


def write_pdf_for_pages(list_of_pages, pdf, output):
    pdf_writer = PdfFileWriter()
    """This write pdf for list of pages [1, 3, 8]"""
    for item in list_of_pages:
        pdf_writer.addPage(pdf.getPage(item - 1))
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)


def delete_pages(list_of_pages, file, to_directory, deleting):
    total_pages = list(range(1, number_of_pages_delete + 1))
    if deleting:
        keep_pages = [item for item in total_pages if item not in list_of_pages]
    else:
        keep_pages = list_of_pages
    output = f'{to_directory}/{os.path.splitext(file)[0].replace(" ","")}_deleted_{list_of_pages[0]}_{list_of_pages[-1]}_{timestamp}.pdf'
    write_pdf_for_pages(keep_pages, single_pdf_element_delete, output)


def do_the_deletes(final_list, msg, deleting):
    print(f'{msg} specific pages...')
    to_directory = os.path.join(CURRENT_DIRECTORY, 'deletes/')
    if not os.path.isdir(to_directory):
        os.mkdir(to_directory)
    list_of_user_choices = []
    for item in final_list:
        if not isinstance(item, list):
            list_of_user_choices.append(item)
        else:
            if item[0] < item[-1]:
                list_of_user_choices += list(range(item[0], item[-1] + 1))
            else:
                list_of_user_choices += range(item[0], item[-1] - 1, -1)
    list_of_user_choices = list(set(list_of_user_choices))
    delete_pages(list_of_user_choices, file_to_be_deleted, to_directory, deleting)
    print(f'File after {msg.lower()} the pages have been saved in {to_directory}')


def split_options(all=True):
    to_directory = os.path.join(CURRENT_DIRECTORY, 'splits/')
    if not os.path.isdir(to_directory):
        os.mkdir(to_directory)
    if all:
        for page in range(1, number_of_pages_split + 1):
            write_pdf(page, single_pdf_element_split, to_directory, file_to_be_split)
        print(f'{number_of_pages_split} split files saved in directory {to_directory}')
    else:
        print("Enter the pages number(s) separated by comma or range of pages (1-2) or both\n")
        user_range_input("To be Split", number_of_pages_split, func="do_the_splits", final_list=None)


def delete_options(deleting=True):
    if deleting:
        msg = "To be Deleted"
        msg_2 = "Deleting"
        others = [msg_2, "deleting = True"]
    else:
        msg = "To be Kept"
        msg_2 = "Keeping"
        others = [msg_2, "deleting = False"]

    print(f'\nEnter the pages number(s)[{msg}] separated by comma or range of pages(1-2) or both\n')

    user_range_input(msg, number_of_pages_delete, func="do_the_deletes", others=others, final_list=None)


def reverse_order():
    print("Reversing the order of pages...")
    single_pdf_element = PdfFileReader(file_to_be_sorted)
    number_of_pages = single_pdf_element.getNumPages()
    to_directory = os.path.join(CURRENT_DIRECTORY, 'sorted/')
    if not os.path.isdir(to_directory):
        os.mkdir(to_directory)
    output = f'{to_directory}/{os.path.splitext(file_to_be_sorted)[0].replace(" ","")}_reversed_{timestamp}.pdf'
    list_of_pages = list(range(number_of_pages, 0, -1))
    print(list_of_pages)
    write_pdf_for_pages(list_of_pages, single_pdf_element, output)
    print(f'File with pages in the reversed order has been saved in {to_directory}')


def swap_move(final_list, msg, swap):
    to_directory = os.path.join(CURRENT_DIRECTORY, 'sorted/')
    if not os.path.isdir(to_directory):
        os.mkdir(to_directory)
    list_of_all_pages = list(range(1, number_of_pages_sort + 1))
    temp_list = list_of_all_pages.copy()
    if swap:
        for item in final_list:
            temp_list[item[0] - 1] = list_of_all_pages[item[-1] - 1]
            temp_list[item[1] - 1] = list_of_all_pages[item[0] - 1]
        message = "swapped"
    else:
        for item in final_list:
            temp_list.remove(list_of_all_pages[item[0] - 1])
            temp_list.insert(item[1] - 1, list_of_all_pages[item[0] - 1])
        message = "moved"
    output = f'{to_directory}/{os.path.splitext(file_to_be_sorted)[0].replace(" ","")}_{message}_{timestamp}.pdf'
    write_pdf_for_pages(temp_list, single_pdf_element_sort, output)
    print(f'File with {message} pages have been saved in {to_directory}')


def swap_options(reverse=False, swap=False, move=False):
    to_directory = os.path.join(CURRENT_DIRECTORY, 'sorted/')
    if not os.path.isdir(to_directory):
        os.mkdir(to_directory)
    if reverse:
        print("Reversing the order of pages...")
        output = f'{to_directory}/{os.path.splitext(file_to_be_sorted)[0].replace(" ","")}_reversed_{timestamp}.pdf'
        list_of_pages = list(range(number_of_pages_sort, 0, -1))
        write_pdf_for_pages(list_of_pages, single_pdf_element_sort, output)
        print(f'File with pages in the reversed order has been saved in {to_directory}')
    else:
        if swap:
            msg_1 = "swap"
            msg_2 = "To be swapped"
            func = "swap_move"
            others = [msg_2, "swap = True"]
        else:
            msg_1 = "move"
            msg_2 = "To be moved"
            func = "swap_move"
            others = [msg_2, "swap = False"]
        print(f'Enter the pages number(s) separated by - to {msg_1} their positions. For mulitple {msg_1}s, separate them with comma\n')
        user_range_input(msg_2, number_of_pages_sort, func=func, others=others, final_list=None, sorts=True)


split_choices = UserChoice(2)
delete_choices = UserChoice(2)
sort_choices = UserChoice(3)
split_functions = [split_options]
# split_functions = [split_all, split_specific]
delete_functions = [delete_options]
# sort_functions = [reverse_order, swap_pages, move_pages]
sort_functions = [swap_options]


def pdf_split():
    global file_to_be_split
    global single_pdf_element_split
    global number_of_pages_split
    print("\nSplit a PDF\n")
    file_to_be_split = file_input()
    single_pdf_element_split = PdfFileReader(file_to_be_split)
    number_of_pages_split = single_pdf_element_split.getNumPages()
    print(f'\nYour file {file_to_be_split} has {number_of_pages_split} page(s).\n')
    print("""What do you want to do?\n\n 1. Split all the pages\n 2. Split specific pages\n""")
    split_choices.run_block(split_functions, splits=True)


def pdf_delete():
    print("\nDelete Pages from a PDF\n")
    global file_to_be_deleted
    global single_pdf_element_delete
    global number_of_pages_delete
    file_to_be_deleted = file_input()
    single_pdf_element_delete = PdfFileReader(file_to_be_deleted)
    number_of_pages_delete = single_pdf_element_delete.getNumPages()
    print(f'\nYour file {file_to_be_deleted} has {number_of_pages_delete} page(s).\n')
    print("""What do you want to do?\n\n 1. Delete specific pages\n 2. Keep Specific pages\n""")
    delete_choices.run_block(delete_functions, deletes=True)


def pdf_merge():
    print("\nMerge PDFs\n")
    print("PDFs will be merged in the same order as in input.")
    files = file_input(single_file=False)
    to_directory = os.path.join(CURRENT_DIRECTORY, 'merged/')
    if not os.path.isdir(to_directory):
        os.mkdir(to_directory)
    pdf_writer = PdfFileWriter()
    output = f'{to_directory}/{"_".join([os.path.splitext(file)[0].replace(" ", "") for  file in files])}_{timestamp}.pdf'
    for file in files:
        pdf_reader = PdfFileReader(file)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open(output, 'wb') as output_file:
        pdf_writer.write(output_file)

    print(f'The merged file has been saved in {to_directory}')


def pdf_sort():
    print("Sort Pages of a PDF\n")
    global file_to_be_sorted
    global single_pdf_element_sort
    global number_of_pages_sort
    file_to_be_sorted = file_input()
    single_pdf_element_sort = PdfFileReader(file_to_be_sorted)
    number_of_pages_sort = single_pdf_element_sort.getNumPages()
    print(f'\nYour file {file_to_be_sorted} has {number_of_pages_sort} page(s).\n')
    print("""What do you want to do?\n\n 1. Reverse order of all the pages\n 2. Swap Pages\n 3. Move certain pages to a specific index\n""")
    sort_choices.run_block(sort_functions, sorts=True)
