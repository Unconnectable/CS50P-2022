def main():
    name = input("Input: ")
    #positions = [i for i, char in enumerate(name) if char.isupper()]
    result = shorten(name)
    print(f"Output: {result}")

def shorten(name):
    quitt = "aeiouAEIOU"
    result = "".join([i for i  in name if i not in quitt])
    return result

if __name__ == "__main__":
    main()
