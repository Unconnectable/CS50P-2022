def main():
    menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    ans = float(0)
    ans = round(ans,2)
    while True:
        try:
            name  = input("Item: ").title()
            if name in menu:
                ans +=menu[name]
                ans = round(ans,2)
                print(f"Total: ${ans:.2f}")
        except EOFError:
            print()
            break

if __name__=="__main__":
    main()
