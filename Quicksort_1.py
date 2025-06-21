def quickSort(arr):
    pivot = arr[0]
    left = []
    equal = []
    right = []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            right.append(num)

    return left + equal + right