# Enter your code here. Read input from STDIN. Print output to STDOUT
nr, dr = list(map(int, input().split(" ")))
n = int(input())
p = nr/dr
print(round(1 - (1 - (p))**n, 3))
