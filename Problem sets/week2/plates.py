def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def f(s):
    num = "0123456789"
    if not (2 <= len(s) <= 6):
        return False
    for i in range(len(s)):
        if s[i] in num:
            return i  # 返回第一个找到的数字字符
    return -1  # 如果未找到数字，可以返回 None 或其他指示

def is_valid(s):
    if not s.isalnum():  # 检查是否只包含字母和数字
        return False
    if not (2<=len(s)<=6):
        return False
    if s[:2].isalpha():
        pos = f(s)
        if(pos!=-1):
            if(s[pos]!="0"):
                if(s[pos:].isdigit()):
                    return True
        else:
            return True
    else:
        return False
main()
