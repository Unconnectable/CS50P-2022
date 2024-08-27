import random


def main():
    ...
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        right = x + y
        time = 1
        while True:
            ans = int(input(f"{x}+{y}= "))
            if ans == right:
                score+=1
                break
            elif time < 3:
                time += 1
                print("EEE")
                ans = input(f"{x} + {y} = ")
            else:
                print(f"{x} + {y} = {right}")
                break
    print("Score:",score)

def get_level():
    Levels = [1,2,3]
    while True:
        try:
            level = int(input("Level: "))
            if level not in Levels:
                raise ValueError
            else:
                return level
                break
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    return random.randint(10 ** (level - 1), 10**level - 1)

if __name__ == "__main__":
    main()
