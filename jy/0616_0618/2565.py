import sys
input = sys.stdin.readline

n = int(input())

li = [list(map(int, input().split())) for _ in range(n)]

li.sort(key=lambda x: x[0])
li = [li[i][1] for i in range(len(li))]
dp = [1]*len(li)
for i in range(len(li)):
    ma = 1
    for j in range(i):
        if li[j]<li[i]:
            ma = max(ma, dp[j]+1)
    dp[i] = ma
print(n-max(dp))

