def quick_sort(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return array

    pivot = array[0]

    less_than_pivot = [value for value in array if value < pivot]
    equal_to_pivot = [value for value in array if value == pivot]
    greater_than_pivot = [value for value in array if value > pivot]

    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)
