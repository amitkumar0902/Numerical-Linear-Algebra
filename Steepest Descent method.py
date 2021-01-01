import numpy as np
from numpy.linalg import multi_dot,norm
from sklearn import datasets as d

#for N=2
n=2
A = d.make_spd_matrix(n)
A= np.array(A)

# while changing n change dimenstion og b and x0 also


b = np.array([(1, 2)]).T

#start point
x0 = np.array([(0, 0)]).T  

print(A)

def gradient(b,A,x):
    grad= (A @ x) -b 
    return grad

xn=[ ]                        #creating list of points
dire = (- gradient(b,A,x0))   # negative gradient direction 
r = b - (A @ x0)              #residual part (negative gradient)

#note: in optimization we take alpha pdation as
# alpha = -(grad.T @ direction / direction.T @ Q @ direction)
# here we are just taking minus sign in  i.e(- grad.T ==  residual//(r)) 


xn.append(x0)
alpha=[ ]
iteration=0
eps = 10 **-3

while ( norm(r,2) > eps):    
    
    alpha.append((r.T @ dire)/(dire.T @ A @ dire))    # alpha updation        
    
    xn.append(xn[-1] + (alpha[-1] * dire))      #updating x value (closer to minimizer)
    
    dire= (- gradient(b,A,xn[-1]))              # updating direction from updated minimizer 
    
    r= b - (A @ xn[-1])     
    
    if (norm(dire,2)==0):                      #if gradient at point equals to 0 we stop
        break
    iteration += 1

  
print("final minimizer will be ")
print(" ")
print(xn[-1])
print(" ")
print("no. of iteration required ")
print(iteration)

#to view all the updation in X value

for i in xn:
    print("  ")
    print(i)
