import numpy as np
import math

def cholesky_decomposition(in_matrix):
    (rows, cols) = in_matrix.shape

    if (rows != cols):
        return None

    out_matrix = np.matrix(np.zeros((rows, cols)))

    L00 = math.sqrt(in_matrix[0,0])

    out_matrix[0,0] = L00

    if (rows == 2):
        L10 = in_matrix[1,0] / L00
        out_matrix[1,0] = L10
        out_matrix[1,1] = math.sqrt(in_matrix[1,1] - (L10 * L10))
        #LLT = out_matrix * out_matrix.T
        return out_matrix
    else:
        L10 = in_matrix[1:,0] / L00
        out_matrix[1:,0] = L10
        L10L10_T = np.outer(L10, L10)
        out_matrix[1:,1:] = cholesky_decomposition(in_matrix[1:,1:] - L10L10_T)
        return out_matrix



matrix1 = np.matrix('25 15 -5; 15 18 0; -5 0 11')
Lmat = cholesky_decomposition(matrix1)
test1 = Lmat * Lmat.T
print(Lmat)

#print(math.sqrt(2))
#print(math.sqrt(1/2))
#print(math.sqrt(3/2))
#print(1/math.sqrt(3))

print(test1)