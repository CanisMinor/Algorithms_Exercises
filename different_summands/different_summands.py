# Uses python3
import sys

def optimal_summands(n):
    summands = []

    remaining_n = n
    i = 1
    while remaining_n > 0:
        if i < remaining_n - i:
            summands.append(i)
            remaining_n = remaining_n - i
            i = i+1
        else:
            summands.append(remaining_n)
            remaining_n = 0
            
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
