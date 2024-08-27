#1.
'''
name = input("Name is: ")
#file = open("names.txt","w") 如果使用write 会导致覆盖写入的文件

file = open("names.txt","a")
file.write(f"{name}\n")
file.close()
#带换行符写入name

with open("names.txt","a") as file
   file.write(f"{name}\n") 省去了file.close()
'''
#2.读取name and print them
'''
with open("names.txt","r") as file:
    for line in file:
        print(line.rstrip())
'''

#3.
from matplotlib.pylab import f


names = []  #an empty list
with open("names.txt","r") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f"Hello,{name}")