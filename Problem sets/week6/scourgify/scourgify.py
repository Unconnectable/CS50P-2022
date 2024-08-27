import sys
import os
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")
    elif  not os.path.isfile(sys.argv[1]):
        sys.exit("Could not read invalid_file.csv")

    file_path1 = sys.argv[1]
    file_path2 = sys.argv[2]
    new_file(file_path1,file_path2)


def new_file(file_path1,file_path2):
    try:
        with open(file_path1,"r") as file1,open(file_path2,"w",newline='') as file2 :
            head__ = ["first","last","house"]
            reader = csv.DictReader(file1)
            writer  = csv.DictWriter(file2,fieldnames = head__)
            writer.writeheader()

            for line in reader:
                first,last = line["name"].strip().split(", ")
                house = line["house"]
                writer.writerow( {"first":last,"last":first,"house":house } )
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__=="__main__":
    main()
