from PyPDF2 import PdfFileReader
from custom_error import ChoiceNotInRange, EnterCombination


def flatten_list(input_list):
    for item in input_list:
        if type(item) == list:
            flatten_list(item)
        else:
            flat_list.append(item)
    return flat_list


def process_selections(selection_string, sorts=False):
    temp_list = selection_string.split(',')
    single_pages = [int(i) for i in temp_list if '-' not in i]
    temp_multiple_pages = [i for i in temp_list if '-' in i]
    multiple_pages = [list(map(int, i.split('-'))) for i in temp_multiple_pages]
    if sorts:
        if len(single_pages) > 0:
            raise EnterCombination
        else:
            return multiple_pages
    else:
        selection_list_nested = single_pages + multiple_pages
        return selection_list_nested


def check_pages_in_range(selection_list_nested, total_pages):
    global flat_list
    flat_list = []
    temp_list = flatten_list(selection_list_nested)
    for item in temp_list:
        if item not in range(1, total_pages + 1):
            raise ChoiceNotInRange


def file_check(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
    return pdf
