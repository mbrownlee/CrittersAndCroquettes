class HasShift:

    def __init__(self, shift, chip_number):
        self.shift = shift
        self.__chip_number = chip_number

    @property # The getter
    def chip_number(self):
        try:
            return self.__chip_number
            # Note there are 2 underscores here
        except AttributeError:
            return 0

    @chip_number.setter # The setter
   
    def chip_number(self, new_chip):
        raise RuntimeError("The chip number is read only. You do not have permission to change it.")