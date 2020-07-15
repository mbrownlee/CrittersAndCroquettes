from datetime import date

class Llama:

    def __init__(self, name, species):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


miss_fuzz = Llama("Miss Fuzz", "domestic llama")
for prop, value in miss_fuzz.__dict__.items():
    print(f'{prop}:\n{value}\n')


class Goat:

    def __init__(self, name, species):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

fuzz_butt = Goat("Fuzz Butt", "cutest baby goat ever")
print(fuzz_butt.name)


class Bunny:

    def __init__(self, name, species):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

bugs = Bunny("Bugs", "wraskly rabbit")
print(bugs.name)


class Bobcat:

    def __init__(self, name, species):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

rufus = Bobcat("Rufus", "best party cat")
print(rufus.name)


class Ostrich:

    def __init__(self, name, species):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

jerkface = Ostrich("Jerk Face", "biggest jerkiest bird ever")
print(jerkface.name)


class Python:

    def __init__(self, name, species):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

eek = Python("Eek", "slimy")
print(eek.name)


class Boa:

    def __init__(self, name, species):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

heckno = Boa("Heck No", "nope")      
print(heckno.name)


class Catepillar:

    def __init__(self, name, species):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

becoming = Catepillar("Becoming Butterfly", "transitional")
print(becoming.name)


class Inchworm:

    def __init__(self, name, species):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

tiny = Inchworm('Tiny', "green worm")
print(tiny.name)


class Cottonmouth:

    def __init__(self, name, species):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

gross = Cottonmouth("Gross", "run away")
print(gross.name)


class Clownfish:

    def __init__(self, name, species):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

nemo = Clownfish("Nemo", "rebellious kid fish")
print(nemo.name)


class Blowfish:

    def __init__(self, name, species):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

notouchy = Blowfish("No Touchy", "spiky fish")
print(notouchy.name)


class Turtle:

    def __init__(self, name, species):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

dude = Turtle("Dude", "wise turtle")
print(dude.name)


class Beluga:

    def __init__(self, name, species):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

smooshy = Beluga("Smooshy", "darn cute whale")
print(smooshy.name)


class Penguin:

    def __init__(self, name, species):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

tuxedo = Penguin("Tuxedo", "formal cutie")
print(tuxedo.name)
