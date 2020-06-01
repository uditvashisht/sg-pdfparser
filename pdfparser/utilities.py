from PyPDF2 import PdfFileReader
from pdfparser.custom_error import ChoiceNotInRange, EnterCombination


def flatten_list(input_list):
    """ Flattens a nested list
    Parameters:
    -----------
    input_list : list
        Nested list of user input
    Returns:
    flat_list : list
        Flattened list
    """

    for item in input_list:
        if type(item) == list:
            flatten_list(item)
        else:
            flat_list.append(item)
    return flat_list


def process_selections(selection_string, sorts=False):
    """
    This function processes the user input and converts that string into a meaningful list
    Parameters:
    selection_string: str
        It is a processed and allowed string input by the user
    sorts: boolean
        If true, single elements are not allowed it means the list will only have range of pages [[1-3,m[2-5]]
    Returns:
    multiple_pages : list
        Used in sorting. A list in which hyphens are converted to comma [[1,3],[2,5]]
    selection_list_nested: list
        Used in delete and split. A list in which hyphens are converted to comma but single pages are also allowed [1,[1,3],[2,5]]

    """
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
    """ It checks that the page numbers entered by the user is in the range of total pages of pdf
    Parameters:
    selection_list_nested:list
        list returned by processed_selections
    total_pages:int
        Total number of pages in the PDF to be parsed
    Raises:
    ChoiceNotInRange Error if the page number is not in range.
    """
    global flat_list
    flat_list = []
    temp_list = flatten_list(selection_list_nested)
    for item in temp_list:
        if item not in range(1, total_pages + 1):
            raise ChoiceNotInRange


def file_check(pdf_path):
    """ Checks, whether the input file is pdf file, takes use of PyPDF2 to throw the error if the file can't be read.

    Returns:
    pdf : PyPDF2's pdf element
    """
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
    return pdf
