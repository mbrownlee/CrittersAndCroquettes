from .animal import Animal
from movements import Walking
from datetime import date

class Llama(Animal):

    def __init__(self, name, species, shift, food, chip_number):
        Animal.__init__(self, name, species, food, chip_number)
        Walking.__init__(self, shift)
      

    # @property # The getter
    # def name(self):
    #     try:
    #         return "The animal's name is " + self.__name
    #         # Note there are 2 underscores here
    #     except AttributeError:
    #         return 0

    # @name.setter # The setter
    # # miss_fuzz.name = "Mrs. Fizz"
    # def name(self, new_name):
    #   raise RuntimeError("This name is read only. You do not have permission to change.")
    #     # if type(new_name) is str:
    #     #     self.__name = new_name
    #     # else:
    #         # raise TypeError('Please provide a string value for the name property')

    # @property # The getter
    # def walking(self):
    #     try:
    #         return "This animal walks? " + self.__walkng
    #         # Note there are 2 underscores here
    #     except AttributeError:
    #         return 0

    # @walking.setter # The setter
    # # miss_fuzz.name = "Mrs. Fizz"
    # def walking(self, new_walk):
    #     if type(new_walk) is bool:
    #         self.__walking = new_walk
    #     else:
    #         raise TypeError('Please provide a True or False value for the walking property')

    def feed(self):
      print(f'On {date.today()}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}.')