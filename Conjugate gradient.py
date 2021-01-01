import numpy as np
from numpy import linalg as LA

def conjugate_gradient(A, b, x, tolerance, numiter):
    r_prev = b - (A @ x)
    p = r_prev

    for i in range(numiter):
        alpha = (r_prev.T @ r_prev) / (p.T @ A @ p)
        x = x + alpha * p
        r_curr = r_prev - alpha * A @ p
        
        if LA.norm(r_curr, 2) < tolerance:
            return x, i+1
        
        beta = (r_curr.T @ r_curr) / (r_prev.T @ r_prev)
        p = r_curr + beta * p
        r_prev = r_curr
    
    return x, -1
  

# example
A = np.array([(-9, 1, 1), (-2, 8, 1), (1, 15, 6)])
b = np.array([(1, 2, 3)]).T
x_0 = np.array([(0, 0, 0)]).T

x, iteration = conjugate_gradient(A, b, x_0, 1.0e-6, 10)

print("x =")
print(x)

print(f"\nSolution obtained at iteration {iteration}.")
