import re
#弱化版
'''

name = input("Input name: ").strip()
if "," in name:
    last,first = name.split(",")
    name = f"{first} {last}"
print(f"hello,{name}")

'''
#强力版使用re正则表达式进行匹配 
name = input("Input name: ").strip()

matches = re.search(r"^(.+), *(.+)$", name)
#matches = re.search(r"^(.+), (.+)$", name)
if matches:= re.search(r"^(.+), *(.+)$", name):
    #海象操作符  walrus operator
    name = matches.group(2) + " "+ matches.group(1)
    #first,last = matches.group()
    #name = f"{first} {last}"
print(f"hello {name}")