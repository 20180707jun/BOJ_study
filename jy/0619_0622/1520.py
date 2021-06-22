import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

M, N = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(M)]

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

dp = [[None]*N for _ in range(M)]
dp[0][0] = 1

def get_ans(x, y):
    global li
    global d
    if dp[x][y]!=None:
        return dp[x][y]
    else:
        dp[x][y] = 0
        for i, j in d:
            a = x+i
            b = y+j
            if 0<=a<M and 0<=b<N and li[a][b]>li[x][y]:
                dp[x][y] += get_ans(a, b)
        return dp[x][y]


print(get_ans(M-1, N-1))