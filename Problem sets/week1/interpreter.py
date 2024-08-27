def main():
    name = input("Input num and op and num ")
    x,y,z=name.split(" ",2)
    x=int(x)
    z=int(z)
    result=f(x,y,z)
    #print(f"{result:.1f}")
    print(f"{result:.1f}")

def f(x,y,z):
    if(y=="+"):
        return x+z
    if(y=="-"):
        return x-z
    if(y=="*"):
        return x*z
    if(y=="/"):
        return x/z

main()
