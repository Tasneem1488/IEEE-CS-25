def max_books(n, t, a):
    start, total_time, max_books = 0, 0, 0
    for end in range(n):
        total_time += a[end]
        while total_time > t:
            total_time -= a[start]
            start += 1
        max_books = max(max_books, end - start + 1)
    return max_books

n, t = map(int, input().split())
a = list(map(int, input().split()))
print(max_books(n, t, a))
