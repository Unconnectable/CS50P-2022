import math
import re
'''
Begins with #
Composed of 5 characters
0-9 and A-F
'''
#FF0000 red
#00FF00 green
#0000FF blue
#000000 black
#FFFFFF white
#xxxxxx
#红绿蓝

def main():
    code = input("Input code: ")
    pattern = r"^#[a-fA-F0-9]{6}$"
    match = re.search(pattern,code)
    if match:
        print(f"Valid {match.group()}")
    else:
        print("Invalid")
main()