from datetime import date

class Llama:

    def __init__(self, name, species, shift, food):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Goat:

    def __init__(self, name, species, shift, food):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Bunny:

    def __init__(self, name, species, shift, food):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Bobcat:

    def __init__(self, name, species, shift, food):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')        

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Ostrich:

    def __init__(self, name, species, shift, food):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')

    def __str__(self):
        return f"{self.name} is a {self.species}."



class Python:

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
