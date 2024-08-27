def main():
    name = input("Hello ").strip().lower()
    if(name == "hello"):
        print("$0")
    elif(name[0] == "h" and name!="hello"):
        print("$20")
    else:
        print("$100")

main()
