def binary_search(values, target):
    """Return the index of target in sorted values, or -1 if absent."""
    left, right = 0, len(values) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1

if __name__ == "__main__":
    assert binary_search([1, 3, 5, 7], 5) == 2
    assert binary_search([1, 3, 5, 7], 4) == -1
    print("binary search checks passed")