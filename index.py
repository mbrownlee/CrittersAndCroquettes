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
from animals import Goose
from animals import Animal
from attractions import PettingZoo
from attractions import WetLands
from attractions import ReptileHouse
from attractions import Attraction
# from movements import Walking
# from movements import Swimming
# from movements import Slithering

bob = Goose("Bob", "Canada goose", "morning","watercress sandwiches", 44995)
bob.run()
bob.swim()

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "midday", "llama chow", 55234)
print(miss_fuzz.chip_number)


print(miss_fuzz.name)
print(f'{miss_fuzz.name}, the {miss_fuzz.species}, is available to pet during the {miss_fuzz.shift} shift.')
miss_fuzz.feed()

fuzz_butt = Goat("Fuzz Butt", "cutest baby goat ever", "morning", "goat food", 55012)
print(fuzz_butt)
print(f'{fuzz_butt.name}, the {fuzz_butt.species}, is available to pet during the {fuzz_butt.shift} shift.')
fuzz_butt.feed()

bugs = Bunny("Bugs", "wraskly rabbit", "afternoon", "carrots", 55901)
print(bugs)
print(f'{bugs.name}, the {bugs.species}, is available to pet during the {bugs.shift} shift.')
bugs.feed()

rufus = Bobcat("Rufus", "best party cat", "morning", "bobcat chow", 55743)
print(rufus)
print(f'{rufus.name}, the {rufus.species}, is available to pet during the {rufus.shift} shift.')
rufus.feed()

jerkface = Ostrich("Jerk Face", "biggest jerkiest bird ever", "afternoon", "stolen pellets", 55821)
print(jerkface)
print(f'{jerkface.name}, the {jerkface.species}, is available to pet during the {jerkface.shift} shift.')
jerkface.feed()

eek = Python("Eek", "slimy", "ill behaved children", 33935)
print(eek)
eek.feed()

heckno = Boa("Heck No", "nope", "mice", 33912)
print(heckno)
heckno.feed()

becoming = Catepillar("Becoming Butterfly", "transitional", "milkweed", 33054)
print(becoming)
becoming.feed()

tiny = Inchworm('Tiny', "green worm", "worm food", 33664)
print(tiny)
tiny.feed()


gross = Cottonmouth("Gross", "run away", "mice", 33742)
print(gross)
gross.feed()

nemo = Clownfish("Nemo", "rebellious kid fish", "fish food", 77001)
print(nemo)
nemo.feed()

notouchy = Blowfish("No Touchy", "spiky fish", "fish food", 77824)
print(notouchy)
notouchy.feed()

dude = Turtle("Dude", "wise turtle", "turtle chow", 77931)
print(dude)
dude.feed()

smooshy = Beluga("Smooshy", "darn cute whale", "whale mix", 77096)
print(smooshy)
smooshy.feed()

tuxedo = Penguin("Tuxedo", "formal cutie", "baby fish", 77843)
print(tuxedo)
tuxedo.feed()

def report_animals_by_attractions(*attractions):

    for attraction in attractions:
        print(f'{attraction.attraction_name} is where you can find {attraction.description} like:')
        for animal in attraction.animals:
            print(f'* {animal.name} the {animal.species}.')


varmint_village = PettingZoo("Varmint Village", "cute and fuzzy critters to cuddle!")
varmint_village.animals.extend([bugs, miss_fuzz, fuzz_butt, rufus, jerkface])
for animal in varmint_village.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}.')
print(varmint_village.last_critter_added)
# varmint_village.add_animal(bob)
# for animal in varmint_village.animals:
#     print(animal)

slither_inn = ReptileHouse("Slither Inn", "snakes and slimy things of all sizes")
slither_inn.animals.extend([eek, heckno, becoming, tiny, gross])
for animal in slither_inn.animals:
    print(f'You can find {animal.name} the {animal.species} in {slither_inn.attraction_name}.')
print(slither_inn.last_critter_added)


critter_cove = WetLands("Critter Cover", "one acre walk through with lots of water animals")
critter_cove.animals.extend([nemo, notouchy, dude, smooshy, tuxedo])
for animal in critter_cove.animals:
    print(f'You can find {animal.name} the {animal.species} in {critter_cove.attraction_name}.')
print(critter_cove.last_critter_added)

report_animals_by_attractions(critter_cove, slither_inn, varmint_village)