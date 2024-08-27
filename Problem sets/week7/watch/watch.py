import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
    '''
    .   any character except a new line
    *   0 or more repetitions
    +   1 or more repetitions
    ?   0 or 1 repetition
    {m} m repetitions
    {m,n} m-n repetitions

    \d    decimal digit
    \D    not a decimal digit
    \s    whitespace characters
    \S    not a whitespace character
    \w    word character, as well as numbers and the underscore
    \W    not a word character

    <iframe width="560" height="315" src="https://cs50.harvard.edu/python"> </iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen> </iframe>
    r'<iframe.*?src="(https?:\/\/(?:www\.)?youtube\.com(?:\/embed)?\/[a-zA-z0-9_-]+)".*?',s,
    '''
    # 转义字符  /：\/
    # ?:非捕获组 不会加入 group中
    # .*贪婪匹配
    # .*非贪婪匹配
    pattern = r'<iframe.*?src="https?:\/\/(?:www\.)?youtube\.com(?:\/embed)?\/([a-zA-Z0-9_-]+)".*?'
    
    if match := re.search(pattern,s) :
        url = match.group(1)
        return (f"https://youtu.be/{url}")
    return None
if __name__ == "__main__":
    main()
