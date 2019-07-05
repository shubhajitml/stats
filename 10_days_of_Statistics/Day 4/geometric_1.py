def g(n,p): return ((1-p)** (n-1) * p
nr, dr = list(map(int, input().split(" ")))
n = int(input())
p = nr/dr
print(f"{g(n,p):.3f}")