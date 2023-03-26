# going to implement the stack by the list or array 
class stack_:
    def __init__(self):
        self.links_ = ['link1','link2','link3','link4',]
        

    def pop(self):
        val =  self.links_[len(self.links_) - 1]
        del self.links_[len(self.links_) - 1] 
        return val
    
    def push(self, val):
        self.links_.append(val)
        return self.links_[len(self.links_) - 1]
    
    def print(self):
        return self.links_
    
    def is_empty(self):
        return len(self.links_) == 0
    
    def size(self):
        return len(self.links_)
    
if __name__ == '__main__':
    stack1 = stack_()
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.push(20))
    print(stack1.print())
    print(stack1.is_empty())
    print(stack1.size())



    from collections import deque
    stack = deque()

    # dir(stack) - will show the functions/ methods that we can use to manipulate the stack
    stack.append('link5')
    stack.append('link6')
    stack.append('link7')
    stack.append('link8')
    print(stack)
    print(stack.pop())
    print(stack)

