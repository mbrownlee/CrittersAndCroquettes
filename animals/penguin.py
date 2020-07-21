from .animal import Animal
from movements import Swimming

class Penguin(Animal):

      def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)
       