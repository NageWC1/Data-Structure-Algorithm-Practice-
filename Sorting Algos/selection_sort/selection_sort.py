def find_min(arr):
    min = arr[0]
    for i in range(len(arr)):
        if arr[i] <= min:
            min = arr[i]
    return min 

def selection_sort(arr):
    size = len(arr)
    for i in range(size - 1):
        min_index = i
        for j in range(min_index + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == "__main__":
    elements = [78,23,12,15,61,53,63,27]
    selection_sort(elements)
    print(elements)


    test = [
        [89,78,34,56,43,23,24,4,5,3,24,2],
        [67,23,45,12,78,43],
        [],
        [23,12,34,2,5,3,12,32,3]
    ]

    for elements in test:
        selection_sort(elements)
        print(f'The sorted array: {elements}')
    