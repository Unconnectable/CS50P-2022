'''
def hello(to="world"):
    print("hello,", to)
hello()#不带参数默认为world
name = input("what's your name? ")
hello(name)

'''
#如何按照任意顺序定义函数
#不按照的话必须从上到下定义函数 否则会报错
'''
def main():
    name = input("what's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,",to)

main()    
'''

#如何创建有返回值的函数
def main():
    x= int(input("what's x? "))
    print("x square is",square(x))

def square(n):
    return n*n # pow(n,2)
main()