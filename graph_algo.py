
from collections import deque

def execute_action(item):
    print(item)

def bfs(g, name):
    search_q = deque()
    search_q += g[name]
    searchd = []

    while search_q:
        current = search_q.popleft()

        if not current in searchd:
            execute_action(current)
            search_q += g[current]
            searchd.append(current)




