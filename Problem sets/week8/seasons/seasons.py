from datetime import datetime, date
import sys
import inflect

def number_to_words(number):
    # Create an inflect engine
    p = inflect.engine()
    # Convert number to words
    return p.number_to_words(number)

def validate(s):
    try:
        # Parse the input date string to a datetime object
        s = datetime.strptime(s, "%Y-%m-%d").date()
        r = date.today()
        # Calculate the difference in minutes
        minutes = cal(s, r)

        # Convert the number of minutes to words
        words = number_to_words(minutes)
        words = words.capitalize()
        words = words.replace(" and ", " ")
        print(f"{words} minutes")

    except ValueError:
        sys.exit("Invalid date")

def cal(s, r):
    time_difference = r - s
    return int(time_difference.total_seconds() / 60)

def main():
    validate(input("Date of Birth (YYYY-MM-DD): "))

if __name__ == "__main__":
    main()
