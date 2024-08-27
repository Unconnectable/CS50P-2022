def main():
    x= int(input("What is x "))
    if(check(x)):
        print(x," is Even")
    else:
        print(x," is Odd")    
def check(x):
    #缩写成一行
    # return True if n%2==0 else False
    #再次改写 return (n % 2 == 0)
    if(x % 2 == 0):
        return True
    else:
        return False
main()