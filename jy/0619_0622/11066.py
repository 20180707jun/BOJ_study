import sys

def get_min_sum(s, e):
    global dp
    global cost
    if dp[s][e]:
        return dp[s][e]
    if s==e:
        dp[s][e]=0
        return cost[s][e]
    else:
        mi = float('inf')
        for i in range(s, e):
            mi = min(mi, get_min_sum(s, i)+get_min_sum(i+1, e))
        dp[s][e] = mi+cost[s][e]
        # dp[s][e] = mi+sum(li[i:j+1])
        return dp[s][e]

T = int(input())
for _ in range(T):
    K = int(input())
    li = list(map(int, input().split()))
    cost = [[None]*K for _ in range(K)]
    dp = [[None]*K for _ in range(K)]
    for i in range(K):
        for j in range(i, K):
            cost[i][j] = sum(li[i:j+1])
    for i in range(K):
        cost[i][i] = 0
    print(get_min_sum(0, K-1))


