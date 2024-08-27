class Package:
    def __init__(self,num,sender,ripient,weight):
        self.num = num
        self.sender = sender
        self.ripient = ripient
        self.weight = weight

def main():
    packages = [
        Package(100,"Phrink","Bear","200kg"),
        Package(100,"filament","shadows","1T"),
    ]
    for _ in packages:
        print(_)
main()