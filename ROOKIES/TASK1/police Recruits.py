n = int(input())
events = list(map(int, input().split()))

untreated_crimes = 0
available_officers = 0

for event in events:
    if event == -1:  # A crime occurs
        if available_officers > 0:
            available_officers -= 1  # Assign an officer to handle the crime
        else:
            untreated_crimes += 1  # No officers available, crime goes untreated
    else:  # Officers are recruited
        available_officers += event

print(untreated_crimes)
