'''
#一种叫做list的数据结构 使用中括号
studnets = ["alice","bob","cindy"]
for student in studnets:
    print(student)
for i in range(len(studnets)):
    print(studnets[i])

#一种叫做dictionary dict的数据
studnets = {
    "alice":"girl",
    "bob":"boy",
    "cindy":"girl",
    "david":"boy",
    "frank":"robot",
    }

for stu in studnets:
    print(stu,studnets[stu],sep=" sex->")
'''


#将字典和list组合起来
students = [
    {"name":"alice","sex":"girl","age":"12"},
    {"name":"bob","sex":"boy","age":"23"},
    {"name":"cindy","sex":"girl","age":"19"},
]
for stu in students:
    print(stu["name"],stu["sex"],stu["age"],sep="  ")