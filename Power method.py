import numpy as np
matrix=np.array([[2,0,0],[0,2,0],[0,0,1]])
matrix.shape
def power():
    x0=np.array([1,1,1])
    tol=10**-5
    for i in range(20):
        Xk=np.dot(matrix,x0)
        Xk=Xk/np.linalg.norm(Xk)
        eigen=np.dot(np.dot(Xk.T,matrix),Xk)
        error=np.linalg.norm(np.dot(matrix,Xk)-eigen*Xk)
        if(error<tol):
            return i,eigen
        x0=Xk
    return i,eigen
    
i,b=power()
print(i,b)
