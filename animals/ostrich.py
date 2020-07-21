from .animal import Animal
from movements import Walking

class Ostrich(Animal):

    def __init__(self, name, species, shift, food, chip_number):
        Animal.__init__(self, name, species, food, chip_number)
        Walking.__init__(self, shift)