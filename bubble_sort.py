def bubble_sort(arr):
  """Sorts a list in ascending order using Bubble Sort algorithm.

  Args:
      arr: A list of sortable elements.

  Returns:
      A new list containing the sorted elements.
  """
  n = len(arr)
  # Flag to track if any swaps occurred
  swapped = True
  # Loop through all elements n-1 times
  for i in range(n-1):
    swapped = False
    # Compare adjacent elements and swap if needed
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swapped = True
    # If no swaps occurred in the inner loop, the list is already sorted
    if not swapped:
      break
  return arr