n = int(input())
heights = list(map(int, input().split()))

max_height = max(heights)
min_height = min(heights)

index_of_max = heights.index(max_height)
index_of_min = len(heights) - 1 - heights[::-1].index(min_height)

# If the tallest comes before the shortest, we save one swap
if index_of_max > index_of_min:
    print(index_of_max + (n - 1 - index_of_min) - 1)
else:
    print(index_of_max + (n - 1 - index_of_min))
