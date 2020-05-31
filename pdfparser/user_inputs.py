from utilities import *
from colorama import Fore, Back, Style, init
init(autoreset=True)


def file_input(single_file=True):
    while True:
        try:
            if single_file:
                file_name = str(input('Enter the name of file with extension(.pdf)\n'))
                file_check(file_name)
                return file_name
            else:
                file_names = str(input('Enter the names of files with extension(.pdf) separated by a comma\n'))
                files = file_names.split(',')
                files = [item.strip() for item in files]
                for file in files:
                    file_check(file)
                return files
            break
        except ValueError:
            print(Fore.RED + "Please enter the correct filename")
        except IOError as e:
            err_no, err_msg = e.args
            print(Fore.RED + f'IO Error-({err_no}) : {err_msg}')
