class Attraction:
    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def addAnimals(self, animals):
        self.animals.extend(animals)

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_animals(self, animals):
        self.animals.extend(animals)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def __str__(self):
        return f'{self.attraction_name} ({len(self)} animals)'

    def __len__(self):
        return len(self.animals)

    @property
    def last_critter_added(self):
        return (f"{self.animals[-1].name} the {self.animals[-1].species} was the most recent animal added.")
        

   



   


