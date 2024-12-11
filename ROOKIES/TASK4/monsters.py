from collections import deque

def escape_labyrinth(n, m, grid):
    directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
    reverse_directions = {v: k for k, v in directions.items()}
    player_start = None
    monster_starts = []

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'A':
                player_start = (i, j)
            elif grid[i][j] == 'M':
                monster_starts.append((i, j))

    player_queue = deque([player_start])
    monster_queue = deque(monster_starts)
    player_visited = {player_start: None}
    monster_distances = [[float('inf')] * m for _ in range(n)]

    while monster_queue:
        x, y = monster_queue.popleft()
        for dx, dy in directions.values():
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.' and monster_distances[nx][ny] == float('inf'):
                monster_distances[nx][ny] = monster_distances[x][y] + 1
                monster_queue.append((nx, ny))

    while player_queue:
        x, y = player_queue.popleft()
        if x == 0 or x == n - 1 or y == 0 or y == m - 1:
            path = []
            while (x, y) != player_start:
                px, py = player_visited[(x, y)]
                path.append(reverse_directions[(x - px, y - py)])
                x, y = px, py
            return "YES", len(path), ''.join(reversed(path))

        for move, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.' and (nx, ny) not in player_visited:
                if monster_distances[nx][ny] > len(player_visited):
                    player_visited[(nx, ny)] = (x, y)
                    player_queue.append((nx, ny))

    return "NO", None, None

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
result, length, path = escape_labyrinth(n, m, grid)
print(result)
if result == "YES":
    print(length)
    print(path)