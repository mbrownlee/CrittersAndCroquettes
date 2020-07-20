from datetime import date
from .animal import Animal
from .has_shift import HasShift

class Llama(Animal, HasShift):

    def __init__(self, name, species, shift, food, chip_number):
        Animal.__init__(self, name, species, food, chip_number)
        HasShift.__init__(self, shift)
        self.walking = True

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


class Goat(Animal, HasShift):

    def __init__(self, name, species, shift, food, chip_number):
        Animal.__init__(self, name, species, food, chip_number)
        HasShift.__init__(self, shift)
        self.walking = True


class Bunny(Animal, HasShift):

    def __init__(self, name, species, shift, food, chip_number):
        Animal.__init__(self, name, species, food, chip_number)
        HasShift.__init__(self, shift)
        self.walking = True



class Bobcat(Animal, HasShift):

    def __init__(self, name, species, shift, food, chip_number):
        Animal.__init__(self, name, species, food, chip_number)
        HasShift.__init__(self, shift)
        self.walking = True


class Ostrich(Animal, HasShift):

    def __init__(self, name, species, shift, food, chip_number):
        Animal.__init__(self, name, species, food, chip_number)
        HasShift.__init__(self, shift)
        self.walking = True


class Python(Animal):

    def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.slithering = True



class Boa(Animal):

    def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.slithering = True

    def feed(self):
      print(f"On {date.today()}, {self.name} had it's chin scratched so it would eat its {self.food}.")



class Catepillar(Animal):

    def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.slithering = True



class Inchworm(Animal):

    def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.slithering = True



class Cottonmouth(Animal):

    def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.slithering = True



class Clownfish(Animal):

     def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.swimming = True



class Blowfish(Animal):

      def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.swimming = True


class Turtle(Animal):

      def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.swimming = True


class Beluga(Animal):

      def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.swimming = True

      def feed(self):
        print(f"On {date.today()}, {self.name} played hide and seek before feeding time so it would eat its {self.food}.")


class Penguin(Animal):

      def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.swimming = True