def gauss_sidel(a,x,b):
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
        y[i] = y[i]/a[i][i]
    return y

a = [[4, 1, 2],[3, 5, 1],[1, 1, 3]] ## matrix
b = [4,7,3] 
x = [0, 0, 0]  ## initial guess
r = 1 ## tolerance error
eps = 10**-10
while r >=eps:
    r = np.sum(np.square(np.array(b) - np.dot(a,x))) ## tolreance erro
    y = gauss_sidel(a, x, b)
    #print each time the updated solution 
    print(y)
    x = y
