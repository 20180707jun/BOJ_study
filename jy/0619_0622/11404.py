import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
g = dict()
min_cost = [[float('inf')]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if c>min_cost[a][b]:
        continue
    g.setdefault(a, list())
    g[a].append((b, c))
    min_cost[a][b] = c

for i in range(1, n+1):
    min_cost[i][i] = 0

for j in range(1, n+1):
    for i in range(1, n+1):
        for k in range(1, n+1):
            if min_cost[i][k]>min_cost[i][j]+min_cost[j][k]:
                min_cost[i][k] = min_cost[i][j]+min_cost[j][k]

for i in range(1, n+1):
    for j in range(1, n+1):
        if min_cost[i][j]!=float('inf'):
            print(min_cost[i][j], end=' ')
        else:
            print(0, end=' ')
    print()
