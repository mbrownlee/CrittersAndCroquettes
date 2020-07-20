from datetime import date
from .animal import Animal
from .has_shift import HasShift

class Llama(Animal, HasShift):

    def __init__(self, name, species, shift, food, chip_number):
        Animal.__init__(self, food)
        HasShift.__init__(self, shift, chip_number)

        self.__name = name
        self.species = species
        self.date_added = date.today()
        self.__walking = True

    @property # The getter
    def name(self):
        try:
            return "The animal's name is " + self.__name
            # Note there are 2 underscores here
        except AttributeError:
            return 0

    @name.setter # The setter
    # miss_fuzz.name = "Mrs. Fizz"
    def name(self, new_name):
      raise RuntimeError("This name is read only. You do not have permission to change.")
        # if type(new_name) is str:
        #     self.__name = new_name
        # else:
            # raise TypeError('Please provide a string value for the name property')

    @property # The getter
    def walking(self):
        try:
            return "This animal walks? " + self.__walkng
            # Note there are 2 underscores here
        except AttributeError:
            return 0

    @walking.setter # The setter
    # miss_fuzz.name = "Mrs. Fizz"
    def walking(self, new_walk):
        if type(new_walk) is bool:
            self.__walking = new_walk
        else:
            raise TypeError('Please provide a True or False value for the walking property')

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Goat(HasShift):

    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(shift, chip_number)
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Bunny(HasShift):

    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(shift, chip_number)
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Bobcat(HasShift):

    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(shift, chip_number)
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Ostrich(HasShift):

    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(shift, chip_number)
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}."



class Python(Animal):

    def __init__(self, name, species, food):
        super().__init__(food)

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Boa:

    def __init__(self, name, species, food):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Catepillar:

    def __init__(self, name, species, food):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Inchworm:

    def __init__(self, name, species, food):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Cottonmouth:

    def __init__(self, name, species, food):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Clownfish:

    def __init__(self, name, species, food):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Blowfish:

    def __init__(self, name, species, food):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Turtle:

    def __init__(self, name, species, food):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Beluga:

    def __init__(self, name, species, food):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Penguin:

    def __init__(self, name, species, food):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}."
