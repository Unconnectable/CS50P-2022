import re
url = input("URL: ").strip()


#username = url.removeprefix("https://twitter.com/")
#使用正则表达式
'''
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)
print(f"Username: {username}")
'''
matches  = re.match(r"^https?://(www\.)?twitter\.com/(.+)$",url,re.IGNORECASE)
if matches:
    print(f"Username: ",matches.group(2))