from numpy import array, zeros, fabs
a=array([[1,3,-6,-1],
       [4,8,7,3],
       [2,3,4,5],
       [-9,6,3,2]],float)
b=array([2,4,5,7],float)
n = len(b)
x = zeros(n, float)

# Elimination step
for k in range(n-1):
    for i in range(k+1,n):
        if a[i,k] == 0 : continue
        factor = a[k,k]/a[i,k]
        
        for j in range (k,n):
            a[i,j]=a[k,j]-a[i,j]*factor
            
        b[i]=b[k]-b[i]*factor
        
print(factor)
print(a)

# Back substitution

x[n-1]=b[n-1]/a[n-1,n-1]
for i in range(n-2,-1,-1):
    sumx=0
    for j in range(i+1,n):
        sumx += a[i,j]*x[j]
    x[i]=(b[i]-sumx)/a[i,i]
print(x)
