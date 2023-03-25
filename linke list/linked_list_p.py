# implement the linked list using python 

# this is represent the induvidual elements in the list 
class Node:
    def __init__ (self, data=None, next=None):
        self.data = data # the value of element, can contain  integer , string or complex object
        self.next = next # this is pointer to the next element 

# we have head variable, which points to the heade the of the linked list 
class LinkedList:
    def __init__ (self):
        # slef head is a object that going to the beginning of the node of link list 
        self.head = None

    # this is responsible for inserting value to beggining of the list  
    def insert_at_beggining(self, data):
        node = Node(data, self.head)
        self.head = node 
    
    def insert_at_end(self, data):
        # check whether the head is none, that means the list is empty 
        # so we crating the for the head and next will none 
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        # the while loop is going to run until that retue true - the true is return when the variable having the value
        # this is used to find the end of the list 
        while itr.next:
            itr = itr.next
        # here we know that itr is in the last element because, above while loop will run until the itr.next have 
        # value, fi doen't have value is stop running, so here we will be at the end logically 
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None # wipe out all the value from the list 

        # then we go through all the value in the list - we can consider this as the noramla array contain
        # values 
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr  = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return count
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            print("This is not the valid index")
            raise Exception("Invalide index")
        
        if index == 0:
            self.head = self.head.next

        count = 0 
        itr = self.head
        while itr.next:
            # we stopping at the element that previous to the element that we going to delete 
            #  so we can point the previous element next to the element after the element that we going to delete
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            print("This is not the valid index")
            raise Exception("Invalide index")
        
        if index == 0:
            self.insert_at_beggining(data)
            return
        
        #  this is to check the index and stop to modify the list  
        count = 0
        # initialize the first elemnt to the itr
        itr = self.head
        # then we using that to go through the list
        while itr:
            # check the index to stop befor ethe element index wherer we want to indert value
            # because that is where the modification should start  
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break
        

            itr = itr.next
            count += 1
        
    def print(self):
        if self.head is None:
            print("the link lis is empty")
            return
        
        itr = self.head

        llstr = ''
        while itr:
            # llstr += str(itr.data) + ' Add: '+str(itr)+ '-->'
            llstr += str(itr.data) + '-->'
            itr = itr.next

        # print(llstr + "  " + str(itr))
        # i  put check is the next link address and originally the value show by programe for itr are same
        # cool its same
        print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_beggining(5)
    # ll.insert_at_beggining(15)
    # ll.insert_at_beggining(10)
    # ll.insert_at_end(154)
    # ll.insert_at_beggining(12)
    ll.insert_values(["hi","bye"])
    print("my linked list length is",ll.get_length())
    ll.remove_at(1)
    ll.insert_at(0, 10)
    ll.insert_at(1, 10)
    ll.insert_at(0, 15)
    ll.print()




# NOTE: is really the stored value in the next is the address of the next node, have to check on this 