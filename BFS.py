d = {}

def add(key, value):
    if key not in d:
        d[key] = [value]
    else:
        d[key].append(value)
    if value not in d:
        d[value] = [key]
    else:
        d[value].append(key)

add(0, 1)
add(0, 2)
add(0, 4)
add(1, 4)
add(2, 3)
add(3, 4)

print(d)

def bfs(d, source):
    v = set()
    q = []
    q.append(source)
    v.add(source)
    while q:
        node = q.pop(0)
        print(node,end=" ")
        for neighbors in d.get(node,[]):
            if neighbors not in v:
                q.append(neighbors)
                v.add(neighbors)
    return v

a = bfs(d,0)
def dfs(d, source):
    v = set()
    q = []
    q.append(source)
    v.add(source)
    while q:
        node = q.pop()
        print(node,end=" ")
        for ns in d.get(node,[]):
            if ns not in v:
                q.append(ns)
                v.add(ns)
    return v
a=dfs(d,0)