def chocolates(n, times):
    left, right = 0, n - 1
    alice_time, bob_time = 0, 0
    alice_count, bob_count = 0, 0

    while left <= right:
        if alice_time <= bob_time:
            alice_time += times[left]
            alice_count += 1
            left += 1
        else:
            bob_time += times[right]
            bob_count += 1
            right -= 1

    return alice_count, bob_count

n = int(input())
times = list(map(int, input().split()))
result = chocolates(n, times
