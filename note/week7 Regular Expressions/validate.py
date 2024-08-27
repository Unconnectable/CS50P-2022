import re
email = input("Input email: ").strip()
#username,domain = email.split("@")

'''
if username and domain.endswith(".edu") :
    print("Valid")
else:
    print("Invalid")
'''
'''
#以下两种相同  \w 包含了0-9 a-z A-Z 还有一些符号
#if re.search(r"^[^@]+@[^@]+\.edu$", email):
#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):

.   any character except a new line
*   0 or more repetitions
+   1 or more repetitions
?   0 or 1 repetition
{m} m repetitions
{m,n} m-n repetitions

\d    decimal digit
\D    not a decimal digit
\s    whitespace characters
\S    not a whitespace character
\w    word character, as well as numbers and the underscore
\W    not a word character


'''

if re.search(r"^(\w|\.)+@(\w+\.)*\w+\.edu$", email,re.IGNORECASE):
    print("Valid")
#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    # .+ =..* 
    print("Valid")
else:
    print("Invalid")