def count_pairs(t, test_cases):
    results = []
    for case in test_cases:
        n, l, r, a = case
        a.sort()
        count = 0
        for i in range(n):
            low = l - a[i]
            high = r - a[i]
            start = i + 1
            end = n - 1
            while start <= end:
                mid = (start + end) // 2
                if a[mid] < low:
                    start = mid + 1
                else:
                    end = mid - 1
            left = start
            start = i + 1
            end = n - 1
            while start <= end:
                mid = (start + end) // 2
                if a[mid] <=
