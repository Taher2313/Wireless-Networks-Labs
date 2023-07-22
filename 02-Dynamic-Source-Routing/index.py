# Name: Taher Mohamed Ahmed
# Sec: 1
# BN: 37

from collections import deque

n, m = map(int, input().split())

# build adjacency list for the graph
adj_list = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)
    adj_list[u].sort()
    adj_list[v].sort()

# source and destination vertices
src, dest = map(int, input().split())

# initialize route discovery process
visited = [False] * (n+1)
parent = [-1] * (n+1)
route = [[] for _ in range(n+1)]
route[src] = [src]
queue = deque([src])

while queue:

    curr = queue.popleft()

    if curr == dest:
        continue

    visited[curr] = True

    for neighbor in adj_list[curr]:
        if neighbor not in route[curr]:
            # update only if the new route is shorter than the previous one or smaller lexicographically
            new_route = route[curr] + [neighbor]

            if  route[neighbor] == [] or len(new_route) < len(route[neighbor]):
                parent[neighbor] = curr
                route[neighbor] = route[curr] + [neighbor]
                queue.append(neighbor)

# output the route forwarded in RREQ for each vertex

if src == dest:
    for i in range(1, n+1):
        print(-1)
else:
    for i in range(1, n+1):
        if i == src:
            print(route[src][0])
        elif not visited[i] or i == dest:
            print(-1)
        else:
            print(" ".join(map(str, route[i])))