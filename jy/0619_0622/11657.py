'''import sys

input = sys.stdin.readline

N, M = map(int, input().split())

g = [[float('inf')]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    if g[a][b] > c:
        g[a][b] = c

d = [float('inf')]*(N+1)
d[1] = 0
for b in range(1, N+1):
    d[b] = g[1][b]
for _ in range(N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if d[j] > d[i] + g[i][j]:
                d[j] = d[i] + g[i][j]
td = d[:]
for _ in range(N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if d[j] > d[i] + g[i][j]:
                d[j] = d[i] + g[i][j]
if td!=d:
    print(-1)
else:
    for i in d[2:]:
        if i==float('inf'):
            print(-1)
        else:
            print(i)

'''

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
e = list()
d = [float('inf')]*(N+1)
d[1] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    e.append((a, b, c))
    if a==1:
        d[b] = c

for i in range(1, N+1):
    for a, b, c in e:
        if d[b] > d[a]+c:
            d[b] = d[a]+c
td = d[:]
for i in range(1, N+1):
    for a, b, c in e:
        if d[b] > d[a]+c:
            d[b] = d[a]+c
if td!=d:
    print(-1)
else:
    for i in d[2:]:
        if i==float('inf'):
            print(-1)
        else:
            print(i)


