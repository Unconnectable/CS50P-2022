import validators

def __vali(s):
    if validators.email(s):
        print("Valid")
    else:
        print("Invalid")
def main():
    __vali(input("What's your email address? "))
if __name__ == "__main__":
    main()
