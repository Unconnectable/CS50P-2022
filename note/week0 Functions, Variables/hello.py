
'''
everithing here is commments 
所有内容在这里都是注释
'''

name = input("what's your name ? ")

'''
#Hello To User
#print(*objects, sep='',end='\n',file=sys.stdout, flush=Falseend= '\n')
#print("hello, "+name)

把end 变成了???
#print("hello,",end='???')
#print(name)
'''

#print("hello,", name,sep="???")
#把分隔符变成了???
'''
#如何打印引号?
#case1 : print('hello,"name" ')把外面引号换成单引号
#case2 : print("hello,\"name\"")使用转义字符 
#case3 : print(f"hello,{name}")
print(f"hello,{name}")会打印    hello,{name}
而加上f之后会变成:               hello,name

name = name.strip()
# Remove whitespace from str 
删除字符串中的空白

name = name.capitalize()
# 将字符串的首字母大写

name = name.title()
# 将字符串的每个单词的首字母大写
'''
name = name.strip().title()#连用函数  先去除空格 再title
#甚至可以 name = input("what's your name ? ").strip().title()
first , last = name.split(" ")
print(f"hello,{first}")