from datetime import date

class Animal:
    def __init__(self, name, species, food, chip_number):
        self.name = name
        self.species = species
        self.food = food
        self.__chip_number = chip_number
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    
    def __str__(self):
        return f"{self.name} is a {self.species}."
    
    @property
    def chip_number(self):
        return self.__chip_number
    
    @chip_number.setter
    def chip_number(self, new_chip):
        raise RuntimeError("The chip number is read only. You do not have permission to change it.")

