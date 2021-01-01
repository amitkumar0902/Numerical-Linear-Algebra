# Cholesky Factorization

import numpy as np
from math import sqrt
from sklearn import datasets as d

def cholesky(A):
    L = [[0.0] * len(A) for _ in range(len(A))]
    
    for i, (Ai, Li) in enumerate(zip(A, L)):
        
        for j, Lj in enumerate(L[:i+1]):
            s = sum(Li[k] * Lj[k] for k in range(j))
            
            if (i == j):
                Li[j] = sqrt(Ai[i] - s)  
            else:
                Li[j] = (1.0 / Lj[j] * (Ai[j] - s))
    return L

if __name__ == "__main__":
    
    n= int(input("Enter size of square matrix"))
    
    # Generate Symmetric-Positive Definite 'nxn' Matrix with random values
    A=d.make_spd_matrix(n)
    
    # Compose Cholesky Factorization
    L = np.array(cholesky(A))
    
    print('\nSymmetric Positive Definite Matrix A=\n',np.array(A))
    print('\nCholesky Decomposition (A= L L.T)\n',L,'\n\n',L.T)
