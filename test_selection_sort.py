# Test case
test_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = selection_sort(test_list.copy())
print("Selection Sort:", sorted_list)

# Count comparisons (outer loop * inner loop iterations)
comparisons = n * (n-1)
swaps = n - 1  # One swap per iteration (except the last)
print("Comparisons:", comparisons)
print("Swaps:", swaps)