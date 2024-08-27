def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    #str.replace(old, new, count=-1) 第三个参数不填写就是所有
    d = float(d.replace(d[0],' ',1) )
    #d = float(s[1:])
    return d


def percent_to_float(p):
    # TODO
    p = float(p[:-1])
    return float(p/100)


main()
