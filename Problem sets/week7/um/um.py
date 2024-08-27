import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    ans=0
    ans  =int(ans)
    s = s.lower().strip()
    pattern = r"\bum\b"

    for m in re.finditer(pattern,s,re.IGNORECASE):
        ans+=1

    return ans
    #return len(re.finditer(pattern,s,re.IGNORECASE))

    #return len(re.findall(pattern, s, re.IGNORECASE))

if __name__ == "__main__":
    main()
