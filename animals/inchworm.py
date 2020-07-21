from .animal import Animal

class Inchworm(Animal):

    def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.slithering = True