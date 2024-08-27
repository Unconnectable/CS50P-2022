import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r'<iframe.*?src="https?:\/\/(?:www\.)?youtube\.com(?:\/embed)?\/([a-zA-Z0-9_-]+)".*?'
    if match := re.search(pattern,s) :
        url = match.group(1)
        print(url)
if __name__ == "__main__":
    main()
