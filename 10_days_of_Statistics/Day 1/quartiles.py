def median(arr):
    arr = sorted(arr) # the array needs to be sorted before finding median
    if len(arr)%2 == 0:
        return int(sum(arr[len(arr)//2-1:len(arr)//2+1])/2)
    else:
        return arr[len(arr)//2]

def quartiles(N, X):
    Q2 = median(X)
    Q1 = median(X[:len(X)//2])
    if N%2 == 0:
        Q3 = median(X[len(X)//2:])
    else:
        Q3 = median(X[len(X)//2+1:])
    return Q1, Q2, Q3

N = int(input()) # no. of elements in each X and W
X = sorted([int(x) for x in input().split()])

Q1, Q2, Q3 = quartiles(N,X)
print(Q1)
print(Q2)
print(Q3)