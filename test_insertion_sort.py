# Test case
test_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = insertion_sort(test_list.copy())
print("Insertion Sort:", sorted_list)

# Count comparisons (elements compared during insertion)
comparisons = n - 1  # One comparison per element (except the first)
swaps = n - 1  # Similar to comparisons in most cases
print("Comparisons:", comparisons)
print("Swaps:", swaps)