#match 对应 C++中的swtich
name = input("What is name? ")
match name:
    case "alice" | "Bob"| "Cindy":
        print("Simple")
    case "Linda":
        print("middle")
    case "Phrink":
        print("little hard") 
    case _:
        print("difficult")