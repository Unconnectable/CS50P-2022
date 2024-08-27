def f(name):
    #找出字符串 name 中所有大写字母的位置
    #enumerate(name)返回index
    positions = [i for i, char in enumerate(name) if char.isupper()]

    # 由于我们要插入下划线，索引会变化，因此需要从后往前处理
    for pos in resered(positions):
        name = name[:pos] + "_" + name[pos:]
    name = name.lower()
    print(name)

def main():
    name = input("What is your name? ").strip()
    f(name)

if __name__ == "__main__":
    main()
