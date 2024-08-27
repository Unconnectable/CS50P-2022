from telnetlib import GA


class Vault:
    def __init__(self,galleons=0,sickles=0,knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    def __str__(self):
        return f"{self.galleons} {self.sickles} {self.knuts}"
    def __add__(A,B):
        galleons = A.galleons + B.galleons
        sickles = A.sickles + B.sickles
        knuts = A.knuts +B.knuts
        return Vault(galleons,sickles,knuts)

potter = Vault(100,200,300)
Galot = Vault(1,2,3)
print(potter)

tot = potter+Galot
print(tot)

