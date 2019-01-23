N = int(input()) # no of elements
X = [int(x) for x in input().split()] # given array
mean = sum(X)/N
variance = sum([((x - mean) ** 2) for x in X]) / N
stddev = variance ** 0.5
print(f"{stddev:.1f}")