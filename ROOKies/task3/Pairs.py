def max_balanced_team(n, skills):
    skills.sort()
    left = 0
    max_team = 0

    for right in range(n):
        if skills[right] - skills[left] > 5:
            left += 1
        max_team = max(max_team, right - left + 1)
    
    return max_team

n = int(input())
skills = list(map(int, input().split()))
print(max_balanced_team(n, skills))
