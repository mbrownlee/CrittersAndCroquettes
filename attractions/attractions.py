class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle!"
        self.animals = list()

    def addAnimals(self, animals):
        self.animals.extend(animals)

    @property
    def last_critter_added(self):
        return (f"{self.animals[-1].name} the {self.animals[-1].species} was the most recent animal added.")


class ReptileHouse:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "snakes and slimy things of all sizes"
        self.animals = list()

    def addAnimals(self, animals):
        self.animals.extend(animals)

    @property
    def last_critter_added(self):
        return (f"{self.animals[-1].name} the {self.animals[-1].species} was the most recent animal added.")
   


class WetLands:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "one acre walk through with lots of water animals"
        self.animals = list()

    def addAnimals(self, animals):
        self.animals.extend(animals)

    @property
    def last_critter_added(self):
        return (f"{self.animals[-1].name} the {self.animals[-1].species} was the most recent animal added.")