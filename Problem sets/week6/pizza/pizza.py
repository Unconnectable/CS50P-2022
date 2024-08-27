import sys
import csv
from tabulate import tabulate
def process_csv(filename):
    try:
        with open(filename,"r") as file:
            lines = csv.reader(file)
            data = list(lines)
            table = tabulate(data,headers='firstrow',tablefmt='grid')
            print(table)
    except FileExistsError:
        sys.exit("File does not exist")


def main():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    file_path = sys.argv[1]
    process_csv(file_path)

if __name__ == "__main__":
    main()
