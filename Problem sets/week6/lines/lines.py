import sys
import os

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

def rid_file(filepath):
    try:
        with open(filepath,'r') as file:
            lines = file.readlines()
            #readlines读取所有行

    except FileNotFoundError:
        sys.exit("File does not exist")

    count = 0
    for line in lines:
        line = line.strip()
        #去除两头的空字符
        if line and not line.startswith('#'):
            count+=1
    return count

def main():
    filepath = sys.argv[1]
    ans  = rid_file(filepath)
    print(ans)

if __name__=="__main__":
    main()
