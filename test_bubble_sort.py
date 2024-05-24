# Test case
test_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(test_list.copy())  # Avoid modifying original list
print("Bubble Sort:", sorted_list)

# Count comparisons and swaps (nested loop iterations)
comparisons = (n-1) * n
swaps = 0  # Count swaps during execution
for i in range(n-1):
  for j in range(0, n-i-1):
    if arr[j] > arr[j+1]:
      swaps += 1
print("Comparisons:", comparisons)
print("Swaps:", swaps)