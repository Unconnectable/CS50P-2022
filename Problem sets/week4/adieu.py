import inflect
def farewell(names):
    farewell_message = f"Adieu, adieu, to {', '.join(names)}"
    #farewell_message = f"Adieu, adieu, to {', '.join(names)}"
    return farewell_message
def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            names.append(input().strip())
        except EOFError:
            break
    print(f"Adieu, adieu, to {p.join(names)}")
if __name__=="__main__":
    main()
