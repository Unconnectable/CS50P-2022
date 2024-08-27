
'''
i = 1
while(i<=3):
    print("meow")
    i+=1

for i in[0,1,2]:
    print("meow")
#以上两种一模一样
'''
print( "meow\n" * 3,end="")
#输出三次 moew

while True:
    n = int(input("What is n? "))
    if n>0:
        break
for _ in range(n):
    print("meow")

