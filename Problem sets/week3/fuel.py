'''
燃料表通常以分数表示油箱里的燃油量。例如，1/4 表示油箱的燃油量为 25%，1/2 表示油箱的燃油量为 50%，3/4 表示油箱的燃油量为 75%。

在名为 fuel.py 的文件中，实现一个程序，该程序提示用户输入格式为 X/Y 的分数，其中 X 和 Y 都是整数，然后以四舍五入到最接近整数的百分比输出油箱中的燃油量。但是，如果剩余 1% 或更少，则输出 E 以表示油箱基本上是空的。如果剩余 99% 或更多，则输出 F 以表示油箱基本上是满的。

然而，如果 X 或 Y 不是整数，X 大于 Y 或 Y 为 0，则提示用户重新输入。Y 不一定必须为 4。请务必捕捉诸如 ValueError 或 ZeroDivisionError 之类的异常。
'''

'''
            # isinstance(object, classinfo)
            # 检查objiect是否是某一个种类
            # isinstance(num, int)
            # isinstance(value, (str,int))  value是str 或者int 都为真
'''
def main():
    while True:
        try:
            x,y= map(int,input("Fraction: ").split("/"))
            if x>y:
                raise ValueError
            if y==0:
                raise ZeroDivisionError
            if (not isinstance(x,int)) or (not isinstance(y,int)):
                raise ValueError
            break
        except(ValueError,ZeroDivisionError):
                pass

    result = round(x/y,2)
    if(result<=0.01):
        print("E")
    elif(result>=0.99):
        print("F")
    else:
        result =int(result *100)
        print(f"{result:.0f}%")

if __name__ == "__main__":
    main()
