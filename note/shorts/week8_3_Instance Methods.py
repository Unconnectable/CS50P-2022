from itertools import count


class Package:
    def __init__(self,num,sender,ripient,weight):
        self.num = num
        self.sender = sender
        self.ripient = ripient
        self.weight = weight
    def __str__(self):
        return f"{self.num} {self.sender} {self.ripient} {self.weight}"
    def count_(self,per):
        return int(self.weight*per)

def main():
    packages = [
        Package(num=1,sender="Phrink",ripient="Bear",weight="200"),
        Package(num=2,sender="filament",ripient="shadows",weight="100"),
    ]
    for package in packages:
        print(f"{package} {package.count_(10)}") 


if __name__=="__main__":
    main()