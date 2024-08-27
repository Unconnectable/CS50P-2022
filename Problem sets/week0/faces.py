def convert(name):
    name=name.replace(':)','🙂')
    name=name.replace(':(','🙁')
    return name

def main():
    name = input("This is name ")
    print(convert(name))

main()
