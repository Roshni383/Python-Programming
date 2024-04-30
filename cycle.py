def has_cycle(graph):
    visited = set()
    stack = set()

    def dfs(node):

visited.add(node)
stack.add(node)

for neighbor in graph[node]:
    if neighbor not in visited:
        if dfs(neighbor):
            return True
elif neighbor in stack:
return True

stack.remove(node)
return False

for node in graph:
    if node not in visited:
        if dfs(node):
            return True
return False
graph = {'A': ['B', 'C'], 'B': ['C'], 'C': ['A']}
print(has_cycle(graph))
graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
print(has_cycle(graph))