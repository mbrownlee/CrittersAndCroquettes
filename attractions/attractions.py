class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle!"
        self.animals = list()

    def addAnimals(self, animals):
        self.animals.extend(animals)


class ReptileHouse:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "snakes and slimy things of all sizes"
        self.animals = list()

    def addAnimals(self, animals):
        self.animals.extend(animals)
   


class WetLands:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "one acre walk through with lots of water animals"
        self.animals = list()

    def addAnimals(self, animals):
        self.animals.extend(animals)

   

