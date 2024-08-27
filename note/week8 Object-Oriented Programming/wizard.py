class Wizard:
    def __init__(self,name): 
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Studnet(Wizard):
    def __init__(self, name,house):
        super().__init__(name)
        self.house = house
        
class Professor(Wizard):
    def __init__(self, name,subject):
        super().__init__(name)
        self.subject = subject
a = Wizard("Phrink")
b = Studnet("Kelly","Sichuan")
c = Professor("SnowFall","Mathematic ") 