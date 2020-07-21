from .animal import Animal
from movements import Swimming
from datetime import date

class Beluga(Animal):

      def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)
      

      def feed(self):
        print(f"On {date.today()}, {self.name} played hide and seek before feeding time so it would eat its {self.food}.")