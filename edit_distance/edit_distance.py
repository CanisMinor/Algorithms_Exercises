# Uses python3
import numpy as np

def edit_distance(s, t):
    m = len(s)
    n = len(t)
    matrixD = np.zeros((m + 1, n + 1))

    matrixD[:,0] = range(0, m + 1)
    matrixD[0,:] = range(0, n + 1)

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            insertion = matrixD[i, j-1] + 1
            deletion = matrixD[i-1, j] + 1
            if s[i - 1] == t[j - 1]:
                match = matrixD[i-1, j-1]
                matrixD[i,j] = min(insertion, deletion, match)
            else:
                mismatch = matrixD[i-1, j-1] + 1
                matrixD[i,j] = min(insertion, deletion, mismatch)

    #write your code here
    return int(matrixD[m, n])


if __name__ == "__main__":
    print(edit_distance(input(), input()))
