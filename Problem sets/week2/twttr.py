def main():
    quitt = "aeiouAEIOU"
    name = input("Input: ")
    #positions = [i for i, char in enumerate(name) if char.isupper()]
    result = "".join([i for i  in name if i not in quitt])
    print("Output: "+result)
if __name__ == "__main__":
    main()
