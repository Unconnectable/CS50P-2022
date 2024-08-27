import requests
import sys
def main():
    try:
        n = float(sys.argv[1])
    except IndexError:
        print("Missing command-line argument")
    except ValueError:
        print("Missing command-line argument")
    price(n)

def price(n):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        #print(response.json())
        current_price = data["bpi"]["USD"]["rate_float"]
        bit_price = float(data["bpi"]["USD"]["rate_float"])
    except requests.RequestException:
        sys.exit()
    print(f"${n * bit_price:,.4f}")
if __name__=="__main__":
    main()
