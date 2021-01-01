
import numpy as np
A=np.array([[9,55,63,54],[89,35,97,23],[34,76,5,19],[11,17,73,79]])
n=len(A)
U=A
L=np.zeros((n,n))
for k in range(0,n):
  for r in range(0,n):
    if k==r:
      L[r][k]=1
    if k<r:
      factor=U[r][k]/U[k][k]
      L[r][k]=factor
      for c in range(0,n):
        U[r][c]=U[r][c]-(factor*U[k][c])

print(L,U)
print(np.dot(L,U))
