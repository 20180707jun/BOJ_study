import sys

input = sys.stdin.readline

N, K = map(int, input().split())

li = list(map(int, input().split()))
gap_li = list()
for i in range(len(li)-1):
    gap_li.append(li[i+1]-li[i])
gap_li.sort(reverse=True)
print(sum(gap_li[K-1:]))
