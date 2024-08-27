def main():
    user_input = input("What is the answer ").strip().lower()  # 去除前后空格并转换为小写
    str_1 = "forty-two"
    str_2 = "forty two"
    if user_input == "42" or user_input == str_1 or user_input == str_2:
        print("Yes")
    else:
        print("No")

main()
