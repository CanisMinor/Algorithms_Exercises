# Uses python3
import sys

def get_change(n):
    coins = [10,5,1]
    n_coins = 0
    for coin in coins:
        n_div = int(n // coin)
        if n_div > 0:
            n_coins += n_div
            n -= n_div * coin 
        
    return n_coins

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))
