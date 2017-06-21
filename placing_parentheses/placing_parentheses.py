# Uses python3
import numpy as np

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    dataset = list(dataset)

    if len(dataset) % 2 != 1:
        return False

    n = int((len(dataset) + 1)/2)
    data_ops = dataset[1::2]
    data_values = list(map(float, dataset[0::2]))
    minMatrix = np.zeros((n,n))
    maxMatrix = np.zeros((n,n))

    #if there is only one number in the sub-expression,
    #min and max are the same
    for i in range(0, n):
        minMatrix[i,i] = data_values[i]
        maxMatrix[i,i] = data_values[i]

    #now expand min and max matrices step-wise
    for s in range(1, n ):
        for i in range(0, n-s):
            j = i + s
            minim = np.inf
            maxim = -np.inf
            for k in range(i, j):
                a = evalt(maxMatrix[i,k], maxMatrix[k+1, j], data_ops[k])
                b = evalt(maxMatrix[i,k], minMatrix[k+1, j], data_ops[k])
                c = evalt(minMatrix[i,k], maxMatrix[k+1, j], data_ops[k])
                d = evalt(minMatrix[i,k], minMatrix[k+1, j], data_ops[k])
                minim = min(minim, a, b, c, d)
                maxim = max(maxim, a, b, c, d)

            minMatrix[i,j], maxMatrix[i,j] = minim, maxim

    #write your code here
    return int(maxMatrix[0, n-1])

if __name__ == "__main__":
    print(get_maximum_value(input()))
