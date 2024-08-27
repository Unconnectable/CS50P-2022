def main():
    months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        name = input("Date: ")
        if(len(name.split("/")) ==3 ):
            name = name.split("/")
            try:
                mon,day,year=map(int,name)
                if 1 <= mon <= 12 and 1 <= day <= 31:
                    print(f"{year:04d}-{mon:02d}-{day:02d}")
                    break
            except ValueError:
                pass
        else:
            #December 80, 1980
            name= name.split(",")
            if(len(name)==2 ):
                try:
                    month,day = name[0].split()
                    month = months.index(month)+1
                    day,year=int(day),int(name[1])
                    if 1 <= month <= 12 and 1 <= day <= 31:
                        print(f"{year:04d}-{month:02d}-{day:02d}")
                        break
                except ValueError:
                    pass
if __name__ =="__main__":
    main()
