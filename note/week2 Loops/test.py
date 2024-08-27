def main():
    n = get()
    f(n)

def get():
    while True:
        n = int(input("What is n? "))
        if n >0:
            break
    return n
    
def f(n):
    for _ in range(n):
        print("meow")

if __name__=="__main__":
    main()