def main():
    coins = [5,10,25]
    amount = 50
    print("Aount Due: 50")
    left = 50
    while True:
        Coin = int(input("Insert Coin:"))
        if  Coin in coins:
            left -= Coin
            if(left<=0):
                s = (-1)*left
                print("Change Owed:",s)
                break
            else:
                print("Amount Due:",left)
        else:
            print("Amount Due:",left)
            #Coin = int(input("Insert Coin: "))
            #left = left- Coin
if __name__ == "__main__":
    main()
