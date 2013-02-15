def least_cost_path(G, start, dest, cost):
    todo = {start: 0}
    parent = {}
    visited = set()
    while todo and dest not in visited:
        (cur,c) = min(todo, key=todo.get)
        todo.pop(cur)
        visited.add(cur)
        for n in G.adj_to(cur):
            if n in visited: continue
            if n not in todo or ( c + cost((cur,n)) < todo[n] ):
                todo[n] = c + cost((cur,n))
                parent[n] = cur
    if dest in visited:
        path = []
        while start not in path:
            path.insert(0, parent[cur])
            cur = parent[cur]
        return path
    else:
        return None

