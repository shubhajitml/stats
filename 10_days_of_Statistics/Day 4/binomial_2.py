def fact(k): return 1 if k==0 else k*fact(k-1)

def combination(n, x): return fact(n)/ (fact(n-x) * fact(x))

def b(x, n, p):
    """
    x: The number of successes to be observed
    n: The total number of trials
    p: The probability of success of 1 trial
    q: The probability of failure of 1 trial
    """
    return combination(n, x) * (p**x) * ( (1-p) ** (n-x))

p, n = list(map(int, input().split(" ")))
p = p/100

print(f"{sum([b(i, n, p) for i in range(2+1)]):.3f}")
print(f"{sum([b(i, n, p) for i in range(2,n+1)]):.3f}")
