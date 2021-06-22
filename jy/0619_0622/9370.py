import sys
import heapq
input = sys.stdin.readline

T = int(input())

def get_path(dest, path):
    ret = ''
    while path[dest]!=dest:
        ret += str(dest)
        dest = path[dest]
    ret += str(dest)
    return ret
    

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = dict()
    for i in range(n+1):
        graph.setdefault(i, list())
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    dests = list()
    for _ in range(t):
        t = int(input())
        dests.append(t)
    hq = list()
    d = [float('inf')]*(n+1)
    d[s] = 0
    path = list(range(n+1))
    path[s] = s

    for node, cost in graph[s]:
        d[node] = cost
        heapq.heappush(hq, (cost, node))
        path[node] = s

    while hq:
        cost, node = heapq.heappop(hq)
        for nnode, ncost in graph[node]:
            if d[nnode]> cost+ncost:
                d[nnode] = cost+cost
                path[nnode] = node
                heapq.heappush(hq, (d[nnode], nnode))

    ans_li = list()
    for dest in dests:
        ret_path = get_path(dest, path)
        if str(h)+str(g) in ret_path or str(g)+str(h) in ret_path:
            ans_li.append(dest)
    ans_li.sort()
    for ans in ans_li:
        print(ans, end=' ')
    print()
    

