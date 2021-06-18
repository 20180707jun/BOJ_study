import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

visit = [[[False]*M for _ in range(N)] for _ in range(H)]
d = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]

tomatos = list()
for _ in range(H):
    floor = [list(map(int, input().split())) for _ in range(N)]
    tomatos.append(floor)
t_cor = list()
z_cnt = 0
for x in range(M):
    for y in range(N):
        for z in range(H):
            if tomatos[z][y][x]==1:
                t_cor.append((z,y, x))
                visit[z][y][x] = True
            if tomatos[z][y][x]==0:
                z_cnt += 1

day = -1
while t_cor:
    q = deque(t_cor)
    t_cor = list()
    while q:
        z, y, x = q.popleft()
        for c, b, a in d:
            next_z = z+c
            next_y = y+b
            next_x = x+a
            if 0<=next_z<H and 0<=next_y<N and 0<=next_x<M \
            and tomatos[next_z][next_y][next_x] == 0 \
            and visit[next_z][next_y][next_x]==False:
                z_cnt -= 1
                visit[next_z][next_y][next_x] = True
                t_cor.append((next_z,next_y,next_x))
    day += 1
if z_cnt==0:
    print(day)
else:
    print(-1)            

