def find_sum(number):
    if number == 1: 
        return 1
    return number + find_sum(number -1)

def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo(n - 1) + fibo(n -2) 

if __name__ == "__main__":
    print(find_sum(5))
    print(fibo(7))