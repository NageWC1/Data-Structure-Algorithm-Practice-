arr = [10,12,13,14,15,16,17]

# fining the elements by its index so, it will take: O(1) time - constant time
print(arr[0])

# senario 02: find out the day which have price 15 
# here the time will be: O(n) - becasue have to go through all the element by for loop 
for i in range(len(arr)):
    if arr[i] == 15:
        print("They day is:", i+1)
