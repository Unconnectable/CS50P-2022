import re

def main():
    print("True" if validate(input("IPv4 Address: ")) else "False")

def check(x):
    return 0 <= x <= 255

def validate(ip):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.search(pattern, ip)
    if match:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        num3 = int(match.group(3))
        num4 = int(match.group(4))
        if check(num1) and check(num2) and check(num3) and check(num4):
            return True
    return False

if __name__ == "__main__":
    main()
