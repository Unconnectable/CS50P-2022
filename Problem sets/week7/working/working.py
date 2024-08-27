import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^(\d{1,2}):?(\d{0,2})? (AM|PM) to (\d{1,2}):?(\d{0,2})? (AM|PM)$"

    match = re.search(pattern, s, re.IGNORECASE)
    if not match:
        raise ValueError

    time1, time2, ch1, time3, time4, ch2 = match.groups()

    time1 = int(time1)
    time2 = int(time2) if time2 else 0
    time3 = int(time3)
    time4 = int(time4) if time4 else 0

    try:
        if time1 > 12 or time2 > 59 or time3 > 12 or time4 > 59:
            raise ValueError
        if ch1.upper() == "PM" and time1 != 12:
            time1 += 12
        elif ch1.upper() == "AM" and time1 == 12:
            time1 = 0

        if ch2.upper() == "PM" and time3 != 12:
            time3 += 12
        elif ch2.upper() == "AM" and time3 == 12:
            time3 = 0

        time1_str = f"{time1:02}:{time2:02}"
        time2_str = f"{time3:02}:{time4:02}"
        return f"{time1_str} to {time2_str}"
    except ValueError:
        raise ValueError

if __name__ == "__main__":
    main()
