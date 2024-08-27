import sys
from pyfiglet import Figlet
import random
def main():
    fonts = Figlet().getFonts()
    if len(sys.argv)==1:
        Font = random.choice(fonts)
    elif len(sys.argv)==3:
        if sys.argv[1]=="-f" and sys.argv[2] in fonts :
            Font = sys.argv[2]
        else:
            sys.exit("Invalid arguments")

    else:
        sys.exit("Invalid Arguments")
    text = input()
    print("Output:\n",Figlet(font = Font).renderText(text))

if __name__=="__main__":
    main()
