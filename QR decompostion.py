import numpy as np
from scipy.linalg import hilbert
import time
#-------------Computing the givens parameter---------

def GivensParam(x_i,x_j):
    
    if x_j==0:
        c,s=1,0
        
    elif abs(x_j)>abs(x_i):
        t=x_i/x_j
        s=1/np.sqrt(1+t**2)
        c=s*t
        
    elif abs(x_i)>abs(x_j):
        t=x_j/x_i
        c=1/np.sqrt(1+t**2)
        s=c*t
    return c,s


#----------------Product of a Givens Matrix J with a General Matrix A-----

def GivensMul(A,i,j,c,s):
    
    a=A[i,:]
    b=A[j,:]
    
    tmp1=np.copy(c*a+s*b)
    tmp2=np.copy(-s*a+c*b)
    A[i,:]=tmp1
    A[j,:]=tmp2
    
    return A


#------------------Givens QR Decomposition----------------------

def GivensQR(A):
    m,n=A.shape
    Q=np.eye(m)
    for i in range(min(m-1,n)):
        for j in range(i+1,m):
            c,s=GivensParam(A[i,i],A[j,i])   
            A=GivensMul(A,i,j,c,s)
            Q=GivensMul(Q,i,j,c,s)
    
    R=A
    Q=Q.T
    
    return Q,R
            





start_time=time.time()
H=hilbert(5)
Q,R=GivensQR(H)
print(Q)
print(R)
end_time=time.time()
print('Time taken in the  process',end_time-start_time)
