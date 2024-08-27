def main():
    name = input("Hello ").strip().lower()
    print(f"${value(name)}")

def value(name):
    if(name == "hello"):
        return 0
    elif(name[0] == "h" and name!="hello"):
        return 20
    else:
        return 100
if __name__ == "__main__":
    main()
