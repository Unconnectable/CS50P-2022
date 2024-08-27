def main():
    size = int(input("Input size please "))
    Mario(size)

def Mario(size):
    '''
    for i in range(size):
        for j in range(size):
            print("#",end="")
        print()
    '''
    #等价于
    for i in range(size):
        print("#" * size)

if(__name__=="__main__"):
    main()