def find_sum(number):
    sum = 0
    for i in range(len(1,number + 1)):
        sum += i
    return sum

if __name__ == "__main__":
    print(find_sum(5))