def selection_sort(arr):
  """Sorts a list in ascending order using Selection Sort algorithm.

  Args:
      arr: A list of sortable elements.

  Returns:
      A new list containing the sorted elements.
  """
  n = len(arr)
  # Find the minimum element in unsorted array and swap with the first element
  for i in range(n):
    min_index = i
    for j in range(i+1, n):
      if arr[j] < arr[min_index]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
  return arr