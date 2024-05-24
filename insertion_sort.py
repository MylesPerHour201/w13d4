def insertion_sort(arr):
  """Sorts a list in ascending order using Insertion Sort algorithm.

  Args:
      arr: A list of sortable elements.

  Returns:
      A new list containing the sorted elements.
  """
  n = len(arr)
  # Insert each element into its correct position in the sorted sub-array
  for i in range(1, n):
    key = arr[i]
    j = i-1
    # Move elements of sorted sub-array that are greater than the key
    while j >= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key
  return arr