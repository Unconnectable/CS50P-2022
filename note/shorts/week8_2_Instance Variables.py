from re import S


class Package:
    def __init__(self,num,sender,ripient,weight):
        self.num = num
        self.sender = sender
        self.ripient = ripient
        self.weight = weight

def main():
    packages = [
        Package(num=1,sender="Phrink",ripient="Bear",weight="200kg"),
        Package(num=2,sender="filament",ripient="shadows",weight="1T"),
    ]
    for package in packages:
        print(f"Package {package.num} {package.sender} {package.ripient} {package.weight} ")


if __name__=="__main__":
    main()