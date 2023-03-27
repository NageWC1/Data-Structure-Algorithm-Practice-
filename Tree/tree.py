# here all the tree data strcuture will be implemented 
class TreeNode:
    def __init__(self, data):
        self.data = data
        # each of the element will be instance of the TreeNode, because children itself will be a tree
        self.children = [] 
        # this will store the parent property of the tree 
        self.parent = None
        # tree node is individual node within the tree 
    
    # adding the child to the tree 
    def add_child(self, child):
        # setting the current class will be the parent of the child, which mean the current class which 
        # calling the add_child wil be the parrent of this child 
        # when we creating electroning tree node : 1st 
        # then we calling the add_child to add a node call laptop (which basically another tree node) : 2nd
        # then the laptops paranet will eb electronic
        child.parent = self 
        self.children.append(child)

    def get_level(self):
        level = 0 
        p = self.parent
        while p:
            p += 1
            p = p.parent
        return level
    def print_tree(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_general_tree():
    root = TreeNode('Electronic')

    Laptop = TreeNode('Laptop')
    Laptop.add_child(TreeNode('Mac'))
    Laptop.add_child(TreeNode('Microsoft'))
    Laptop.add_child(TreeNode('thinkpad'))

    phone = TreeNode('Phone')
    phone.add_child(TreeNode('iphone'))
    phone.add_child(TreeNode('google pixel'))
    phone.add_child(TreeNode('vivo'))

    tv = TreeNode('TV')
    tv.add_child(TreeNode('Sumsung'))
    tv.add_child(TreeNode('LG'))

    root.add_child(Laptop)
    root.add_child(phone)
    root.add_child(tv)

    return root



if __name__ == '__main__':
    root = build_general_tree()
    root.print_tree()
    