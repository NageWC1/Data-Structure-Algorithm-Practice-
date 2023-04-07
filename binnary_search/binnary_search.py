def linear_search(number_list, number_to_find):
    for index, element in enumerate(number_list):
        if element == number_to_find:
            return index
    return -1 

def binnary_search(number_list, number_to_find):
    left_index = 0
    right_index = len(number_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = number_list[mid_index]

        if mid_number == number_to_find:
            return mid_index
        
        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    
    return -1


if __name__ == '__main__':
    number_list = [12,15,17,19,21,24,45,67]
    number_to_find = 45

    index = binnary_search(number_list, number_to_find)
    print(f"The index is {index} and the numbe is:",number_list[index])