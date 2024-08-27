import random
class Hat:
    houses = ["Chengdu","Peking","Shanghai","Shenzhen"]
    
    @classmethod
    def sort(cls,name):
        print(name,"is in ",random.choice(cls.houses))

hat = Hat()
hat.sort("Harry")