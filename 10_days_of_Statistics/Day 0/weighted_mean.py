N = int(input()) # no. of elements in each X and W
X = [int(x) for x in input().split()]
W = [int(w) for w in input().split()]

def weighted_mean(N, array, weights):
    sum_nr = 0
    for i in range(N):
        sum_nr += array[i] * weights[i]
    return sum_nr/sum(weights)

print(f'{weighted_mean(N,X,W):.1f}')