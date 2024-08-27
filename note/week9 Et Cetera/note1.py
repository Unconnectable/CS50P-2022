import argparse
parser = argparse.ArgumentParser(description="THIS IS DESCRIPTION")
parser.add_argument("-n",default=1,help="n is times to print",type=int)
argument = parser.parse_args()

for _ in range(argument.n):
    print("moew")