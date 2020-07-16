from animals import Llama
from animals import Goat
from animals import Bunny
from animals import Bobcat
from animals import Ostrich
from animals import Boa
from animals import Python
from animals import Catepillar
from animals import Inchworm
from animals import Cottonmouth
from animals import Clownfish
from animals import Blowfish
from animals import Beluga
from animals import Turtle
from animals import Penguin
from attractions import PettingZoo
from attractions import WetLands
from attractions import ReptileHouse

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "midday", "llama chow")
print(miss_fuzz)
print(f'{miss_fuzz.name}, the {miss_fuzz.species}, is available to pet during the {miss_fuzz.shift} shift.')
miss_fuzz.feed()

fuzz_butt = Goat("Fuzz Butt", "cutest baby goat ever", "morning", "goat food")
print(fuzz_butt)
print(f'{fuzz_butt.name}, the {fuzz_butt.species}, is available to pet during the {fuzz_butt.shift} shift.')
fuzz_butt.feed()

bugs = Bunny("Bugs", "wraskly rabbit", "afternoon", "carrots")
print(bugs)
print(f'{bugs.name}, the {bugs.species}, is available to pet during the {bugs.shift} shift.')
bugs.feed()

rufus = Bobcat("Rufus", "best party cat", "morning", "bobcat chow")
print(rufus)
print(f'{rufus.name}, the {rufus.species}, is available to pet during the {rufus.shift} shift.')
rufus.feed()

jerkface = Ostrich("Jerk Face", "biggest jerkiest bird ever", "afternoon", "stolen pellets")
print(jerkface)
print(f'{jerkface.name}, the {jerkface.species}, is available to pet during the {jerkface.shift} shift.')
jerkface.feed()

eek = Python("Eek", "slimy", "ill behaved children")
print(eek)
eek.feed()

heckno = Boa("Heck No", "nope", "mice")      
print(heckno)
heckno.feed()

becoming = Catepillar("Becoming Butterfly", "transitional", "milkweed")
print(becoming)
becoming.feed()

tiny = Inchworm('Tiny', "green worm", "worm food")
print(tiny)
tiny.feed()

gross = Cottonmouth("Gross", "run away", "mice")
print(gross)
gross.feed()

nemo = Clownfish("Nemo", "rebellious kid fish", "fish food")
print(nemo)
nemo.feed()

notouchy = Blowfish("No Touchy", "spiky fish", "fish food")
print(notouchy)
notouchy.feed()

dude = Turtle("Dude", "wise turtle", "turtle chow")
print(dude)
dude.feed()

smooshy = Beluga("Smooshy", "darn cute whale", "whale mix")
print(smooshy)
smooshy.feed()

tuxedo = Penguin("Tuxedo", "formal cutie", "baby fish")
print(tuxedo)
tuxedo.feed()

def report_animals_by_attractions(*attractions):

    for attraction in attractions:
        print(f'{attraction.attraction_name} is where you can find {attraction.description} like:')
        for animal in attraction.animals:
            print(f'* {animal.name} the {animal.species}.')
       

varmint_village = PettingZoo("Varmint Village")
varmint_village.animals.extend([bugs, miss_fuzz, fuzz_butt, rufus, jerkface])
for animal in varmint_village.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}.')


slither_inn = ReptileHouse("Slither Inn")
slither_inn.animals.extend([eek, heckno, becoming, tiny, gross])
for animal in slither_inn.animals:
    print(f'You can find {animal.name} the {animal.species} in {slither_inn.attraction_name}.')


critter_cove = WetLands("Critter Cover")
critter_cove.animals.extend([nemo, notouchy, dude, smooshy, tuxedo])
for animal in critter_cove.animals:
    print(f'You can find {animal.name} the {animal.species} in {critter_cove.attraction_name}.')

report_animals_by_attractions(critter_cove, slither_inn, varmint_village)