# int 
'''
x = int(input("what is x "))
y = int(input("what is y "))
print(x+y) 
'''
#float
x = float(input("what is x "))
y = float(input("what is y "))
'''
z = round(x+y)#默认四舍五入到整数
print(f"{z:,}")#每三位加一个逗号分隔
'''
z = round(x/y,2)#小数点后两位
#如果不使用round 
print(f"{z:.2f}") #四舍五入小数点后两位
#   round(number[, ndigits])