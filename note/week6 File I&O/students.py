
#1.超级朴素版本处理文件
'''
students = []
with open("studnets.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        #name,location = line.rstrip().split(",")\
        student = {"name":row[0],"house":row[1]}
        students.append(student)
        #print(f"{row[0]} is in {row[1]}")
def cmp(student):
    return student["house"]

#for stu in sorted(students,key = cmp,reverse=True):
#    print(f"{stu['name']} is in {stu['house']}") 
#另一种写法
for stu in sorted(students,key = lambda student:student["name"] ):
    print(f"{stu['name']} is in {stu['house']}") 


'''

#全新版本 我们CSV屌爆了!
'''

import csv
students = []
with open("studnets.csv") as file:
    reader = csv.DictReader((file))
    for row in reader:
        students.append({"name":row["name"],"home":row["home"]})

def cmp(student):
    return student["house"]
for stu in sorted(students,key = lambda student:student["name"] ):
    print(f"{stu['name']} is in {stu['home']}") 

这是用到的CSV文件s
name,sex,home,
Xcode,G,American
Atom,G,American
Subline,B,American
Vscode,G,American
Bitcon,G,American
Tencent,B,China
NET_EASE,B,China
    
'''

#如何编写CSV文件

import csv

name = input("name is: ")
home = input("home is: ")

with open("students.csv", "a") as file:  # a: append
    w = csv.DictWriter(file,fieldnames=["name","home"])
    w.writerow([name, home])
