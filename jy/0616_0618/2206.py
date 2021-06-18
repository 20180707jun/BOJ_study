import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

li = [list(map(int, list(input()[:-1]))) for _ in range(N)]
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
visit = [[[False]*2 for _ in range(M)] for _ in range(N)]
visit[0][0][0] = True
visit[0][0][1] = True
q = deque([[0, 0, 1, 0]]) # x, y, cnt, breaked
while q:
    x, y, cnt, breaked = q.popleft()
    if (x, y) == (N-1, M-1):
        print(cnt)
        exit()
    for i, j in d:
        a = x + i
        b = y + j
        if 0<=a<N and 0<=b<M and visit[a][b][breaked]==False:
            if li[a][b]==0:
                visit[a][b][breaked] = True
                q.append([a, b, cnt+1, breaked])
            elif breaked==0:
                visit[a][b][breaked] = True
                q.append([a, b, cnt+1, 1])
        
print(-1)

# 8 8
# 01000100
# 01010100
# 01010100
# 01010100
# 01010100
# 01010100
# 01010100
# 00010100