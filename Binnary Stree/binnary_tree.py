class BinarySearchTreeNode:
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
    
    def add_child_(self, data):
        # check the values is anyway in the tress, if that is in the tres
        # we dont need to insert ebecase the binnary tree will not have dublicate value
        if data == self.data:
            return
        
        if data < self.data:
            # add data to add left sub tree
            if self.left:
                self.left.add_child_(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data to right sub tree
            if self.right:
                self.right.add_child_(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_travesersal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_travesersal()
        
        # visit base node
        elements.append(self.data)

        # visit right node
        if self.right:
            elements += self.right.in_order_travesersal()

        return elements
    
    def search(self,val):

        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.min()
        
    def max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.max()

    def delete_(self, val):
        if val < self.data:
            if self.left:
               self.left =  self.left.delete_(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_val = self.right.min()
            self.data = min_val
            self.right = self.right.delete_(min_val)
        
        return self 


def build_tree(elemnts):
    root = BinarySearchTreeNode(elemnts[0])

    for i in range(1, len(elemnts)):
        root.add_child_(elemnts[i])
    
    return root

if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,28,34,18,4,17]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_travesersal())
    print(numbers_tree.search(200))

    # check by create string values 
    countries = ["India","Pakistan","Germany","USA","China","India","UK","USA"]
    country_tree  = build_tree(countries)

    print("UK is in the list?", country_tree.search("UK"))
    print("Sweeden is in the list?", country_tree.search("Sweeden"))
    # it will print in alphebatic order  
    print(country_tree.in_order_travesersal())

    # test delte 
    numbers_tree.delete_(20)
    numbers_tree.delete_(9)
    print("After delete the value 20: ",numbers_tree.in_order_travesersal())
    print("After delete the value 9: ",numbers_tree.in_order_travesersal())
# one of the unitility in the binnary tree is we can sort the list
# by using it 