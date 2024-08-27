from emoji import emojize
def main():
    name = input("Input :")
    #emoji_name = emojize(name, use_aliases=True)
    emoji_name = emojize(name, language="alias")
    print(f"Output:{emoji_name}")

if __name__=="__main__":
    main()
