from collections import deque

def knight_moves(start, dest):
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    start = (ord(start[0]) - ord('a'), int(start[1]) - 1)
    dest = (ord(dest[0]) - ord('a'), int(dest[1]) - 1)
    queue = deque([(start, 0)])
    visited = set()

    while queue:
        (x, y), steps = queue.popleft()
        if (x, y) == dest:
            return steps
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                queue.append(((nx, ny), steps + 1))

T = int(input())
results = []
for _ in range(T):
    start, dest = input().split()
    results.append(knight_moves(start, dest))

print(*results, sep="\n")
