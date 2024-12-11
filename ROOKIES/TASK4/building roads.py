def find(parent, city):
    if parent[city] != city:
        parent[city] = find(parent, parent[city])
    return parent[city]

def union(parent, rank, city1, city2):
    root1 = find(parent, city1)
    root2 = find(parent, city2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1

n, m = map(int, input().split())
parent = list(range(n + 1))
rank = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    union(parent, rank, a, b)

components = set(find(parent, city) for city in range(1, n + 1))
components = list(components)

new_roads = []
for i in range(1, len(components)):
    new_roads.append((components[i - 1], components[i]))
    union(parent, rank, components[i - 1], components[i])

print(len(new_roads))
for road in new_roads:
    print(*road)
