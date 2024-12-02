n = int(input())
directions = input()
positions = list(map(int, input().split()))

min_time = float('inf')

# Iterate through the particles to find the first collision
for i in range(n - 1):
    # Check if a collision can happen between particles i and i+1
    if directions[i] == 'R' and directions[i + 1] == 'L':
        # Calculate time to collision
        time = (positions[i + 1] - positions[i]) // 2
        min_time = min(min_time, time)

# Output the result
print(min_time if min_time != float('inf') else -1)
