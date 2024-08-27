import re
locations = {"+1":"American", "+62":"Indonesia","+505":"Nicaragua"}
def main():
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    # ?P<...> 是一个命名捕获组的语法，用于给捕获组指定一个名称。

    #+505 617-495-1000
    #[1,3] 3   3   4
    num = input("Phone number is: ")
    match = re.search(pattern, num)
    if match:
        country_code = match.group("country_code")
        print(locations[country_code])
    else:
        print("Invalid")

main()