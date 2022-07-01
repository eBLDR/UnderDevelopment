class InputError(Exception):
    def __init__(self):
        msg = 'Invalid input data.'
        super().__init__(msg)
