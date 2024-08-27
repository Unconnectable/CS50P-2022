import random

class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    @classmethod
    def sort(fuckme,name):
        print(name, "is in", random.choice(Hat.houses))

Hat.sort("Harry")
