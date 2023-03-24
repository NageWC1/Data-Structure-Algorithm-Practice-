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
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None # wipe out all the value from the list 
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr  = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return count

    def print(self):
        if self.head is None:
            print("the link lis is empty")
            return
        
        itr = self.head

        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

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
    ll.print()

