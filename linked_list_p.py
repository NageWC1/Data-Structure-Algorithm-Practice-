# implement the linked list using python 

# this is represent the induvidual elements in the list 
class Node:
    def __init__ (self, data=None, next=None):
        self.data = data # the value of element, can contain  integer , string or complex object
        self.next = next # this is pointer to the next element 

# we have head variable, which points to the heade the of the linked list 
class LinkedList:
    def __init__ (self):
        self.head = None

    # this is responsible for inserting value to beggining of the list  
    def insert_at_beggining(self, data):
        node = Node(data, self.head)
        self.head = node 
    
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
    ll.insert_at_beggining(5)
    ll.insert_at_beggining(15)
    ll.insert_at_beggining(10)
    ll.insert_at_beggining(12)
    ll.print()

