def f(name):
    '''
    find函数:从左边开始查找
    用法:str.rfind(sub[, start[, end]])
    举例:print(s.find("o", 5, 10))
    rfind 同find 从右边开始查找
    '''
    pos= name.rfind(".")
    if(pos==-1):
         print("application/octet-stream")
    else:
        after = name[pos + 1:].lower()
        if(after=="gif"  or after=="png"):
            print("image/"+after)
        elif(after=="jpeg" or after=="jpg"):
            print("image/jpeg")
        elif(after=="txt"):
            print("text/plain")
        elif(after=="pdf"):
            print("application/pdf")
        elif(after=="zip"):
            print("application/zip")
        else:
            print("application/octet-stream")
def main():
    name = input("input name").strip()
    f(name)

main()
