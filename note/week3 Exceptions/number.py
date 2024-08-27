'''
SyntaxError:语法错误 
    x = int(input("What is x? )) 少了引号
ValueError
    x = int(input("What is x? "))  输入cat
NameError
    未定义x
'''
#x = int(input("What is x? "))
#print(f"x is {x}")
def getint(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            #print("x is not a integer")
            #pass
            continue


def main():
    print(getint("What is x? "))
main()