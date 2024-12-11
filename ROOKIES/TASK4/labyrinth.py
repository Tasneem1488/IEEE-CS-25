from collections import deque

def find_path(n, m, grid):
    directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
    reverse_directions = {v: k for k, v in directions.items()}
    start, end = None, None

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'A':
                start = (i, j)
            elif grid[i][j] == 'B':
                end = (i, j)

    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {}

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            path = []
            while (x, y) != start:
                px, py = parent[(x, y)]
                path.append(reverse_directions[(x - px, y - py)])
                x, y = px, py
            return "YES", len(path), ''.join(reversed(path))

        for move, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
                parent[(nx, ny)] = (x, y)

    return "NO", None, None

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
result, length, path = find_path(n, m, grid)
print(result)
if result == "YES":
    print(length)
    print(path)
