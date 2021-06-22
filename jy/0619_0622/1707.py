from collections import deque
import sys

input = sys.stdin.readline

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    g = dict()
    for _ in range(E):
        a, b = map(int, input().split())
        g.setdefault(a, set())
        g.setdefault(b, set())
        g[a].add(b)
        g[b].add(a)
    lvisit = [False]*(V+1)
    rvisit = [False]*(V+1)

    all_break = False
    ans = 'YES'
    for snode in range(1, V+1):
        g.setdefault(snode, set())
        if lvisit[snode]==True or rvisit[snode]==True:
            continue
        q = deque([[snode, False], ]) # False : l, True : r
        
        lvisit[snode] = True
        while q:
            node, is_right = q.popleft()
            
            for nnode in g[node]:
                if is_right==True and lvisit[nnode]==False:
                    lvisit[nnode] = True
                    if lvisit[node]==True and rvisit[node]==True:
                        all_break = True
                        ans = 'NO'
                        break
                    q.append([nnode, False])
                elif is_right==False and rvisit[nnode]==False:
                    rvisit[nnode] = True
                    if lvisit[node]==True and rvisit[node]==True:
                        all_break = True
                        ans = 'NO'
                        break
                    q.append([nnode, True])
            if all_break:
                break
    print(ans)
            
                    
        
        

        
        
