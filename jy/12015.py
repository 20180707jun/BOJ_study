N = int(input())
li = list(map(int, input().split()))

dp = [10**6+1]*(N+1)
last = 0
for i in li:
    s, e = 0, last
    while s<e:
        m = (s+e)//2
        if dp[m]>=i:
            e = (s+e)//2
        else:
            s = (s+e)//2 + 1
    if dp[s]==10**6+1:
        last += 1
    dp[s] = i
for i in range(N):
    if dp[i]==10**6+1:
        print(i)
        exit()
print(N)

