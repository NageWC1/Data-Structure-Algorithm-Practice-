def shell_sort(arr):
    
    size = len(arr)
    gap = size // 2
    
    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2



if __name__ == "__main__":
    elements = [21,38,29,17,4,25,11,32,9]
    shell_sort(elements)
    print(elements)

    test = [
        [89,78,34,56,43,23,24,4,5,3,24,2],
        [67,23,45,12,78,43],
        [],
        [23,12,34,2,5,3,12,32,3]
    ]

    for elements in test:
        shell_sort(elements)
        print(f'The sorted array: {elements}')