def SOR(X,y,x,tol,numiter,w):
    A=np.copy(X)
    b=np.copy(y)
    D=np.diagflat(np.diag(A))
    U= np.triu(A, k=1)
    L=np.tril(A,k=-1)
    
    for i in range(numiter):
        
        x=np.linalg.inv(D+L*w).dot(w*b+((1-w)*D-w*U).dot(x))
        
        if (np.linalg.norm(b-A.dot(x))/np.linalg.norm(b))<tol:
            solution=x
            iteration=i+1
            return solution,iteration
    solution=x
    return solution,maxiter

# A = np.array([[5.0,-1.0,2.0],[-1.0,4.0,1.0],[1.0,6.0,7.0]])
# b = np.array([[1.0],[-2.0],[5.0]])
# x0 = np.array([[0.0],[0.0],[0.0]])

A = np.array([[2.0,1.0],[5.0,7.0]],dtype=float)
b = np.array([[11.0],[13.0]],dtype=float)
x0= np.array([[0.0],[0.0]],dtype=float)

solution,iterations = SOR(A,b,x0,1e-3,25,1.2)
print("Solution is:\n",solution)
print("Iterations to converge:",iterations)
