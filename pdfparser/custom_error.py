class Error(Exception):
    """Base class for other exceptions"""
    pass


class ChoiceNotInOptions(Error):
    """If the choice is not in option"""
    pass


class InvalidSelection(Error):
    """If the selected pages are invalid"""
    pass


class ChoiceNotInRange(Error):
    """If the page number is not in range"""
    pass


class EnterCombination(Error):
    """If user has entered only one value for swaps"""
    pass


class InputMultipleFilesError(Error):
    """ If user passes only one file in merge functions.
    """
    pass
