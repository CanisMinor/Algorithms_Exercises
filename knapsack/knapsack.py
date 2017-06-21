# Uses python3
import sys
import numpy as np

def optimal_weight(W, w):
    n = len(w)
    valueMatrix = np.zeros((n,W))

    for i in range(1, n + 1):
        for weight in range(1, W + 1):
            valueMatrix[weight,i] = valueMatrix[weight, i-1]
            if w[i] <= weight:
                print('yay')




if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
