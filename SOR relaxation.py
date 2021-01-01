## Method 2 WITH LESS NUMPY
def sor(a,x,b,w):
    # initialising a vector to store values. 
    y = np.zeros(len(a))
#     y = 1/a11( b - sum of (a,x) for i!=j)

    for i in range(len(a)):
        y[i] = b[i]
#         Two for loop just to skip the multiplication of a,x where i=j.
        for j in range(i):  ## from 0 to i-1
            y[i] -= a[i][j]*y[j]
        for k in range(i+1,len(a)): ## from i+1 to n
            y[i] -= a[i][k]*x[k]
#             Dividing by diagonal element
        y[i] = y[i]*w/a[i][i]
        y[i] = y[i] + (1-w)*x[i]
    return y

a = [[4, 1, 2],[3, 5, 1],[1, 1, 3]] ## matrix
b = [4,7,3] 
x = [0, 0, 0]  ## initial guess
r = 1 ## tolerance error
w = 1.5
eps = 10**-10
it = 0
while r >=eps:
    r = np.sum(np.square(np.array(b) - np.dot(a,x))) ## tolreance erro
    y = sor(a, x, b, w)
    #print each time the updated solution 
    it+=1
    x = y
print(f"No of iteration taken : {it}")
print(f"Solution is :{y}")
