def main():
    items = {}
    while True:
        try:
            item  = input().strip().upper()
            if item in items:
                items[item]['num']+=1
            else:
                items[item] = {'item':item,'num':1}
        except EOFError:
            break

    #for key in sorted(items.items()):
        #print(f"{items[key]['num']} {items[key]['item']}")

    sorted_items = sorted(items.items())
    for key ,ss in sorted_items:
        print(f"{items[key]['num']} {items[key]['item']}")

if __name__=="__main__":
    main()
