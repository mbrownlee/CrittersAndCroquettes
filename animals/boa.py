from .animal import Animal
from movements import Slithering
from datetime import date

class Boa(Animal):

    def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)
   

    def feed(self):
      print(f"On {date.today()}, {self.name} had it's chin scratched so it would eat its {self.food}.")
