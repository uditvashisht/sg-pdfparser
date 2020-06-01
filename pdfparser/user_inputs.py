from pdfparser.utilities import *
from pdfparser.custom_error import *
from colorama import Fore, Back, Style, init
init(autoreset=True)


def file_input(single_file=True):
    """
    This function takes the file input from the user

    Parameters:
    single_file : boolean
        if True, single input is allowed (used for delete, sort and split)
        else, multiple file inputs separated by comma ( used for merge )
    Returns:
    file : str
        In case of delete, sort and split
    list of files : list
        In case of merge
    """
    while True:
        try:
            if single_file:
                file_name = str(input('Enter the name of file with extension(.pdf)\n'))
                """ Throw I/O error, if file is not present"""
                file_check(file_name)
                return file_name
            else:
                file_names = str(input('Enter the names of files with extension(.pdf) separated by a comma\n'))
                files = file_names.split(',')
                files = [item.strip() for item in files]
                # If only one input is given for merge through error.
                if len(files) == 1:
                    raise InputMultipleFilesError
                for file in files:
                    file_check(file)
                return files
            break
        except ValueError:
            print(Fore.RED + "Please enter the correct filename")
        except IOError as e:
            err_no, err_msg = e.args
            print(Fore.RED + f'IO Error-({err_no}) : {err_msg}')
        except InputMultipleFilesError:
            print(Fore.RED + "\nInput at least two PDF files.\n")
