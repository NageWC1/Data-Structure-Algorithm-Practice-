# this will contain all the concept and excercis in the file 
# implement the hash table 
class HashTable:
    def __init__(self):
        self.MAX = 10
        # here i am initializing the array with array instead of the None, because of the 
        # HashTable collision
        self.arr = [[] for i in range(self.MAX)] # declare and initialize the array 
    
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
#     def add(self, key, val):
#         h = self.get_hash(key) # here we taking the hash function for getting the index where the value going to store
#         self.arr[h] = val # store the value using the hash value which means the index to the array
   
#     we can use thise instead of  the above function
    def __setitem__(self, key, val):
        h = self.get_hash(key) # here we taking the hash function for getting the index where the value going to store
        # self.arr[h] = val # store the value using the hash value which means the index to the array
        # here isntead of replacing the value we can go through the list to insert the value
        # because we may think to update the same key's value - handle this situation first 
        
#        eneumerate is the function that use to iterate through the array 
        found = False 
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True 
                break
                
        # if the key does not exist in the list 
        if not found:
            self.arr[h].append((key,val))
            for element in self.arr[h]:
                if element[0] == key:
                    return element[1]
    
#     def get(self,key):
#         h = self.get_hash(key)
#         val = self.arr[h]
#         return val
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        h = self.get_hash(key) # this is used to find the index of the whole list array list 
        found = False
        for idx, element in enumerate(self.arr[h]): # then we go through each element in the arry list "h"th index
            # idx is indexes of elemnts inside the self.arr list
            # element is each pair of key and value in te "idx"th position
            if element[0] == key:
                del self.arr[h][idx]

# to check these will create a hash table like below
if __name__ == '__main__':
    t = HashTable()
    t.get_hash('march 6')

# adding the value to the hash table 
# t.add('march 6', 130)
t["march 6"] = 130 # instead passing the 2 argument in function we can use this by developing the python defaut function
t["march 17"] = 500

t.arr
