lst = [64, 25, 12, 22, 11]

# Traverse through all elements in the list
for i in range(len(lst)):
    # Find the minimum element in the remaining unsorted list
    min_idx = i
    for j in range(i+1, len(lst)):
        if lst[j] < lst[min_idx]:
            min_idx = j
    # Swap the found minimum element with the first element
    lst[i], lst[min_idx] = lst[min_idx], lst[i]

# Print the sorted list
print("Sorted list using Selection Sort:", lst)
