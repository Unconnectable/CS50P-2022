def convert(time):
    pos = time.find(":")
    num1 = int(time[0:pos])
    num2 = int(time[pos+1:])
    return num1+num2/60

def main():
    time = input("What time is it ? ").strip()
    number = convert(time)
    if 7 <= number <= 8:
        print("breakfast time")
    elif 12 <= number <= 13:
        print("lunch time")
    elif 18 <= number <= 19:
        print("dinner time")

if __name__=="__main__":
    main()
