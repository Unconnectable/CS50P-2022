import random

def game(prompt):
    while True:
        try:
            level = int(input(prompt))
            if level >0:
                return level
            else:
                raise ValueError
        except ValueError:
            pass

def main():
    level = game("Level: ")
    num = random.randint(1,level)
    while True:
        try:
            guess = int(input("Guess: "))
            if(guess==num):
                print("Just right!")
                break
            elif(guess<num):
                print("Too small!")
            else:
                print("Too large!")
        except ValueError:
            pass
if __name__=="__main__":
    main()
