from datetime import date

class Llama:

    def __init__(self, name, species, shift):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift


miss_fuzz = Llama("Miss Fuzz", "domestic llama", "midday")
print(f'{miss_fuzz.name}, the {miss_fuzz.species}, is available to pet during the {miss_fuzz.shift} shift.')


class Goat:

    def __init__(self, name, species, shift):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

fuzz_butt = Goat("Fuzz Butt", "cutest baby goat ever", "morning")
print(f'{fuzz_butt.name}, the {fuzz_butt.species}, is available to pet during the {fuzz_butt.shift} shift.')

class Bunny:

    def __init__(self, name, species, shift):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

bugs = Bunny("Bugs", "wraskly rabbit", "afternoon")
print(f'{bugs.name}, the {bugs.species}, is available to pet during the {bugs.shift} shift.')


class Bobcat:

    def __init__(self, name, species, shift):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

rufus = Bobcat("Rufus", "best party cat", "morning")
print(f'{rufus.name}, the {rufus.species}, is available to pet during the {rufus.shift} shift.')


class Ostrich:

    def __init__(self, name, species, shift):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

jerkface = Ostrich("Jerk Face", "biggest jerkiest bird ever", "afternoon")
print(f'{jerkface.name}, the {jerkface.species}, is available to pet during the {jerkface.shift} shift.')


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
