def main():
    hello("world")
    bye("world")

def hello(name):
    print("Hello,",name)
def bye(name):
    print("Goodbye,",name)

'''
如果直接写main()的话  被import时会调用main()函数
应该写成
if __name__ =="__main()__":
    main()
'''
if __name__ =="__main()__":
    main()