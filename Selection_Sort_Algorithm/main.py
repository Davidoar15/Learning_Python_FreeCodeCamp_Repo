def selection_sort(array):
    n = len(array)

    for i in range(n-1):
        pivot = array[i]

        for j in range(i+1, n):
            if array[i] > array[j]:
                pivot = array[j]
                array[j] = array[i]
                array[i] = pivot
    
    return array
