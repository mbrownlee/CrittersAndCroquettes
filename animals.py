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


miss_fuzz = Llama("Miss Fuzz", "domestic llama", "midday", "llama chow")
print(miss_fuzz)
print(f'{miss_fuzz.name}, the {miss_fuzz.species}, is available to pet during the {miss_fuzz.shift} shift.')
miss_fuzz.feed()


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

fuzz_butt = Goat("Fuzz Butt", "cutest baby goat ever", "morning", "goat food")
print(fuzz_butt)
print(f'{fuzz_butt.name}, the {fuzz_butt.species}, is available to pet during the {fuzz_butt.shift} shift.')
fuzz_butt.feed()

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

bugs = Bunny("Bugs", "wraskly rabbit", "afternoon", "carrots")
print(bugs)
print(f'{bugs.name}, the {bugs.species}, is available to pet during the {bugs.shift} shift.')
bugs.feed()


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

rufus = Bobcat("Rufus", "best party cat", "morning", "bobcat chow")
print(rufus)
print(f'{rufus.name}, the {rufus.species}, is available to pet during the {rufus.shift} shift.')
rufus.feed()


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

jerkface = Ostrich("Jerk Face", "biggest jerkiest bird ever", "afternoon", "stolen pellets")
print(jerkface)
print(f'{jerkface.name}, the {jerkface.species}, is available to pet during the {jerkface.shift} shift.')
jerkface.feed()


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

eek = Python("Eek", "slimy", "ill behaved children")
print(eek)
eek.feed()


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

heckno = Boa("Heck No", "nope", "mice")      
print(heckno)
heckno.feed()


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

becoming = Catepillar("Becoming Butterfly", "transitional", "milkweed")
print(becoming)
becoming.feed()


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

tiny = Inchworm('Tiny', "green worm", "worm food")
print(tiny)
tiny.feed()


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

gross = Cottonmouth("Gross", "run away", "mice")
print(gross)
gross.feed()


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

nemo = Clownfish("Nemo", "rebellious kid fish", "fish food")
print(nemo)
nemo.feed()


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

notouchy = Blowfish("No Touchy", "spiky fish", "fish food")
print(notouchy)
notouchy.feed()


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

dude = Turtle("Dude", "wise turtle", "turtle chow")
print(dude)
dude.feed()


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

smooshy = Beluga("Smooshy", "darn cute whale", "whale mix")
print(smooshy)
smooshy.feed()


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

tuxedo = Penguin("Tuxedo", "formal cutie", "baby fish")
print(tuxedo)
tuxedo.feed()
