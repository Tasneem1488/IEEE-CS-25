n = int(input())

# List all lucky numbers up to 1000
lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

# Check if n is divisible by any lucky number
is_almost_lucky = any(n % lucky == 0 for lucky in lucky_numbers)

# Output the result
print("YES" if is_almost_lucky else "NO")
