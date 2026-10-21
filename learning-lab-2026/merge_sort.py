def merge_sort(values):
    """Return a sorted copy using merge sort."""
    if len(values) < 2:
        return list(values)
    middle = len(values) // 2
    left, right = merge_sort(values[:middle]), merge_sort(values[middle:])
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: merged.append(left[i]); i += 1
        else: merged.append(right[j]); j += 1
    return merged + left[i:] + right[j:]

if __name__ == "__main__":
    assert merge_sort([5, 1, 4, 1, 0]) == [0, 1, 1, 4, 5]
    print("merge sort checks passed")