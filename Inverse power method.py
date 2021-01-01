matrix=np.array([[1,3,0],[2,5,1],[-1,2,3]])
matrix.shape


def inversepower():
    x0=np.array([1,1,1])
    tol=10**-3
    inverse=np.linalg.inv(matrix)
    for i in range(10):
        Xk=np.dot(inverse,x0)
        Xk=Xk/np.linalg.norm(Xk)
        eigen=(np.dot(np.dot(Xk.T,inverse),Xk))/(np.dot(Xk.T,Xk))
        error=np.linalg.norm(np.dot(matrix,Xk)-eigen*Xk)
        if(error<tol):
            return i,1/eigen
        x0=Xk
    return i,1/eigen

i,v=inversepower()
print(i,v)
