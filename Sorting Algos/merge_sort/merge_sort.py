def merge_sort(arr):
    if len(arr) <= 1:
        return 
    
    # this whole process is to spit the array and send it to sort 2 sperate arrrays 
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(a,b,arr):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i]  <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    
    while j < len_b:
        arr[k] = b[j]
        j+=1
        k += 1

if __name__ == "__main__":
    a = [5,8,12,56,58]
    b = [7,8,45,51]
    arr = [75,14,25,36,45,75,84,54]

    # print(merge_two_sorted_lists(a,b))
    merge_sort(arr)
    print(arr)

    tests = [
        [11,9,29,7,2,15,28],
        [3,7,9,11],
        [25,22,21,10],
        [29,15,28],
        [],
        [6]
    ]

    for elements in tests:
        merge_sort(elements)
        print(f'sorted array: {elements}')