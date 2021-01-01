a =array([[0,7,-1,3,1],
   [0,3,4,1,7],
   [6,2,0,2,-1],
   [2,1,2,0,2],
   [3,4,1,-2,1]],float)
b=array([5,7,2,3,4],float)
n=len(b)
x=zeros(n,float)

for k in range(n-1):
    if fabs(a[k,k]) <  1.0e-12:
        for i in range(k+1,n):
            if fabs(a[i,k]) > fabs(a[k,k]):
                a[[k,i]] = a[[i,k]]
                b[[k,i]] = b[[i,k]]
                break
    for i in range(k+1,n):
        if a[i,k] == 0 : continue
        factor = a[k,k]/a[i,k]
        for j in range (k,n):
            a[i,j]=a[k,j]-a[i,j]*factor
        b[i]=b[k]-b[i]*factor

print(a)
print(b)

x[n-1]=b[n-1]/a[n-1,n-1]
for i in range(n-2,-1,-1):
    sumx=0
    for j in range(i+1,n):
        sumx += a[i,j]*x[j]
    x[i]=(b[i]-sumx)/a[i,i]
print(x)
